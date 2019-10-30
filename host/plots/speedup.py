

import matplotlib.pyplot as plt
from pylab import *

w1 = 17.659420013427734
w2 = 9.688361883163452
w4 = 6.39198112487793
w8 = 3.87300705909729

workers = [1, 2, 4, 8]
speedup = [w1/w1, w1/w2, w1/w4, w1/w8]

plt.plot(workers, speedup, linestyle='--', marker='o', color='b')


plt.legend(loc='upper left')
plt.ylabel("Speed up")
plt.xlabel("Number of workers")
plt.show()
