#!/usr/bin/python
''' using MySQLdb '''

import MySQLdb
import re

# Open database connection
db = MySQLdb.connect("localhost","root","root","rcp_base" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS CIS")

# Create table as per requirement
sql_createtable = """CREATE TABLE CIS (
         ID_SPEC  INT NOT NULL,
         NAME  CHAR(50),
         GALENIC CHAR(50),
         WAY CHAR(20),
         AUTHORISATION CHAR(20),  
         LOCALIZATION CHAR(50),
         INSTORE CHAR(10),
         ID_WEB INT);"""

cursor.execute(sql_createtable)

# INSERT INTO DATABASE :
sql_insert = """INSERT INTO CIS VALUES (%s);"""

with open('CIS.txt', 'r', encoding='windows-1252') as f:
    for line in f:
        line_split = re.split(r'\t+', line)
        line_split = line_split[:-1]
        if len(line_split) == 7:
            line_split.append('0')
        line_str = str(line_split).strip('[]')
        sql_insert1 = sql_insert % line_str
        print(sql_insert1)
        cursor.execute(sql_insert1)
        db.commit()
        
# disconnect from server
db.close()