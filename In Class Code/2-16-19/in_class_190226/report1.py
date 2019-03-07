import requests
from previous.json_with_dates import loads

PORT = 21212

area_request = requests.get("http://localhost:21212/measures/area")
areas = loads(area_request.text)

count = 1

for area in areas:
    area_id = area[0]
    location_request = requests.get("http://localhost:21212/measures/area/location/{}".format(area_id))
    num_location = loads(location_request.text)

for i in num_location:
    print(i)

#print("all areas:")
#for area in areas:
    #print(area)
