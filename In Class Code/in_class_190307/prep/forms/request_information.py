

# import requests
# from json_with_dates import loads
from bottle import run, route, static_file, request, template

PORT = 8000

page_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Request Information</title>
</head>
<body>
    <table>
    % for (key, value) in sorted(environment.items()):
    <tr><td>{{key}}</td><td>{{value}}</td></tr>
    % end
    </table>
</body>
</html>
"""


@route('/')
def send_request_data():
    # rtval = str(request.environ.keys())

    rtval = template(page_template, environment=request.environ.copy())

    return rtval



@route('/static/<filepath:path>')
def send_static(filepath):
    print("send_static", filepath)
    return static_file(filepath, root='static')



run(host='localhost', port=PORT, debug=True)

