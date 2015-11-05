import os
import csv
import time as time
from csv import DictReader
import pandas as pd

os.chdir('/data')
try:
    os.remove(file_out)
except:
    pass

def add_spread_to_mdb(chunksize, file_in,file_out):
    start_time = time.time()
    for chunk in pd.read_csv(file_in, chunksize=chunksize):
        df=chunk
        #df.columns=['Timestamp','Ask price','Ask volume','Bid price','Bid volume']
        df['spread']=df['Ask price'] - df['Bid price']
        #print(df)
        
        if os.path.isfile(file_out):
            df.to_csv(file_out,mode='a',header=False,index=False,float_format='%.5f')
        else:
            df.to_csv(file_out,mode='w',header=True,index=False,float_format='%.5f') 


    print("--- %s Add seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    chunksize = 1000000
    symbol='EURUSD'
    file_in     = symbol +'_100k_est.csv'
    file_out    = symbol +'_100k_est_up2.csv'
    #file_in     = symbol +'_2003-05-05_09122015_est.csv'
    #file_out    = symbol +'_2003-05-05_09122015_est_up.csv'
    add_spread_to_mdb(chunksize, file_in,file_out)
