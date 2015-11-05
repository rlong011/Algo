import os
import csv
import pandas as pd
import numpy as np
import time as time


def add_spread_to_df(chunksize, file_in,file_out):
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
    chunksize = 3000000
    file_in ='EURUSD_2003-05-05_07252015_est.csv'
    file_out ='EURUSD_2003-05-05_07252015_est_up.csv'
    add_spread_to_df(chunksize, file_in,file_out)

 
##for chunk in pd.read_csv('EURUSD_1m_est.csv', chunksize=chunksize):
##        df=chunk    
##        df['spread']=df['Ask price'] - df['Bid price']
##        if os.path.isfile('/data/EURUSD_1m_est_up.csv'):
##            df.to_csv('EURUSD_1m_est_up.csv',mode='a',header=False,float_format='%.5f')
##        else:
##           df.to_csv('EURUSD_1m_est_up.csv',mode='w',header=True,float_format='%.5f') 
