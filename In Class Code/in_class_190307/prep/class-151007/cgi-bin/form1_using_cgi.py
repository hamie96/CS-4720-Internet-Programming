#!c:/python34/python.exe

__author__ = 'Ben'


import os

import cgi
import cgitb
cgitb.enable()

print( "Content-Type: text/plain; charset=UTF-8")
print()

form = cgi.FieldStorage()

op1 = form.getfirst("first-opnd","not present")
op1list = form.getlist("first-opnd")

op2 = form.getfirst("second-opnd","not present")
op2list = form.getlist("second-opnd")

print("op1", op1)
print( "op1list", op1list)
print( "op2", op2)
print( "op2list", op2list)