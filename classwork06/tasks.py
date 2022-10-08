import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

f = pd.read_csv("telecom_churn.csv")

print(f['Total day calls'].mean(), end = '\n \n')                                                                                                #3

print(f[f["State"] == "AL"].groupby(["State"]).agg({"Total day calls": "mean"}), end = '\n \n')                                                  #4

daycalls = f.groupby(["State"]).agg({"Total day calls": "mean"})                                                                                 #5

m = f.groupby(["State"]).agg({"Total day calls": "mean"}).mean()[0]                                                                              #6
daycalls = daycalls[daycalls["Total day calls"] > m]                                                                                             #6

newf = f.groupby(["State"]).agg({"Total day calls": "mean", "Total eve calls": "mean"})                                                          #7

moref = newf                                                                                                                                     #8
evecalls = f.groupby(["State"]).agg({"Total eve calls": "mean"})                                                                                 #8
moref.loc[moref["Total day calls"] > moref["Total eve calls"], 'day > eve'] = 'True'                                                             #8
moref.loc[moref["Total day calls"] <= moref["Total eve calls"], 'day > eve'] = 'False'                                                           #8

international = f[f["International plan"] == "Yes"]                                                                                              #9
voice = f[f["Voice mail plan"] == "Yes"]                                                                                                         #9
print(voice.shape[0]/f.shape[0])                                                                                                                 #9
print(international.shape[0]/f.shape[0], end = '\n \n')                                                                                          #9

print(f['Area code'].nunique())                                                                                                                 #10

servcalls = f.groupby(['Customer service calls']).count().iloc[:, 0:1].rename(columns = {"State" : "Number of clients"})                        #11
print(servcalls, end = '\n \n')                                                                                                                 #11

churnrate = f.groupby(['Customer service calls']).agg({"Churn": "mean"})                                                                        #12
print(churnrate, end ='\n \n')                                                                                                                  #12
churnrate = churnrate.reset_index()                                                                                                             #12
churnrate.plot(x="Customer service calls", y = 'Churn', kind = 'line')                                                                          #12
plt.show()                                                                                                                                      #12

print(f['Total intl minutes'].mean())                                                                                                           #13

tablraw = f.iloc[:, 6:15].mean()                                                                                                                #14
data = {'days' : tablraw.iloc[0:3].tolist(),                                                                                                    #14
        'eves' : tablraw.iloc[3:6].tolist(),                                                                                                    #14
        'nigts' : tablraw.iloc[6:].tolist()}                                                                                                    #14
tabl = pd.DataFrame(data, index = ['minutes',                                                                                                   #14
                                   'number',                                                                                                    #14
                                   'charge'])                                                                                                   #14
print(tabl)                                                                                                                                     #14
#14: Можно было переименовать строчки в tableraw, сгруппировать по ним и получить тоже самое. Но вроде \
# моё решение тоже не особо затратное с точки зрения ресурсов

comparas = f.groupby(['Churn']).agg({'Total day charge': 'mean'})                                                                               #15
print(comparas)                                                                                                                                 #15

sorti = f.groupby(['State']).agg({'Total day charge': 'mean'}).sort_values(by = 'Total day charge', ascending = False)                          #16
print(sorti)                                                                                                                                    #16

means = f.groupby(["Area code"]).mean(numeric_only=True)                                                                                        #17
print(means)                                                                                                                                    #17

print(f.iloc[100:105:2, ::19])                                                                                                                  #18

numbers = pd.DataFrame({'A': [13, 2, 7, 9, 0], 'B': [6, 5, 8, 11, 10]})                                                                         #19
numbers['C'] = numbers[['A', 'B']].apply(lambda x: sum([t**2 for t in x]), axis = 1)                                                            #19

numbers['D'] = numbers[['A', 'B', 'C']].apply(lambda x: x.mean(), axis = 1)                                                                     #20
print(numbers)                                                                                                                                  #20