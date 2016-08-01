# Cython test

[Cython documentation - using C++ in Cython](http://docs.cython.org/en/latest/src/userguide/wrapping_CPlusPlus.html)

Command line usage:

```
python3 setup.py build_ext --inplace
python3
```

Now, inside the python3 terminal:

```
import example
rect = example.PyRectangle(1, 2, 3, 4)
rect.getXPos()
rect.getYPos()
rect.move(5, 5)
rect.getXPos()
rect.getYPos()
del rect
exit()
```

*Note*: The python terminal commands were not placed in a script so that the user can follow the output and c++ calls (which have printf() calls) as they are used.

