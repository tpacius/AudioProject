import numpy as np
import audioUtilities as au

# Configuration.
fS = 44100  # Sampling rate.
fL = 4410  # Cutoff frequency.
N = 59  # Filter length, must be odd.

#Takes in a wav array and a window type
def lowpassFilter(X, windowType):
	sincFilter = np.sinc(2 * fL / fS * (np.arange(N) - (N - 1) / 2.))

	if windowType == "Blackman":
		sincFilter *= np.blackman(N)
	if windowType == "Hanning":
		sincFilter *= np.hanning(N)

	sincFilter /= np.sum(sincFilter)

	return np.convolve(X,sincFilter)

#Takes in a wav array and a window type
def highpassFilter(X,windowType):
	sincFilter = np.sinc(2 * fL / fS * (np.arange(N) - (N - 1) / 2.))

	if windowType == "Blackman":
		sincFilter *= np.blackman(N)
	if windowType == "Hanning":
		sincFilter *= np.hanning(N)

	sincFilter /= np.sum(sincFilter)

	#spectral inversion from low pass filter
	sincFilter = -sincFilter
	sincFilter[(N-1) / 2] += 1

	return np.convolve(X,sincFilter)

#Takes in a wav array and a window type
def bandPassFilter(X, windowType):
	low = np.sinc(2 * fL / fS * (np.arange(N) - (N - 1) / 2.))

	if windowType == "Blackman":
		low *= np.blackman(N)
	if windowType == "Hanning":
		low *= np.hanning(N)

	low /= np.sum(low)
	high = -low
	high[(N-1)/2] += 1

	bandPass = np.convolve(low, high)
	return np.convolve(X, bandPass)

#Takes in a wav array and a window type
def bandRejectFilter(X, windowType):
	low = np.sinc(2 * fL / fS * (np.arange(N) - (N - 1) / 2.))

	if windowType == "Blackman":
		low *= np.blackman(N)
	if windowType == "Hanning":
		low *= np.hanning(N)

	low /= np.sum(low)
	high = -low
	high[(N-1)/2] += 1

	bandReject =  low + high
	return np.convolve(X, bandReject)


#Unit Testing
test1 = au.readWaveFile("Beethoven.Ninth.wav")
test2 = au.readWaveFile("BluesGuitar.wav")
test3 = au.readWaveFile("Clarinet01_01.wav")
test4 = au.readWaveFile("BassGuitar.wav")
test5 = au.readWaveFile("Beethoven.Sixth.wav")

#Blackman window
ret1 = lowpassFilter(test,"Blackman")
au.writeWaveFile("LowPassTest.wav",ret1)
ret2 = highpassFilter(test, "Blackman")
au.writeWaveFile("HighPassTest.wav",ret2)
ret3 = bandPassFilter(test, "Blackman")
au.writeWaveFile("BandPassFilterTest.wav",ret3)
ret4 = bandRejectFilter(test, "Blackman")
au.writeWaveFile("BandRejectFilterTest.wav",ret4)

#Hanning window
ret1 = lowpassFilter(test,"Hanning")
au.writeWaveFile("LowPassTestHanning.wav",ret1)
ret2 = highpassFilter(test, "Hanning")
au.writeWaveFile("HighPassTestHanning.wav",ret2)
ret3 = bandPassFilter(test, "Hanning")
au.writeWaveFile("BandPassFilterTestHanning.wav",ret3)
ret4 = bandRejectFilter(test, "Hanning")
au.writeWaveFile("BandRejectFilterTestHanning.wav",ret4)





