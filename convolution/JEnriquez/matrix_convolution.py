import numpy as np
import matplotlib.pyplot as plt


def convolve_via_matrix(x, h):
    """
    Simulate convolution using a matrix approach.

    Parameters:
    x (array): Input signal.
    h (array): Impulse response.

    Returns:
    y (array): Convolution result of x and h.
    """
    len_x = len(x)
    len_h = len(h)
    len_y = len_x + len_h - 1  # Length of the convolution result

    # Create an empty matrix to hold shifted versions of x
    X_matrix = np.zeros((len_h, len_y))

    # Populate the matrix with shifted copies of x
    for i in range(len_h):
        X_matrix[i, i:i + len_x] = x

    # Flip the impulse response (h) to perform convolution
    h_flipped = h[::-1]

    # Multiply and sum across rows to get the convolution result
    y = X_matrix.T @ h_flipped  # Equivalent to summing product of rows with h

    return y


# Define the input signals
x = np.array([1, 2, 3])  # Example input signal
h = np.array([4, 5, 6])  # Example impulse response

# Perform convolution
y = convolve_via_matrix(x, h)

# Plot the results
plt.figure(figsize=(10, 4))
plt.stem(y, basefmt=" ")
plt.title("Result of Convolution (Matrix Method)")
plt.xlabel("Sample index")
plt.ylabel("Amplitude")
plt.grid()
plt.show()