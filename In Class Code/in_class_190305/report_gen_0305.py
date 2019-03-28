

from bottle import route, run, request, static_file
from json_with_dates import loads, dumps
import requests

REST_PORT = 54321
WEB_PORT = 8080

page_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Chinook Summary Report</title>
    <link href="/web/style.css" rel="stylesheet"/>
</head>
<body>
<h1>Chinook Summary Report</h1>
{}
</body>
</html>
"""

@route("/")
def report():
    web_page = "<table>"
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
                template = "<tr><td>{}</td><td>  {}</td><td>  {}</td><td>  {}</td><td>  {:.2f}</td></tr>"
                line = template.format(last_cust_id, last_fname,
                                       last_lname, running_count, running_tot)
                web_page += line
            running_tot = 0
            running_count = 0
            last_cust_id = cust_id
            last_fname = fname
            last_lname = lname
        elif inv_id != last_invoice_id:
            running_tot += inv_tot
            last_invoice_id = inv_id
        running_count += 1

    template = "<tr><td>{:3}</td><td>  {:15}</td><td>  {:15}</td><td>  {:3}</td><td>  {:8.2f}</td></tr>"
    line = template.format(last_cust_id, last_fname,
                           last_lname, running_count, running_tot)
    web_page += line

    web_page += "</table>"

    return page_template.format(web_page)

@route('/web/<filepath:path>')
def send_static(filepath):
    print("send_static", filepath)
    return static_file(filepath, root='web')



run(host='localhost', port=WEB_PORT)



