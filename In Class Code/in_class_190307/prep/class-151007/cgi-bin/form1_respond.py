#!c:/python34/python.exe

__author__ = 'Ben'

import os
import re
import sys
import urllib
import cgitb
cgitb.enable()



print("Content-Type: text/html; charset=UTF-8")
print()

print('''
<!DOCTYPE html>
<html>
    <head>
        <title>form1 response</title>
        <link rel="Stylesheet" type="text/css" href="/style1.css"/>
    </head>
    <body>
''')


method = os.environ.get('REQUEST_METHOD','').lower()

if method == 'post':
    print("<p>method: {}</p>".format( method))
    sent_data = sys.stdin.read()
elif method == 'get':
    print("<p>method: {}</p>".format( method))
    sent_data = os.environ.get('QUERY_STRING','')
else:
    print("<p>method not expected: {}</p>".format( method))
    sent_data = ''

if sent_data:
    pairs = re.split('&', sent_data)

    print("<h2>Pairs</h2>")
    for p in pairs:
        print("<p>{}</p>".format(p))

    print("<h2>Split pairs</h2>")
    print("<table class='grid'>")
    for p in pairs:
        (key, value) = re.split('=', p)
        print("<tr><td>{}</td><td>{}</td></tr>".format(key, value))
    print('</table>')


    print("<h2>Split pairs, Unquoted</h2>")
    print("<table class='grid'>")
    for p in pairs:
        (key, value) = re.split('=', p)
        value = urllib.parse.unquote_plus(value)
        print("<tr><td>{}</td><td>{}</td></tr>".format(key, value))
    print('</table>')




print('''
    </body>
</html>
''')