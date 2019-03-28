

from bottle import run, route, static_file

PORT = 8000


# @route('/web/')
# def send_home_page():
#     return static_file("index.html", root='web')


@route('/web<filepath:path>/')
def send_index(filepath):
    print("send_index", filepath)
    return static_file(filepath + "/index.html", root='web')


@route('/web/<filepath:path>')
def send_static(filepath):
    print("send_static", filepath)
    return static_file(filepath, root='web')



run(host='localhost', port=PORT, debug=True)

