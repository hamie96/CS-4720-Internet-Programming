
# Hamilton Bradford
# Assignment 4
# CS4720 Internet Programming
# Compiled on Python 3.7

import requests
import time
from json_with_dates import loads

PORT = 21212

t0 = time.time()

area_request = requests.get("http://localhost:21212/measures/area")
areas = loads(area_request.text)

count = 1
line_format = '{:<3} {:<19} {:<6}'
line_format2 = '{:<3} {:<16} {:<6} {:<6} {:<14}'
print(line_format2.format("ID", " Name", " N. Loc ", "Avg", "Categories"))

areaid = 1
num_loc = []

for i in areas:
    location_request = requests.get("http://localhost:21212/measures/area/location/num/{}".format(areaid))
    num_location = (loads(location_request.text))
    num_loc.append(num_location)
    areaid = areaid + 1

areaid = 0

for area in areas:
    category_request = requests.get("http://localhost:21212/measures/area/categories/{}".format(area[0]))
    category = loads(category_request.text)
    avg_request = requests.get("http://localhost:21212/measures/area/average/{}".format(area[0]))
    average = loads(avg_request.text)

    print(line_format.format(str(area[0]),str(area[1]),str(num_loc[areaid])),end= " ")

    if average is None:
        pass
    else:
        print(str(round(average,2)),end=" ")

    for i in category:
        print(str(i[1]),end=" ")

    areaid = areaid + 1
    print()


t1 = time.time()
print("Program ran in " + str(round(t1-t0,4)) + " seconds")
