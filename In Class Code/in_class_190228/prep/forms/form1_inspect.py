

# import requests
# from json_with_dates import loads
from bottle import run, route, static_file, request, template, post

PORT = 8000

page_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Form1 Information</title>
    <link href="/static/style.css" rel="stylesheet"/>
</head>
<body>


    <h2>request.params</h2>
    
    <table class='grid'>
    <tr><th>name</th><th>getall</th><th>key as index</th></tr>
    % for key in sorted(params):
    <tr><td>{{key}}</td><td>{{params.getall(key)}}</td><td>{{params[key]}}</td></tr>
    % end
    </table>



    <h2>request.query</h2>
    
    <table class='grid'>
    <tr><th>name</th><th>getall</th><th>key as index</th></tr>
    % for key in sorted(query):
    <tr><td>{{key}}</td><td>{{query.getall(key)}}</td><td>{{query[key]}}</td></tr>
    % end
    </table>
    
    <h2>request.environ</h2>
    <table class='grid'>
    % for (key, value) in sorted(environment.items()):
    <tr><td>{{key}}</td><td>{{value}}</td></tr>
    % end
    </table>
</body>
</html>
"""


@post('/')
@route('/')
def send_request_data():
    # rtval = str(request.environ.keys())

    rtval = template(page_template, environment=request.environ.copy(),
                     query=request.query,
                     params=request.params)

    return rtval



@route('/static/<filepath:path>')
def send_static(filepath):
    print("send_static", filepath)
    return static_file(filepath, root='static')



run(host='localhost', port=PORT, debug=True)

