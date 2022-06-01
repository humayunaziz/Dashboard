import config
import pyodbc
import json


class DbUtility():
    def __init__(self):
        self.result = []

    def getCustomer(self):
        con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + config.SERVER +
                             ';DATABASE='+config.DATABASE+';UID='+config.USER_ID+';PWD=' + config.PASSWORD)
        query = 'SELECT * FROM Customer;'
        cursor = con.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        col_names = [column[0] for column in cursor.description]
        for row in data:
            self.result.append(dict(zip(col_names, row)))
        return self.result
