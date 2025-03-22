import numpy as np
import matplotlib.pyplot as plt
from BiomechTools import low_pass, add_padding

# Read Pezzack
data = np.genfromtxt('D:/Python Code/Butterworth_Endpoint_Correction/Data Files/pezzack.csv', delimiter=',', skip_header=1)
x = data[:, 0]
y = data[:, 1]

dt = x[1] - x[0]

sm_y = low_pass(y, 1/dt, 4.0)
plt.plot(y, 'b',color = 'b', label='Original padded 20 pts')
plt.plot(sm_y, 'b',color = 'r', label='Smoothed padded 20 pts')
plt.legend(loc='best')
plt.grid(True)
plt.show()