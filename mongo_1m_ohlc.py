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

def mdb_1m_ohlc(chunksize, period, file_in, file_out):
    start_time = time.time()
    for chunk in pd.read_csv(file_in, chunksize=chunksize):
        fxdata=chunk
        fxdata.Datetime=(pd.to_datetime(fxdata.Timestamp, format='%Y%m%d %H:%M:%S:%f'))
        fxdata.set_index([fxdata.Datetime],inplace=True)

        #fxdata_ru=eufxdatarusd.resample('1min', how={'bid_price': 'ohlc', 'bid_vol' : 'sum','spread':'mean'})
        fxdata_ru               =fxdata.resample(period, how={'Ask price': 'ohlc','Bid price': 'ohlc'})
        
        fxdata_ru['Bid volume'] =fxdata.resample(period, how={'Bid volume' : 'sum'})
        fxdata_ru['Ask volume'] =fxdata.resample(period, how={'Ask volume' : 'sum'})
        fxdata_ru['spread']     =fxdata.resample(period, how={'spread' : 'mean'})
        fxdata_ru.columns       =['Ask open','Ask high','Ask low','Ask close',
                                  'Bid open','Bid high','Bid low','Bid close',
                                  'Bid volume','Ask volume','spread']
        ##
        ##
        fxdata_ru['Ask volume']     =fxdata_ru['Ask volume'].fillna(0)
        fxdata_ru['Bid volume']     =fxdata_ru['Bid volume'].fillna(0)
        fxdata_ru['spread']         =fxdata_ru['spread'].fillna(0)
        fxdata_ru['Ask close']      =fxdata_ru['Ask close'].fillna(method='pad')
        fxdata_ru['Ask low']        =fxdata_ru['Ask low'].fillna(fxdata_ru['Ask close'])
        fxdata_ru['Ask high']       =fxdata_ru['Ask high'].fillna(fxdata_ru['Ask close'])
        fxdata_ru['Ask open']       =fxdata_ru['Ask open'].fillna(fxdata_ru['Ask close'])
        fxdata_ru['Bid close']      =fxdata_ru['Bid close'].fillna(method='pad')
        fxdata_ru['Bid low']        =fxdata_ru['Bid low'].fillna(fxdata_ru['Bid close'])
        fxdata_ru['Bid high']       =fxdata_ru['Bid high'].fillna(fxdata_ru['Bid close'])
        fxdata_ru['Bid open']       =fxdata_ru['Bid open'].fillna(fxdata_ru['Bid close'])
        fxdata_ru['Adj Close']      =fxdata_ru['Bid close']
        fxdata_ru['returns']        =fxdata_ru["Bid close"].pct_change()
        #fxdata_ru                   =fxdata_ru.iterrows()

        #print (fxdata_ru.head())
        #print (fxdata_ru.tail())
            
        if os.path.isfile(file_out):
            fxdata_ru.to_csv(file_out,mode='a',header=False,index=True,float_format='%.5f')
        else:
            fxdata_ru.to_csv(file_out,mode='w',header=True,index=True,float_format='%.5f') 

    print("--- %s Add seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    chunksize = 500000
    period='B'
    symbol='EURUSD'
    file_in     =   symbol +'_2003-05-05_09122015_est_up.csv'
    file_out    =   symbol +'_2003-05-05_09122015_B_ohlc_est_up.csv'
    mdb_1m_ohlc(chunksize, period, file_in, file_out)
