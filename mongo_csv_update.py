import csv
import pandas as pd

df=pd.read_csv('EURUSD_50_est.csv')

df.set_index(['Timestamp'],inplace=True)

#print(df.columns)

df['spread']=df['Ask price'] - df['Bid price']

print(df)


