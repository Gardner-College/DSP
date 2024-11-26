import numpy as np
import matplotlib.pyplot as plt

# Signal parameters
f_signal = 5  # Frequency of the original signal in Hz
t = np.linspace(0, 1, 1000, endpoint=False)  # High-resolution time vector
signal = np.sin(2 * np.pi * f_signal * t)  # Original continuous-time signal

# Sampling rates
fs_high = 20  # High sampling rate (well above Nyquist rate)
fs_nyquist = 10  # Nyquist rate (2 * f_signal)
fs_low = 6  # Below Nyquist rate (aliased)

# Generate sampled signals
t_high = np.arange(0, 1, 1/fs_high)  # Time vector for high sampling rate
t_nyquist = np.arange(0, 1, 1/fs_nyquist)  # Time vector for Nyquist rate
t_low = np.arange(0, 1, 1/fs_low)  # Time vector for low sampling rate

sampled_high = np.sin(2 * np.pi * f_signal * t_high)
sampled_nyquist = np.sin(2 * np.pi * f_signal * t_nyquist)
sampled_low = np.sin(2 * np.pi * f_signal * t_low)

# Plot the results
plt.figure(figsize=(15, 10))

# Original signal
plt.subplot(3, 1, 1)
plt.plot(t, signal, label="Original Signal (5 Hz)")
plt.scatter(t_high, sampled_high, color='red', label="Samples (Fs=20 Hz)")
plt.title("Sampling above Nyquist Rate")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()

# Nyquist sampling
plt.subplot(3, 1, 2)
plt.plot(t, signal, label="Original Signal (5 Hz)")
plt.scatter(t_nyquist, sampled_nyquist, color='orange', label="Samples (Fs=10 Hz)")
plt.title("Sampling at Nyquist Rate")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()

# Below Nyquist sampling (Aliasing)
plt.subplot(3, 1, 3)
plt.plot(t, signal, label="Original Signal (5 Hz)")
plt.scatter(t_low, sampled_low, color='blue', label="Samples (Fs=6 Hz)")
plt.title("Sampling below Nyquist Rate (Aliasing)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()

plt.tight_layout()
plt.show()