

import requests
from json_with_dates import loads
from bottle import run, route, static_file

PORT = 8000
REST_PORT = 54321

page_top = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Chinook Report</title>
    <link href="/static/style.css" rel="stylesheet"/>
</head>
<body>
<table class='grid'>
"""

page_end = """
</table>
</body>
</html>
"""

row_template = "<tr><td>{:3} </td><td> {:15} </td><td> {:15} </td><td> {:3} </td><td> {:8.2f}</td></tr>\n"


@route('/')
def send_report():
    lines = ""
    r = requests.get("http://localhost:{}/chinook/invoice-item/invoice/customer".format(REST_PORT))
    rows = loads(r.text)

    last_cust_id = -1
    last_invoice_id = -1
    last_fname = None
    last_lname = None
    running_tot = None
    running_count = None

    for (cust_id, fname, lname, inv_id, inv_tot) in rows:
        if cust_id != last_cust_id:
            if last_cust_id >= 0:
                line = row_template.format(last_cust_id, last_fname,
                                           last_lname, running_count, running_tot)
                lines += line
            running_tot = 0
            running_count = 0
            last_cust_id = cust_id
            last_fname = fname
            last_lname = lname
        elif inv_id != last_invoice_id:
            running_tot += inv_tot
            last_invoice_id = inv_id
        running_count += 1

    line = row_template.format(last_cust_id, last_fname,
                               last_lname, running_count, running_tot)
    lines += line
    return page_top + lines + page_end




@route('/static/<filepath:path>')
def send_static(filepath):
    print("send_static", filepath)
    return static_file(filepath, root='../web')



run(host='localhost', port=PORT, debug=True)

