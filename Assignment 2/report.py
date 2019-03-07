# Hamilton Bradford
# Assignment 2 - Internet Programming
# Compiled using Python 3.7


import db_access
import db_utility


side = '||'
space = 18
line_format = side + ' {:>4}   {:<25}   {:<10}  {:^12}  {:' + str(space + 1) + '} '
line_format2 = side + ' {:^' + str(60 + space + len(side)) + '} '
print(line_format.format("ID", "Name", "Num Loc", "Avg Value", "Categories"))


for i in db_access.get_all_areas():
    avg = db_utility.get_average_measurements_for_area(i[0]) # calculate average
    print(line_format.format(i[0], i[1], db_utility.number_of_locations_by_area(i[0]),  # areaId, name, num of locations
                             "-----" if avg is None else str(round(avg, 2)), # avg measurement, round 2 decimals
                             str(", ".join(str(j[1]) for j in db_access.get_categories_for_area(i[0])))))

