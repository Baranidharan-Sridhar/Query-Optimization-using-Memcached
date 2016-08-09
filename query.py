""""--------------------------------------------------------------------------------------------
Module Name :- query_RDS.py
Course Number : CSE6331
Lab number : Programming Assignment 2
Description : Program to query RDS database
Created Date : 02/28/2015
----------------------------------------------------------------------------------------------"""
__author__ = 'barae'

# import required libraries
import MySQLdb
import time
import memcache

import boto.elasticache

db = MySQLdb.connect(host="hostname",
                     user="", passwd="", port=3306, db="eq")

cur = db.cursor()
cur1=db.cursor()
#memc = MemcacheClient('')


memc = memcache.Client([''])

#print describe_response

#query_list = ["select * from earthquake where mag > 2.0","select * from earthquake where rms > 1.0","select * from earthquake where depth > 100.0"]

##
def mem_query():
    """function to run 2000 random queries with caching and calculate the time"""

    start = time.time()
    query = "select * from fatality where Fatality_SEX='M'or fatality_location like '%open'"
    query1 = "select count(*) from fatality where Fatality_SEX='M'or fatality_location like '%open'"
    cache = memc.get("query" + str(1))
    if not cache:
        
        cur.execute(query1)
        data1=cur.execute(query1)
        print data1
        cur.execute(query)
        data = cur.fetchall()
        print data
        memc.set("query" + str(1),data,300)
    else:
        for rows in cache:
            #print "Available in cache" + "query " + str(rand)
            pass


    end = time.time()
    print "From Cache",end - start

#query()
mem_query()
##limit_query()
##limit_mem_query()
##db.close()
