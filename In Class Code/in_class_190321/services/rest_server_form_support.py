
from bottle import run, route, response
from services import chinook_services
import json

PORT = 21212

@route('/album_list')
def album_list():
    alist = chinook_services.album_list()
    response.content_type = "application/json"
    return json.dumps(alist)

@route('/album_info/<album_id:int>')
def album_info(album_id):
    info = chinook_services.album_info(album_id)
    response.content_type = "application/json"
    return json.dumps(info)

@route("/album_tracks/<album_id:int>")
def album_tracks(album_id):
    tracks = chinook_services.album_tracks(album_id)
    response.content_type = "application/json"
    return json.dumps(tracks)

@route("/track_info/<track_id:int>")
def track_info(track_id):
    info = chinook_services.track_info(track_id)
    response.content_type = "application/json"
    return json.dumps(info)


run(host='localhost', port=PORT, debug=True)

