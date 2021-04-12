import matplotlib.pyplot as plt
import numpy as np
from scipy import signal, optimize

def gaussian(x, a, b, std):
  return a*np.exp((-(x-b)**2)/(2*std**2))

arr = np.loadtxt("2015209_2015213_H217O.dat")
arr = arr.reshape(77,228,3)
sum = np.mean(arr[:,:,2], axis=0)

plt.rcParams["figure.figsize"] = (18,10)
plt.plot(arr[0,:,0], sum, label='original (average)') 

#average of the data /77; stack is without /77 
#x-axis: frequency y-axis: stack of intensity

smooth_data = signal.medfilt(sum,3) #moving medium 
max_value = np.max(smooth_data)
print(max_value)
plt.plot(arr[0,:,0], smooth_data, label='channel smoothing')

#curve fit
popt, pcov = optimize.curve_fit(gaussian, arr[0,:,0], smooth_data, p0=[13, 552020, 2])
print(popt)
plt.plot(arr[0,:,0], gaussian(arr[0,:,0], *popt), 'g--', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))

plt.legend()
plt.show()
