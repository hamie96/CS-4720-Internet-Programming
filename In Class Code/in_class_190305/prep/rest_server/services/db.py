__author__ = 'Ben'

import sqlite3
#
# def dictionary_factory(cursor, row):
#     """
#     Create a dictionary from rows in a cursor result.
#     The keys will be the column names.
#     :param cursor: A cursor from which a query row has just been fetched
#     :param row: The query row that was fetched
#     :return: A dictionary associating column names to values
#     """
#     col_names = [d[0] for d in cursor.description]
#     return dict(zip(col_names, row))

from os.path import split, join


class DbConnector:

    def __init__(self, db_file_path):
        self.file_path = db_file_path

    def _get_connection(self):
        this_dir = split(__file__)[0]
        fname = join(this_dir, self.file_path)
        # print("fname", fname)
        conn = sqlite3.connect(fname)
        # conn.row_factory = dictionary_factory
        return conn

    def do_command(self, cmd, args=None):
        conn = self._get_connection()
        try:
            crs = conn.cursor()
            if args:
                crs.execute(cmd, args)
            else:
                crs.execute(cmd)
            return crs.fetchall()
        finally:
            conn.close()

