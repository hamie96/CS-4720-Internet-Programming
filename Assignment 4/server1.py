# Hamilton Bradford
# Assignment 4
# Compiled on Python 3.7

from bottle import route, run, response

from db_access import get_all_areas, get_locations_for_area, get_measurements_for_location, get_categories_for_area
from db_utility import get_average_measurements_for_area, number_of_locations_by_area

from json_with_dates import dumps

@route("/measures/area")
def area():
    area = get_all_areas()
    response.content_type = "application/json"
    return dumps(area)

@route("/measures/area/categories/<area_id:int>")
def categories_for_area(area_id):
    categories_area = get_categories_for_area(area_id)
    response.content_type = "application/json"
    return dumps(categories_area)

@route("/measures/area/average/<area_id:int>")
def average_measurements_for_area(area_id):
    average_measurements = get_average_measurements_for_area(area_id)
    response.content_type = "application/json"
    return dumps(average_measurements)

@route("/measures/area/location/num/<area_id:int>")
def numb_of_locations_by_area(area_id):
    num_location = number_of_locations_by_area(area_id)
    response.content_type = "application/json"
    return dumps(num_location)


run(host='localhost', port=21212)
