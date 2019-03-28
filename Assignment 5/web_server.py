from bottle import run, route, static_file, response
import requests
from json_with_dates import loads

# Hamilton Bradford
# Assignment 5
# March 14, 2019
# CS 4702


PORT = 8085
REST_PORT = 21212

page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>REPORT</title>
    <link href='style.css' rel='stylesheet'>
</head>
<body>
<h1>Web Report</h1>
'''

page_tail = '''
</body>
</html>
'''

header_template = '<tr> <th>{:<5}</th> <th>{:<12}</th> <th>{:<8}</th> <th>{:<16}</th> <th>{:<9}</th> </tr>'
template = "<tr> <td>{:<3}</td> <td>{:<16}</td> <td>{:<6}</td> <td>{:6}</td> <td>{:<14}</td> </tr>"

@route('/')
def report():
    header = header_template.format("ID","Name","N. Loc", "Categories", "Average")
    web_line = '<table>' + header

    area_request = requests.get('http://localhost:{}/measures/area'.format(REST_PORT))
    areas = loads(area_request.text)
    
    for area in areas:
        location_request = requests.get('http://localhost:{}/measures/area/location/num/{}'.format(REST_PORT,area[0]))
        num_location = loads(location_request.text)

        category_request = requests.get('http://localhost:{}/measures/area/categories/{}'.format(REST_PORT,area[0]))
        category = loads(category_request.text)

        cat_string = ''
        for cat in category:
            if cat is None:
                cat_string = '-----'
            else:
                cat_string += cat[1] + " "

        average_request = requests.get('http://localhost:{}/measures/area/average/{}'.format(REST_PORT,area[0]))
        average = loads(average_request.text)
        
        if average is None:
            average = "----"

        web_line += template.format(area[0],area[1],num_location,str(cat_string),average)

    return page_head + web_line + "</table>" + page_tail

@route('/static/<filepath:path>')
def send_static(filepath):
    print("send_static", filepath)
    return static_file(filepath, root='static')

run(host='localhost',port=PORT)
