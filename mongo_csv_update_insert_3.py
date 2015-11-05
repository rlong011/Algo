import os
import csv
import pandas as pd
import numpy as np
import time as time
import pymongo as pmc
import pymongo
from csv import DictReader
from csv import reader as csvReader

##def add_spread_to_df(chunksize, file_in,file_out):
##    start_time = time.time()
##    for chunk in pd.read_csv(file_in, chunksize=chunksize):
##        df=chunk
##        #df.columns=['Timestamp','Ask price','Ask volume','Bid price','Bid volume']
##        df['spread']=df['Ask price'] - df['Bid price']
##
##        
##        if os.path.isfile(file_out):
##            df.to_csv(file_out,mode='a',header=False,float_format='%.5f')
##        else:
##           df.to_csv(file_out,mode='w',header=True,float_format='%.5f') 
    

start_time = time.time()
print(start_time)


db = pymongo.MongoClient('192.168.1.22').FXdata
db.eurusd_1m.delete_many({})
#reader = DictReader(open('EURUSD_1m_est_up.csv', 'r'))
reader = csvReader(open('EURUSD_1m_est_up.csv', 'r'))
header=['Ask volume','Ask price','Bid price','Bid volume','Timestamp','spread']
bulk = db.eurusd_1m.initialize_ordered_bulk_op()
for each in reader:
    row={}
    for field in header:
        row[field]=each[field]

    bulk.insert(row)
bulk.execute()
    
print(db.eurusd_1m.count())

print("--- %s Add seconds ---" % (time.time() - start_time))

##
##if __name__ == "__main__":
##    chunksize = 10
##    file_in ='EURUSD_50_est.csv'
##    file_out ='EURUSD_50_est_up.csv'
##    add_spread_to_df(chunksize, file_in,file_out)


#db.eurusd_50.insert_many([{'i':i} for i in DictReader(open('EURUSD_50_est.csv', 'r'))]).inserted_ids

##    for row in DictReader(open('EURUSD_50_est.csv', 'r')):
##        print(row)

##[{'i':i} for i in DictReader(open('EURUSD_50_est.csv', 'r'))]
##print(i)

##cols=['Timestamp','Bid price','Ask price','Bid volume','Ask volume']
##for row in (pd.read_csv('EURUSD_50_est.csv', header=0).to_dict()):
##    print(row)

##the_reader = DictReader(open('EURUSD_50_est.csv', 'r'))
##
##for row in the_reader:
##    print(row)


##    print("--- %s Add seconds ---" % (time.time() - start_time))
##
##
##if __name__ == "__main__":
##    chunksize = 10
##    file_in ='EURUSD_50_est.csv'
##    file_out ='EURUSD_2003-05-05_07252015_est_up.csv'
##    add_spread_to_df(chunksize, file_in,file_out)


#the_reader = DictReader(open('EURUSD_50_est.csv', 'r'))
 
##for chunk in pd.read_csv('EURUSD_1m_est.csv', chunksize=chunksize):
##        df=chunk    
##        df['spread']=df['Ask price'] - df['Bid price']
##        if os.path.isfile('/data/EURUSD_1m_est_up.csv'):
##            df.to_csv('EURUSD_1m_est_up.csv',mode='a',header=False,float_format='%.5f')
##        else:
##           df.to_csv('EURUSD_1m_est_up.csv',mode='w',header=True,float_format='%.5f') 
