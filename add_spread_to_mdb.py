import os
import csv
import time as time
from csv import DictReader
import pandas as pd



def add_spread_to_mdb(chunksize, file_in,file_out):
    start_time = time.time()
    for chunk in pd.read_csv(file_in, chunksize=chunksize):
        df=chunk
        #df.columns=['Timestamp','Ask price','Ask volume','Bid price','Bid volume']
        df['spread']=df['Ask price'] - df['Bid price']

        
        if os.path.isfile(file_out):
            df.to_csv(file_out,mode='a',header=False,float_format='%.5f')
        else:
           df.to_csv(file_out,mode='w',header=True,float_format='%.5f') 


    print("--- %s Add seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    chunksize = 1000000
    file_in ='EURUSD_09122015_est.csv'
    file_out ='EURUSD_09122015_est_up.csv'
    add_spread_to_mdb(chunksize, file_in,file_out)
