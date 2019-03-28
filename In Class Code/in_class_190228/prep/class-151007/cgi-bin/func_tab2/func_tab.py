#!c:/python34/python.exe
'''
Created on Oct 14, 2013

@author: ben
'''

import cgi
import cgitb
import jinja2

cgitb.enable()
import math
from function_table_error import page
from jinja2 import Environment, PackageLoader
from functions import functionMap

loader = jinja2.FileSystemLoader('templates')
#print("loader is ", loader)
env = Environment(loader=loader)


#def page(message):
#    print(message)

fldstor = cgi.FieldStorage()

try:
    start = float(fldstor.getfirst("start", 1))
    end = float(fldstor.getfirst("end",10))
    numrows = int(fldstor.getfirst("numrows", 5))
except Exception as exc:
    page("One of the values you entered did not convert properly", exc)
    quit()
    
functionList = fldstor.getlist("function")


if (start >= end):
    page("Start value should be less than the end value")
    quit()
elif  (start <= 0):
    page("Start value should be positive")
    quit()
elif (numrows < 2):
    page("There should be at least two rows in the table")
    quit()


# build an array of the function information
funcInfo = []
for f in functionList:
    funcInfo.append(functionMap[f])



# create the data

# amount of the step of x from one row to the next
step = (end-start)/(numrows-1)

data = []
step = (end-start)/(numrows-1)
for row in range(0,numrows):
    x = row*step+start
    rdat = [x]
    for f in functionList:
        if f in functionMap:
            rdat.append(functionMap[f][2](x))
    data.append(rdat)


print("Content-Type: text/html; charset=UTF-8")
print("")



template = env.get_template('function_table.html')
print(template.render(title='Jinja2 Function table', data=data, function_info=funcInfo))

#print(sys.path)
