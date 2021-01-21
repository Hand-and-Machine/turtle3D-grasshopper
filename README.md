# turtle3D for Grasshopper

A Python library implementing 3D graphics in a way that can be used within [Grasshopper](https://www.grasshopper3d.com/).

## Installing

Download [the turtle3D.py script](https://git.sr.ht/~boringcactus/turtle3D-grasshopper/blob/main/turtle3D.py) and place it somewhere on your computer, in a folder by itself.
Then open Rhino, go to Tools > PythonScript > Edit..., go to Tools > Options, and in the Files tab, under Module Search Paths, click the "Add to search path" button, and then find the folder you put turtle3D.py in.

## Using

Add the following script to a Grasshopper Python node:

```python2
from turtle3D import *

home()
pendown()
forward(10)
right(45)
forward(12)
right(90 + 45)
tiltdown(30)
forward(20)
a = lines()
```

This will create a turtle automatically, provide it the given instructions, and output the lines it has drawn to the `a` output of the Python node.

**Important**: If you omit the call to `home()` at the start of the code, you will get a `NullReferenceException` when the Python node runs for a second time.
I do not know why this happens, but I believe it has something to do with the fact that the implicitly-created turtle is persisted between runs of the Python node.

## Multiple Turtles

If you wish to create turtles explicitly, or you wish to keep imported names to a minimum to avoid name collisions, this code will have the same effect as the above code:

```python2
from turtle3D import Turtle

turtle = Turtle()
turtle.pendown()
turtle.forward(10)
turtle.right(45)
turtle.forward(12)
turtle.right(90 + 45)
turtle.tiltdown(30)
turtle.forward(20)
a = turtle.lines()
```

## License

This library is released under the terms of the [Anti-Capitalist Software License](https://anticapitalist.software) v1.4.
