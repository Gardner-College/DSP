import numpy as np
import matplotlib.pyplot as plt

# Original signal parameters
f_signal = 5  # Frequency of the original signal in Hz
duration = 1   # Duration of the signal in seconds
t_continuous = np.linspace(0, duration, 1000, endpoint=False)  # High-resolution time
signal = np.sin(2 * np.pi * f_signal * t_continuous)  # Original signal

# Sampling rates
fs_high = 20  # High sampling rate
fs_low = 8    # Low sampling rate (below Nyquist rate)

# Sampling points
t_high = np.arange(0, duration, 1/fs_high)  # High sampling rate time points
t_low = np.arange(0, duration, 1/fs_low)    # Low sampling rate time points

sampled_high = np.sin(2 * np.pi * f_signal * t_high)  # High-rate sampled signal
sampled_low = np.sin(2 * np.pi * f_signal * t_low)    # Low-rate sampled signal

# Plot the results
plt.figure(figsize=(12, 8))

# Original continuous signal
plt.plot(t_continuous, signal, label="Original Signal (5 Hz)", color='black')

# High-rate sampling
plt.scatter(t_high, sampled_high, color='red', label="Samples (Fs=20 Hz)", zorder=5)

# Low-rate sampling
plt.scatter(t_low, sampled_low, color='blue', label="Samples (Fs=8 Hz)", zorder=5)

# Plot settings
plt.title("Sampling Demonstration")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()