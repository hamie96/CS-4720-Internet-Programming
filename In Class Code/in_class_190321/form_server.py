
from bottle import run, request, response, SimpleTemplate, route, static_file
import requests
from json import loads


PORT = 8000


def error(messages):
    template = SimpleTemplate(name="error_page.html", lookup=["templates"])
    page = template.render(messages=messages)
    return page


@route('/')
def album_list():
    r = requests.get("http://localhost:21212/album_list")
    a_list = loads(r.text)
    template = SimpleTemplate(name="album_select.html", lookup=["templates"])
    page = template.render(album_list=a_list)
    return page


@route("/album_info")
def album_info():
    album_id = request.query.getall("album-select")
    # what could go wrong?
    #   didn't get an id
    #           request.query.getall("album-select") returns a list of results
    #
    if len(album_id) != 1:
        # send back an error page
        return error(["You must provide exactly one album id",
                      "You provided: {}".format(album_id)])
    else:
        album_id = album_id[0]
        r = requests.get("http://localhost:21212/album_info/{}".format(album_id))
        #  404 error from server (?? why: bad id)
        # print("status", r.status_code)
        if r.status_code != 200:
            return error(["Error in REST Server",
                          "status code is {}".format(r.status_code)])
        else:
            info = loads(r.text)

            r = requests.get("http://localhost:21212/album_tracks/{}".format(album_id))
            tracks = loads(r.text)

            template = SimpleTemplate(name="album_info.html", lookup=["templates"])

            return template.render(album_info=info[0], tracks=tracks)



@route('/static/<filepath:path>')
def send_static(filepath):
    print("send_static", filepath)
    return static_file(filepath, root='static')



run(host='localhost', port=PORT, debug=True)

