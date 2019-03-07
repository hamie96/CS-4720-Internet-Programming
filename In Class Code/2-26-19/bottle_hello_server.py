
from bottle import route, run


@route('/hello/<name>')
def hello_handler(name):
    return "<h1>Hello {}</h1>".format(name)


@route("/goodbye/<code:int>")
def goodbye_handler(code):
    return "<h1>Goodbye!! {}</h1>".format(code)



run(host='localhost', port=8080, debug=True)

