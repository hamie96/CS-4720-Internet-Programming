#!c:/python34/python.exe
'''
Created on Oct 14, 2013

@author: ben
'''

import cgi
import cgitb
cgitb.enable()
import math
from function_table_error import page
#from func_tab.functions import functionMap

fldstor = cgi.FieldStorage()

try:
    start = float(fldstor.getfirst("start", 1))
    end = float(fldstor.getfirst("end",10))
    numrows = int(fldstor.getfirst("numrows", 5))
except Exception as exc:
    page("One of the values you entered did not convert properly", exc)
    quit()
    
functionList = fldstor.getlist("function")


def cube(x):
    return x*x*x

# map key to tuple
# tuple is: short title; description; function
functionMap = { "cube": ("Cube", "Cube function",
                    cube ),
               "square": ("Square", "Square function",
                          lambda x:  x*x),
               "ln":     ("Ln", "Natural logarithm",
                          lambda x: math.log(x)),
               "log2":   ("Log2", "Binary log, base 2 logarithm",
                          lambda x: math.log(x,2)),
               "atan":   ("ArcTan", "Arctangent",
                          lambda x: math.atan(x))
               }


if (start >= end):
    page("Start value should be less than the end value")
    quit()
elif  (start <= 0):
    page("Start value should be positive")
    quit()
elif (numrows < 2):
    page("There should be at least two rows in the table")
    quit()




# amount of the step of x from one row to the next
step = (end-start)/(numrows-1)

print("Content-Type: text/html; charset=UTF-8")
print("")

print ('''
<!DOCTYPE html>
<html>
    <head>
        <title>{}</title>
        <link rel="stylesheet" type="text/css" href="/style1.css"/>
    </head>
    <body>
'''.format("Function Table"))


print ('<table class="grid">')
print( "<tr><th>X</th>")
for f in functionList:
    if f in functionMap:
        print( "<th>{}</th>".format(functionMap[f][0]))
print( "</tr>")
for row in range(0,numrows):
    x = row*step+start
    print( "<tr><td class='numeric'>{:.3f}</td>".format(x))
    for f in functionList:
        if f in functionMap:
            print( "<td class='numeric'>{:.3f}</td>".format(functionMap[f][2](x)))
    print( "</tr>")
    
print( '</table>')

print('''
  </body>
</html>
''' )