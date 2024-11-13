import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve

# Define the input signals
x = np.array([71, 72, 73])  # Example input signal
h = np.array([74, 75, 76])  # Example impulse response

# Perform convolution using scipy
y = convolve(x, h, mode='full')

# Plot the results
plt.figure(figsize=(10, 4))
plt.stem(y, basefmt=" ")
plt.title("Result of Convolution using scipy.signal.convolve")
plt.xlabel("Sample index")
plt.ylabel("Amplitude")
plt.grid()
plt.show()
