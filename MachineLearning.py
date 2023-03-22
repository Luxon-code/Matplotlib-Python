import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
speed = [99,86,87,88,86,103,87,94,78,77,85,86]
promedio= np.mean(speed)
mediana = np.median(speed)
moda = stats.mode(speed)
desviacionEstandar = np.std(speed)
varianza = np.var(speed)

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

percentil = np.percentile(ages, 75)


print(promedio)
print(mediana)
print(moda)
print(desviacionEstandar)
print(varianza)
print(percentil)

#Distribucion de datos
x = np.random.uniform(0.0, 5.0, 100000)

plt.hist(x, 100)
plt.show()

#distribucion normal de datos
l = np.random.normal(5.0, 1.0, 100000)

plt.hist(l, 100)
plt.show()

#Diagrama de dispercion
p = np.random.normal(5.0, 1.0, 1000)
y = np.random.normal(10.0, 2.0, 1000)

plt.scatter(p, y)
plt.show()
