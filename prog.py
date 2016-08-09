import boto
import MySQLdb
import csv
import time

key='A'
secret=''
s3 = boto.connect_s3(key,secret)

def upload():
    bucket = s3.get_bucket('barae')  
    key = bucket.new_key('baranidharan.csv')
    key.set_contents_from_filename('baranidharan.csv')
    key.set_acl('public-read')

def download():
    key = s3.get_bucket('barae').get_key('baranidharan.csv')
    key.get_contents_to_filename('baranidharan.csv')
    print 'soomething'
def sqlconnector():
    counter=0
    file_name = "baranidharan.csv"
    
    #establish the connection with RDS
    db = MySQLdb.connect(host="hostname",
                     user="", passwd="", port=3306, db="eq")
    cur = db.cursor()
    #print cur
    
    insert_query = """insert into fatality values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    start_time = time.time()
    
    try:
        with open(file_name, "rb") as f: # Read data from csv'
            
            data = csv.reader(f, delimiter=",")
            print data
            for row in data:
                if counter <> 0:
                
                    cur.execute(insert_query, (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7],
                    row[8], row[9],row[10]))
                    db.commit()
                else:
                    counter+=1
        cur.close()
        db.close()
        end_time = time.time()
        total_time = end_time - start_time
        print "Completed"
        print "Time for insertion",str(total_time)
    except:
        print "Cannot insert data, check the input file"


sqlconnector()
