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
print(deltasq.loc[1], end='\n \n \n')                                                                                       #5

survage = titanic.groupby(['age']).agg({'survived': "mean"})                                                                #6
survage.plot()                                                                                                              #6
plt.show()                                                                                                                  #6

titcount = titanic                                                                                                          #7
titcount['count'] = 1                                                                                                       #7
survhist = titcount.groupby(['age', 'sex']).agg({'survived': "mean", 'count': 'count'}).reset_index()                       #7
survhist['countsurv'] = survhist['survived']*survhist['count']                                                              #7
survhistmale = survhist[survhist['sex'] == 'male']                                                                          #7
survhistfem = survhist[survhist['sex'] == 'female']                                                                         #7
malecum = survhistmale.cumsum()                                                                                             #7
femcum = survhistfem.cumsum()                                                                                               #7
survhistmale['cumulative'] = malecum['countsurv']                                                                           #7
survhistfem['cumulative'] = femcum['countsurv']                                                                             #7
survhistmale['fins'] = survhistmale['cumulative'].apply(lambda x: x/93)                                                     #7
survhistfem['fins'] = survhistfem['cumulative'].apply(lambda x: x/93)                                                       #7
survhistmale.reset_index()                                                                                                  #7
survhistfem.reset_index()                                                                                                   #7
malehist = survhistmale[['age', 'fins']].copy()                                                                             #7
femhist = survhistfem[['age', 'fins']].copy()                                                                               #7
fig, axs = plt.subplots(2)                                                                                                  #7
malehist.plot(x='age', y='fins', ax=axs[0], title= 'male', label='Fraction of survivals below this age')                    #7
femhist.plot(x='age', y='fins', ax=axs[1], title= 'female', label='Fraction of survivals below this age')                   #7
plt.legend()                                                                                                                #7
plt.show()                                                                                                                  #7

print(titanic['fare'].sum(), end='\n \n \n')                                                                                #8

#9  Здесь нет стобца с именем. Напишу код, представив, что он есть:                                                         #9
#   kates = titanic[(titanic['name'] == 'Kate') or (titanic['name'] == 'Katerina') or (titanic['name'] == 'Ekaterina')]     #9

#10 Аналогичная ситуация:                                                                                                  #10
#   freqnames = titanic.groupby(['sex', 'names']).agg({'count' = ('names': 'count')})                                      #10
#   malenames = freqnames[freqnames['sex'] = 'male']                                                                       #10
#   femnames = freqnames[freqnames['sex'] = 'female']                                                                      #10
#   malemostfreq = malenames[malenames['count'] in malenames.nlargest(5, 'count')]                                         #10
#   femmostfreq = femnames[femnames['count'] in femnames.nlargest(5, 'count')]                                             #10
#   print(malemostfreq)                                                                                                    #10
#   print(femmostfreq)                                                                                                     #10