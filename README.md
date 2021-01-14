# turtle3D for Grasshopper

A Python library implementing 3D graphics in a way that can be used within [Grasshopper](https://www.grasshopper3d.com/).

## Installing

Download the turtle3D.py script and place it somewhere on your computer, in a folder by itself.
Then open Rhino, go to Tools > PythonScript > Edit..., go to Tools > Options, and in the Files tab, under Module Search Paths, click the "Add to search path" button, and then find the folder you put turtle3D.py in.

## Using

Add the following script to a Grasshopper Python node:

```python2
from turtle3D import *

pendown()
forward(10)
right(45)
forward(12)
right(90 + 45)
forward(20)
a = lines()
```

## License

This library is released under the terms of the [Anti-Capitalist Software License](https://anticapitalist.software) v1.4.
