from bottle import run, request, response, SimpleTemplate, route, static_file
import requests
from json import loads

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
    num = request.query.getall('area-select')
    r = requests.get("http://localhost:21212/measures/area")
    areas = loads(r.text)
    
    area_id = areas[0]
    name = area_id[1]
    id_num = area_id[0]

    if id_num != 1:
      return error(["You must construct additional pylons",
                    "You must provide: {}".format(areas)])
    else:
        ## name = area_id[1]
        template = SimpleTemplate(name="area_infos.html", lookup=["templates"])
        page =  template.render(str(id_num),name)
        return page


@route('/static/<filepath:path>')
def send_static(filepath):
    print("send static", filepath)
    return static_file(filepath, root='static')


run(host='localhost', port=PORT,debug=True)
