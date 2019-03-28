__author__ = 'Ben'

import math


def cube(x):
    return x*x*x


functionMap = {"cube": ("Cube", "Cube function",
                        cube),
               "square": ("Square", "Square function",
                          lambda x:  x*x),
               "ln":     ("Ln", "Natural logarithm",
                          lambda x: math.log(x)),
               "log2":   ("Log2", "Binary log, base 2 logarithm",
                          lambda x: math.log(x, 2)),
               "atan":   ("ArcTan", "Inverse to tangent, arctangent",
                          lambda x: math.atan(x)),
               # "sqrt":   ("Sqrt", "Square Root",
               #            lambda x: math.sqrt(x)),
               }
