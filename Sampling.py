# ============================================================
# Project: Sampling Techniques in Digital Communication
# Author : Manidipa Sarkar
#
# Description:
# This program demonstrates three fundamental sampling techniques:
# 1. Natural Sampling
# 2. Flat-top Sampling
# 3. Sample-and-Hold 
#
# A continuous-time sine wave is generated and sampled at a fixed
# sampling frequency. The output compares the original analog signal
# with each sampling method to illustrate their characteristics.
#
# Libraries Used:
#   - NumPy      : Numerical computations
#   - Matplotlib : Signal visualization
#
# Applications:
#   - Digital Communication
#   - Analog-to-Digital Conversion (ADC)
#   - Digital Signal Processing (DSP)
#   - Signals and Systems Laboratory
# ============================================================
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. Generate Continuous-Time Sine Wave
# ==========================================
fs_analog = 1000                 # High-resolution sampling frequency
duration = 1                     # Signal duration (seconds)
t = np.linspace(0, duration, fs_analog, endpoint=False)

f = 10                            # Signal frequency (Hz)
signal = np.sin(2 * np.pi * f * t)

# ==========================================
# 2. Sampling Parameters
# ==========================================
fs_sample = 50                   # Sampling frequency (Hz)
step = fs_analog // fs_sample    # Samples between two sampling instants

sample_times = t[::step]
sample_values = signal[::step]

pulse_width = step // 5          # Width of sampling pulse

# ==========================================
# 3. Natural Sampling
# ==========================================
natural = np.zeros_like(signal)

for i in range(0, len(signal), step):
    end = min(i + pulse_width, len(signal))
    # Pass the original waveform only during the pulse width
    natural[i:end] = signal[i:end]

# ==========================================
# 4. Flat-top Sampling
# ==========================================
flat_top = np.zeros_like(signal)

for i in range(0, len(signal), step):
    end = min(i + pulse_width, len(signal))
    # Hold sampled value only during pulse width
    flat_top[i:end] = signal[i]

# ==========================================
# 5. Sample-and-Hold (Zero-Order Hold)
# ==========================================
sample_hold = np.zeros_like(signal)

for i in range(0, len(signal), step):
    end = min(i + step, len(signal))
    # Hold sampled value until next sampling instant
    sample_hold[i:end] = signal[i]

# ==========================================
# Plot 1 : Natural Sampling
# ==========================================
plt.figure(figsize=(10,4))

plt.plot(t, signal, color='black', linewidth=2,
         label='Analog Signal')
plt.plot(t, natural, color='blue', linewidth=2,
         label='Natural Sampling')

plt.title('Natural Sampling')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.xlim(0, 1)
plt.ylim(-1.2, 1.2)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# ==========================================
# Plot 2 : Flat-top Sampling
# ==========================================
plt.figure(figsize=(10,4))

plt.plot(t, signal, color='black', linewidth=2,
         label='Analog Signal')
plt.plot(t, flat_top, color='blue', linewidth=2,
         label='Flat-top Sampling')

plt.title('Flat-top Sampling')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.xlim(0, 1)
plt.ylim(-1.2, 1.2)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# ==========================================
# Plot 3 : Sample and Hold
# ==========================================
plt.figure(figsize=(10,4))

plt.plot(t, signal, color='black', linewidth=2,
         label='Analog Signal')
plt.plot(t, sample_hold, color='blue', linewidth=2,
         label='Sample and Hold')

plt.title('Sample and Hold ')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.xlim(0, 1)
plt.ylim(-1.2, 1.2)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

plt.show()