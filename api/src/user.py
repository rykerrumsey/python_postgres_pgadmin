import json
import psycopg2
from flask_restful import Resource

class Users(Resource):
    def get(self):
        conn = psycopg2.connect("host='postgres' dbname='postgres' user='postgres' password='password'")

        cur = conn.cursor()
        cur.execute("select * from users")

        column_array = [desc[0] for desc in cur.description]
        rows = cur.fetchall()

        cur.close()
        conn.close()

        data = []

        for row in rows:
            obj = {}
            for column in range(0, len(column_array)):
                obj[column_array[column]] = row[column]
            data.append(obj)

        return data, 200
