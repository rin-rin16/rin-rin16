import numpy as np
import matplotlib
from matplotlib import pyplot as plt

matplotlib.rcParams.update(matplotlib.rcParamsDefault)


def get_numbers(student):
    return student, (student + 4) % 5 + 3, student % 2 * 10 + 12, (student % 5 * 3 + 7) * 3


def fake_data_generator(seed, vmin=0, vmax=10, size=100):
    import numpy as np
    np.random.seed(seed)
    data = np.random.randint(vmin, vmax, size=20)
    mean = data.mean()
    std = data.std()
    noise = np.random.normal(loc=mean, scale=std ** .5, size=size)
    fake_x = np.array([-5 + i * 20 / size for i in range(size)])

    linear = lambda x, k=(.5 - np.random.rand()) * 15, b=np.random.rand() * 10: k * x + b
    linear_data = linear(fake_x)
    fake_y = linear_data + noise
    return fake_x, fake_y

data = fake_data_generator(get_numbers(11))

plt.grid(b=True, which='major', axis='both', alpha=1)
meanx = sum(data[0])/len(data[0])
meany = sum(data[1])/len(data[1])
num1 = 0
for i in range(len(data[0])):
    num1 += data[0][i]*data[1][i]
num2 = sum(data[1])*sum(data[0])
num3 = 0
for i in range(len(data[0])):
    num3 += data[0][i]*data[0][i]
num4 = (sum(data[0]))**2
a = (len(data[0])*num1 - num2)/(len(data[0])*num3 - num4)
b = (sum(data[1])-a*sum(data[0]))/len(data[0])
x = np.linspace(-5, 15, 1000)
print(a, b)
y = a*x + b
plt.plot(x, y, color = 'black', label = 'fit')
np.polyfit(data[0], data[1], deg = 1)
print(np.polyfit(data[0], data[1], deg = 10))
plt.xlabel(r"$\xi, cm$")
plt.ylabel(r"$\rho, mm^{-3}$")
plt.legend(loc = "lower right")
plt.show()


