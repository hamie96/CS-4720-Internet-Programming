
import db_access
from statistics import mean

def get_average_measurements_for_area(area_id):
    """
    Returns the average value of all measurements for all locations in the given area.
    Returns None if there are no measurements.
    """
    locations = db_access.get_locations_for_area(area_id)

    if len(locations) == 0:
        return None
    else:
        return_table = []
        for i in locations:
            for k in db_access.get_measurements_for_location(i[0]):
                return_table.append(k[1])
        return mean(return_table)
def number_of_locations_by_area(area_id):
    """
    Returns the number of locations for the given area.
    """

    if area_id == '':
        raise Exception("area ID could not be ''")

    locations = db_access.get_locations_for_area(area_id)

    return len(locations)
