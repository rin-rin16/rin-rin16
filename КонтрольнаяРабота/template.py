def task1(x, y):
    # TODO: первое задание
    x = float(input())
    y = float(input())
    print(x ** 2 + y ** 2)

def task2():
    # TODO: второе задание
    text = str(input())
    lis = list(text)
    c = 0
    for i in range(len(lis)):
        if lis[i].islower():
            c += 1
    print(c)

def task3():
    # TODO: третье задание
    tex = str(input())
    lis = tex.split()
    c = 0
    for i in range(len(lis)):
        if lis[i].endswith('bus'):
            c += 1
    print(c)

def task4(generator):
    # TODO: четвертое задание
    def filt(x):
        if x % 3 == 0:
            return False
        else:
            return True

    lis = filter(filt, generator)
    return lis

def task5(list_of_smth):
    # TODO: 
    print(list_of_smth[6 : len(list_of_smth) - 1 : 2])

def task6(list1, list2, list3, list4):
    # TODO: пятое задание
    list12 = list(set(list1) & set(list2))
    list34 = list(set(list3) & set(list4))
    one = set(list12)
    two = set(list34)
    tw = two - one
    res = list12 + list(tw)
    print(res)

def task7():
    # TODO: ...
    import numpy as np

    np.random.seed(11)
    array = np.random.randint(37, size=(6, 6))
    array = np.delete(array, 3, axis=0)
    array = np.delete(array, 0, axis=1)
    print(np.linalg.det(array))
    return array

def task8(f, min_x, max_x, N, min_y, max_y):
    # TODO: ...
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.misc import derivative

    x = np.linspace(min_x, max_x, N)
    plt.plot(x, f(x), color='red', label='function')
    plt.yscale('log')
    plt.ylim(min_y, max_y)
    plt.grid(True, which='both')
    plt.savefig('function.jpeg')

    def der(x):
        return derivative(f, x)

    plt.plot(x, der(x), label='derivative')
    plt.legend()
    plt.show()

def task9(data, x_array, y_array, threshold):
    # TODO: ...
    import numpy as np
    import matplotlib.pyplot as plt

    x = np.delete(data, 1, 1)
    y = np.delete(data, 0, 1)
    plt.hist(data)
    plt.savefig('histograms_0.png')

def task10(list_of_smth, n):
    # TODO: ...
    listfin = []
    for i in range(len(list_of_smth)):
        if i + n + 1 < len(list_of_smth):
            listprime = list_of_smth[i: i + n + 1: 1]
            for i in range(len(listprime)):
                listprime[i] = listprime[i] ** 2
            listfin.append((sum(listprime) / len(listprime)) ** 0.5)
        else:
            listprime = list_of_smth[i:len(list_of_smth)]
            for i in range(len(listprime)):
                listprime[i] = listprime[i] ** 2
            listfin.append((sum(listprime) / len(listprime)) ** 0.5)
    print(listfin)

def task11(filename="infile.csv"):
    # TODO: ...
    import pandas as pd
    import numpy as np

    df = pd.read_csv('infile.csv')
    xcount = df['x'].isna().sum()
    ycount = df['y'].isna().sum()
    x_errcount = df['x_err'].isna().sum()
    y_errcount = df['y_err'].isna().sum()
    print(x, y, x_errcount, y_errcount)

    df['x_err'].fillna(value=df['x_err'].mean(), inplace=True)

def task12(filename="video-games.csv"):
    # TODO: ...
