import numpy as np
import matplotlib.pyplot as plt

# Original signal parameters
f_signal = 15  # Original signal frequency in Hz
duration = 1    # Duration of the signal in seconds
t_continuous = np.linspace(0, duration, 1000, endpoint=False)  # High-resolution time
signal = np.sin(2 * np.pi * f_signal * t_continuous)  # Original continuous signal

# Sampling rate below the Nyquist rate
fs_low = 20  # Low sampling rate (less than 2 * f_signal)
t_low = np.arange(0, duration, 1/fs_low)  # Low-rate sampled time points
sampled_low = np.sin(2 * np.pi * f_signal * t_low)  # Undersampled signal

# Reconstructed aliased frequency
f_alias = abs(f_signal - fs_low * np.floor((f_signal + fs_low/2) / fs_low))

# Plot the results
plt.figure(figsize=(12, 8))

# Original continuous signal
plt.plot(t_continuous, signal, label="Original Signal (15 Hz)", color='black')

# Undersampled signal
plt.scatter(t_low, sampled_low, color='red', label=f"Samples (Fs={fs_low} Hz)", zorder=5)

# Aliased signal (conceptual)
aliased_signal = np.sin(2 * np.pi * f_alias * t_continuous)
plt.plot(t_continuous, aliased_signal, '--', label=f"Aliased Signal ({f_alias:.1f} Hz)", color='blue')

# Plot settings
plt.title("Aliasing Demonstration")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()