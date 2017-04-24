#!/usr/bin/python

#The following statements are used to import numpy and matplotlib.
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as int

# TODO fill in this function
def integrate(y, dx):
    return np.sum(y) * dx

# TODO write code here to setup arrays x and y = sin(x) and then plot them.
# After this is done implement your integrate function above integrate y

def plot_sine():
    x = np.arange(0, np.pi, 0.01)
    y = np.sin(x)
    z = np.cos(x)
    plt.plot(x, y)
    plt.plot(x, z)
    plt.show()
    print(integrate(y, 0.01))
    f = lambda w: np.sin(w)
    print(int.quad(f,0,np.pi))


plot_sine()
