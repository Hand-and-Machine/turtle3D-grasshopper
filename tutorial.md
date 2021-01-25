# Making a Procedurally Generated Bowl with turtle3D for Grasshopper

Assumes you've already [installed turtle3D for Grasshopper](https://git.sr.ht/~boringcactus/turtle3D-grasshopper#installing) and you're familiar with intermediate Grasshopper features like input expressions.

1.  Add a slider "move" over the real numbers ranging from 0.1 to 5.0.
2.  Add a slider "turn" over the real numbers ranging from 0.1 to 45.0.
3.  Add a slider "tilt" over the real numbers ranging from 0.1 to 45.0.

4.  Create a domain from -turn to turn.
5.  Create a domain from tilt-1 to tilt+1.
6.  Create a slider "steps" over the integers ranging from 2 to 50.

7.  Generate random numbers (Sets > Sequence > Random) with a range based on "turn" and a number set to "steps".
8.  Generate random numbers with a range based on "tilt" and a number set to "steps".
9.  Generate a random number with a range set to "0 To 360" (leave the number at 1).

10. Add a Python node.
    Give it four inputs: `move`, `first_turn`, `turns`, and `tilts`.
    Right-click on each of `turns` and `tilts` and set them to "List Access".
    Connect `move` to the "move" slider, `first_turn` to the single random number from 0 to 360, and `turns` and `tilts` to the random sequences generated from steps 7 and 8, respectively.
    Give the node this script:
    ```python
    from turtle3D import *

    home()
    right(first_turn)
    pendown()
    for this_turn, this_tilt in zip(turns, tilts):
        forward(move)
        tiltup(this_tilt)
        right(this_turn)
    a = lines()
    ```

11. Add a slider "radius" over the real numbers
 ranging from 0.100 to 5.000.
12. Make a Pipe (Surface > Freeform) with the curve coming from the Python node's `a` output, the radius coming from the slider, and the caps set to Round (right-click the E input to set that).

13. Add a slider "first seed" over the integers ranging from 0 to 100.
14. Add a slider "iterations" over the integers ranging from 2 to 100.
15. Add a Series (Sets > Sequence) starting at "first seed", stepping by 1, for "iterations" numbers.
    Connect the output to the Seed inputs of each of the random number generators created previously.
16. Add a Solid Union (Intersect > Shape) pulling input from the Pipe created earlier.
    Right-click the output of the Pipe and set it to "Flatten".

Now you should have a funky bowl that is randomly generated based on the seed settings you use!
It won't look much like a bowl when your iterations slider is below 10 (and even then it's a stretch), but by that point your computer will have a hard time keeping up with you if you're fine-tuning your parameters.
For me, at least, the bottleneck was actually the Pipe node, so you might want to use a Trigger node or right-click and disable it while you're playing with your sliders.
It's still easy to visualize what's going on with just the polyline view, but it's way easier for Grasshopper to calculate.
