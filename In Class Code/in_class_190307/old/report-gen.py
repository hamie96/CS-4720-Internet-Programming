

from bottle import run, route, static_file
import requests
from json_with_dates import loads

PORT = 8000
REST_PORT = 54321

page_head = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Report</title>
    <link rel='stylesheet' href='/web/style.css'/>
</head>
<body>
<h1>Chinook Customer List</h1>
"""

page_tail = """
</body>
</html>
"""


@route('/')
def report():
    r = requests.get("http://localhost:{}/chinook/invoice-item/invoice/customer".format(REST_PORT))
    rows = loads(r.text)

    table = "<table>"
    for row in rows:
        r = "<tr>"
        for x in row:
            r += "<td>" + str(x) + "</td>"
        r += "</tr>"
        table += r
    table += "</table>"
    print(table)
    return page_head + table +  page_tail


@route('/web/<filepath:path>')
def send_static(filepath):
    print("send_static", filepath)
    return static_file(filepath, root='web')



run(host='localhost', port=PORT, debug=True)

