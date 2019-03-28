'''
Created on Oct 16, 2013
Modified 1/30/2019
    SimpleTemplate from bottle replaces Jinja2

Error page for the function_table script


@author: ben
'''

from bottle import template

page_template = """
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title>Function Table Error</title>
    <link rel="stylesheet" type="text/css" href="/static/style1.css"/>
</head>
<body>
    <h1>There was an input error!</h1>
    % for message in messages:
        <h2 style='color:red'>{{ message }}</h2>
    % end

    <h3>Backup to the entry page and try again!</h3>

</body>
</html>
"""


def page(*messages):
    page = template(page_template, messages=messages, )
    return page
