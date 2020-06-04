import sqlite3


class BaseDB(object):
    def __init__(self):
        self._conn = None

    def connect(self, file_path):
        self._conn = sqlite3.connect(file_path)

    def delete_table(self, table):
        self._conn.execute(f"drop table if exists {table}")
        self._conn.commit()

    def add_column(self, table, column, column_type):
        self._conn.execute(f"alter table {table} add column {column} {column_type}")
        self._conn.commit()

    def execute(self, sql):
        cursor = self._conn.execute(sql)
        self._conn.commit()
        return cursor

    def count_rows(self, row, table):
        cursor = self._conn.execute(f"select count({row}) FROM {table}")
        for row in cursor:
            return row[0]

    def close(self):
        self._conn.close()
