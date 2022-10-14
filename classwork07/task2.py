import pandas as pd
import matplotlib.pyplot as plt

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

bigger5 = diamonds[(diamonds.x > 5) & (diamonds.y > 5) & (diamonds.z > 5)]                                                      #1
print(bigger5, end = '\n \n \n')                                                                                                #1

numonly = diamonds[[c for c in diamonds if diamonds.dtypes.loc[c] != 'object']]                                                 #2
print(numonly, end ='\n \n \n')                                                                                                 #2

print(numonly.mean(), end ='\n \n \n')                                                                                          #3

cutprice = diamonds.groupby(['cut']).agg({'price': "mean"})                                                                     #4
cutprice.plot()                                                                                                                 #4
plt.legend(["average price"])                                                                                                   #4
plt.show()                                                                                                                      #4

diamonds['carat'].hist(bins= 100)                                                                                               #5
plt.show()                                                                                                                      #5

print(diamonds.isnull().sum().sum(), end = '\n \n \n')                                                                          #6

nonnull = diamonds.dropna(axis= 0, how= 'any', inplace= False)                                                                  #7
print(nonnull, end= '\n \n \n')                                                                                                 #7

print(diamonds.info(), end = '\n \n \n')                                                                                        #8

print(diamonds.sample(20))                                                                                                      #9