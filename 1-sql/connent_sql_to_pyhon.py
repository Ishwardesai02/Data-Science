# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 10:40:53 2024

@author: ishwa
"""

import psycopg2 as pg2

#Create a conection with postgresql
#'paasword' whatever you have set for postgresql
conn=pg2.connect(database='dvdrental',user='postgres',password='root')

#Establish connevction and start the cursor to be ready to query
cur=conn.cursor()

#Pass in a postgresql query as a string
cur.execute ("select * from payment")

#rerurn a tuple of the first row as python objects
cur.fetchone()

#return n number of rows
cur.fetchmany(10)

#return all the rows at once
cur.fetchall()

conn.close()

