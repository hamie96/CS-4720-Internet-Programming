

from bottle import run, route, SimpleTemplate, static_file, request
import bottle_beaker
# from services.chinook_services import album_list, album_info
from services import chinook_services

PORT = 8080



@route("/")
def choice_page():
    tmp = SimpleTemplate(name="choose_album.html", lookup=["."])
    # page = tmp.render(albums=[(1, "A"), (2, "B")])
    page = tmp.render(albums=chinook_services.album_list())
    return page


@route('/static/<filepath:path>')
def send_static(filepath):
    print("send_static", filepath)
    return static_file(filepath, root='static')

@route('/album')
def album_info():
    album_id = request.query["album"]
    # info = chinook_services.album_info(album_id)
    tmp = SimpleTemplate(name="album_info.html", lookup=["."])
    page = tmp.render(info=chinook_services.album_info(album_id)[0],
                      tracks=chinook_services.album_tracks(album_id))
    return page

@route('/track-info')
def track_info():
    track_id = request.query["track-id"]
    info = chinook_services.track_info(track_id)
    tmp = SimpleTemplate(name="track_info.html", lookup=["."])
    page = tmp.render(track_info=info[0])
    return page

@route('/add_to_cart')
def add_to_cart():
    cart_additions = request.query.getall("cart-selected")
    # ca = "(" +  ",".join(cart_additions) + ")"
    # ca = [(int(x),) for x in cart_additions]
    tracks_info = chinook_services.tracks_info(cart_additions)
    tmp = SimpleTemplate(name="cart.html", lookup=["."])
    page = tmp.render(selected=cart_additions, tracks=tracks_info)
    return page
    # return "the cart " + str(cart_additions)

run(host='localhost', port=PORT, debug=True)
