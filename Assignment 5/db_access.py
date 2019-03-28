# Hamilton Bradford
# Assignment 2 - Internet Programming
# Compiled on Python 3.7
# DID NOT USE PYCHARM

from sqlite3 import *

def get_all_areas():
    """
    Returns a list of dictionaries representing all the rows in the
    area table.
    """
    con = connect('measures.sqlite')
    cur = con.cursor()
    cur.execute("select * from area")
    results = []
    for row in cur.fetchall():
        results.append(row)

    con.close()

    return results

def get_locations_for_area(area_id):
    """
    Return a list of dictionaries giving the locations for the given area.
    """
    con = connect('measures.sqlite')
    cur = con.cursor()
    cur.execute('select * from location where location_area = ?', (area_id,))
    return_table = []
    
    for row in cur:
        return_table.append(row)

    con.close()
    return return_table

def get_measurements_for_location(location_id):
    """
    Return a list of dictionaries giving the measurement rows for 
    the given location.
    """
    con = connect('measures.sqlite')
    cur = con.cursor()
    cur.execute('select * from measurement where measurement_location = ?', (location_id,))
    results = cur.fetchall()
    con.close()

    return results

def get_categories_for_area(area_id):
    """
    Return a list of rows from the category table that all 
    contain the given area.
    """
    con = connect('measures.sqlite')
    cur = con.cursor()
    cur.execute('select category.* from category,category_area where category.category_id = category_area.category_id and category_area.area_id = ?', (area_id,))
    return_table = []
    for row in cur:
        return_table.append(row)

    con.close()
    return return_table
