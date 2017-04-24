#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

def wavepacket(x, k, sigma):
    """This function creates a wavepacket on the interval defined by x with
    wavevector k and standard deviation sigma."""
    return np.sin(k*x) *  np.exp(-(x**2)/(2*sigma**2))


def main():
    """This function sould call noisy_packet() to get a Gaussian wave
    packet, call clean_data() to apply a low pass filter to the data and
    finally plot the result."""
    x = np.arange(-np.pi, np.pi, 0.01)
    y_values = noisy_packet(x, 5, 1, 0.2)
    data = clean_data(x, y_values)
    x = np.delete(x, 0)
    plt.plot(x, data)
    plt.show()

def noisy_packet(x_values, k, sigma, noise_amplitude):
    """This function returns a noisy Gaussian wavepacket with wave
    vector k, standard deviation sigma and Gaussian noise of standard
    deviation noise_amplitude."""
    clean_y = wavepacket(x_values, k, sigma)
    noisy_y = clean_y + noise_amplitude*np.random.randn(len(x_values))
    return noisy_y

def clean_data(x_values,y_values):
    """This function should take a set of y_values, perform the Fourier
    transform on it, filter out the high frequency noise, transform the
    signal back into real space, and return it."""

    y_sorted = np.fft.rfft(y_values)
    clean_frequencies = np.fft.rfftfreq(len(x_values), 0.01)
    for i in range(0, len(clean_frequencies)):
	if clean_frequencies[i] > 4 :
	    y_sorted[i] = 0
    y_clean = np.fft.irfft(y_sorted)
    return y_clean

main()  # calls your main function
