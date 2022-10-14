import pandas as pd
import numpy as np


df = pd.DataFrame({
'ord_no': [70001, np.nan, 70002, 70004, np.nan, 70005, np.nan, 70010, 70003, 70012, np.nan, 70013],
'purch_amt': [150.5, np.nan, 65.26, 110.5, 948.5, np.nan, 5760, 1983.43, np.nan, 250.45, 75.29, 3045.6],
'sale_amt': [10.5, 20.65, np.nan, 11.5, 98.5, np.nan, 57, 19.43, np.nan, 25.45, 75.29, 35.6],
'ord_date': ['2012-10-05', '2012-09-10', np.nan, '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'],
'customer_id': [3002, 3001, 3001, 3003, 3002, 3001, 3001, 3004, 3003, 3002, 3001, 3001],
'salesman_id': [5002, 5003, 5001,np.nan, 5002, 5001, 5001,np.nan, 5003, 5002, 5003,np.nan]})


mask = pd.isnull(df)                                                                                                            #1
df_mean = df[[c for c in df if c not in ['ord_date']] + ['ord_date']]                                                           #1
for column in range(0, df_mean.shape[1] - 1):                                                                                   #1
    df_mean.iloc[:, column].fillna(df_mean.iloc[:, column].mean(), inplace = True)                                              #1
print(df_mean, end ='\n \n \n')                                                                                                 #1


df_mid = df[[c for c in df if c not in ['ord_date']] + ['ord_date']]                                                            #2
for column in range(0, df_mid.shape[1] - 1):                                                                                    #2
    df_mid.iloc[:, column].fillna(df_mid.iloc[:, column].median(), inplace = True)                                              #2
print(df_mid, end ='\n \n \n')                                                                                                  #2


df_often = df[[c for c in df if c not in ['ord_date']] + ['ord_date']]                                                          #3
for column in range(0, df_often.shape[1] - 1):                                                                                  #3
    df_often.iloc[:, column].fillna(df_often.iloc[:, column].value_counts().idxmax(), inplace = True)                           #3
print(df_often, end ='\n \n \n')                                                                                                #3


df_interpol = df[[c for c in df if c not in ['ord_date']] + ['ord_date']]                                                       #4
for column in range(0, df_mean.shape[1] - 1):                                                                                   #4
    df_interpol.interpolate(inplace = True)                                                                                     #4
print(df_interpol, end ='\n \n \n')                                                                                             #4