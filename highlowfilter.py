import numpy as np
import audioUtilities as au

# Example code, computes the coefficients of a low-pass windowed-sinc filter.

# Configuration.
fS = 44100  # Sampling rate.
fL = 4410  # Cutoff frequency.
N = 59  # Filter length, must be odd.

# Compute sinc filter.
h = np.sinc(2 * fL / fS * (np.arange(N) - (N - 1) / 2.))

# Apply window.
h *= np.blackman(N)

# Normalize to get unity gain.
h /= np.sum(h)

# print(h)

# Applying the filter to a signal s can be as simple as writing
# s = np.convolve(s, h)

def lowpassFilter(X, h):
	return np.convolve(X,h)

def highpassFilter(X,h):
	h = - h
	h[(N - 1) / 2] += 1
	return np.convolve(X,h)

test = au.readWaveFile("Beethoven.Ninth.wav")
ret1 = lowpassFilter(test,h)
au.writeWaveFile("LowPassTest.wav",ret1)
ret2 = highpassFilter(test,h)
au.writeWaveFile("HighPassTest.wav",ret2)




