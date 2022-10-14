import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

titanic = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv")

fig, axs = plt.subplots(2)                                                                                                  #1
titanic['class'].hist(ax=axs[0])                                                                                            #1
titanic['age'].hist(ax=axs[1], bins= 70)                                                                                    #1
plt.show()                                                                                                                  #1

ageg = titanic.groupby(['class']).agg({'age': "median"})                                                                    #2
agesexg = titanic.groupby(['class', 'sex']).agg({'age': "median"})                                                          #2
print(agesexg, end = '\n \n \n')                                                                                            #2

agesexgsurv = titanic.groupby(['class', 'sex']).agg({'age': "median", 'survived': 'mean'})                                  #3
print(agesexgsurv, end= '\n \n \n')                                                                                         #3

avgagesurv = titanic.groupby(['sex']).agg({'survived': "mean"})                                                             #4
print(avgagesurv, end= '\n \n \n')                                                                                          #4

deltasq = titanic.groupby(['survived']).agg({'age': "std"})                                                                 #5
print(deltasq.loc[1])                                                                                                       #5

survage = titanic.groupby(['age']).agg({'survived': "mean"})                                                                #6
survage.plot()                                                                                                              #6
plt.show()                                                                                                                  #6

# Недоделанный пункт 7:

titcount = titanic
titcount['count'] = 1
survhist = titcount.groupby(['age', 'sex']).agg({'survived': "mean", 'count': 'count'}).reset_index()
survhistmale = survhist[survhist['sex'] == 'male']
print(survhistmale)
survhistfem = survhist[survhist['sex'] == 'female']
print(survhistfem)
malecum = survhistmale.cumsum()
print(malecum)
survhistmale['cumulative'] = malecum['count']
print(survhistmale)
survhistmale['fin'] = survhistmale['cumulative'].apply(lambda x: x/453)
print(survhistmale)
malehist = survhistmale['age', 'fin'].copy()
print(malehist)

# Вроде можно не доделывать. Здесь короче просто создаёшь count с учётом процента survived, потом по нему
# делаешь cumulative sum и получаешь данные для графика. Пункты 8-10 очень простые там всё очевидно