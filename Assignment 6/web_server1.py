from bottle import run, request, response, SimpleTemplate, route, static_file
import requests
from json import loads

# Hamilton Bradford
# Internet Programming
# Assignment 6

PORT = 8000
REST_PORT = 21212

def error(messages):
    template = SimpleTemplate(name='error_page.html', lookup = ['templates'])
    page = template.render(messages=messages)
    return page

@route('/')
def area_list():
    r = requests.get("http://localhost:21212/measures/area")
    a_list = loads(r.text)
    template = SimpleTemplate(name ="area_select.html", lookup = ['templates'])
    page = template.render(area_list=a_list)
    return page

@route('/area_info')
def area_info():
    area_id = int(request.params['area-select'])
    r = requests.get("http://localhost:21212/measures/area/{}".format(area_id))
    area_id = r[0]

    category_request = requests.get("http://localhost:21212/measures/area/categories/{}".format(area_id))
    categories = loads(category_request.text)

    avg_request = requests.get("http://localhost:21212/measures/area/average/{}".format(area_id))
    average = loads(avg_request.text)

    location_request = requests.get("http://localhost:21212/measures/area/locations/num/{}".format(area_id))
    num_of_locations = loads(location_request.text)

    return template("area_info.html", name = area_id[1], area_id=area_id[0], categories = categories, average = average, num_of_locations=num_of_locations, lookup=["templates"])
    
    #template = SimpleTemplate(name="area_infos.html", lookup=["templates"])
    #page =  template.render(id_num,name)
    #return page


@route('/static/<filepath:path>')
def send_static(filepath):
    print("send static", filepath)
    return static_file(filepath, root='static')


run(host='localhost', port=PORT,debug=True)
