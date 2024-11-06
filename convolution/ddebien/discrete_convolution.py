import numpy as np
import matplotlib.pyplot as plt


def convolve(x, h):
    """
    Perform convolution between two sequences x and h.

    Parameters:
    x (array): Input signal (e.g., the signal to be filtered).
    h (array): Impulse response (e.g., filter coefficients).

    Returns:
    y (array): The result of the convolution of x and h.
    """
    # Lengths of the signals
    len_x = len(x)
    len_h = len(h)
    len_y = len_x + len_h - 1  # Length of the convolution result

    # Initialize the output signal with zeros
    y = np.zeros(len_y)

    # Perform the convolution operation
    for n in range(len_y):
        for k in range(len_h):
            if n - k >= 0 and n - k < len_x:
                y[n] += x[n - k] * h[k]

    return y


# Define input signals
x = np.array([1, 2, 3])  # Example input signal
h = np.array([4, 5, 6])  # Example impulse response (e.g., simple filter)

# Perform convolution
y = convolve(x, h)

# Plot the results
plt.figure(figsize=(10, 4))
plt.stem(y, basefmt=" ")
plt.title("Result of Convolution")
plt.xlabel("Sample index")
plt.ylabel("Amplitude")
plt.grid()
plt.show()