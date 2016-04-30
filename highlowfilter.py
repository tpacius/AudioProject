import numpy as np
import audioUtilities as au

#Reverb, EQing, Compression, np.fft, np.ifft

# Configuration.
fS = 44100  # Sampling rate.
fL = 4410  # Cutoff frequency.
N = 59  # Filter length, must be odd.

#Takes in a wav array and a window type
def lowpassFilter(X, windowType="Blackman"):
	sincFilter = np.sinc(2 * fL / fS * (np.arange(N) - (N - 1) / 2.))

	if windowType == "Blackman":
		sincFilter *= np.blackman(N)
	if windowType == "Hanning":
		sincFilter *= np.hanning(N)

	sincFilter /= np.sum(sincFilter)

	return np.convolve(X,sincFilter)

#Takes in a wav array and a window type
def highpassFilter(X,windowType="Blackman"):
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
def bandPassFilter(X, windowType="Blackman"):
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
def bandRejectFilter(X, windowType="Blackman"):
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

def displaySignals(wave):
	#Original Signal
	au.displaySignal(wave)
	#Low Pass
	au.displaySignal(lowpassFilter(wave))
	#High Pass
	au.displaySignal(lowpassFilter(wave))
	#Band Pass
	au.displaySignal(bandPassFilter(wave))
	#Band Reject
	au.displaySignal(bandRejectFilter(wave))

def writeAudioFilters(wave, filename):
	au.writeWaveFile(filename + "Low.wav",lowpassFilter(wave))
	au.writeWaveFile(filename + "High.wav",highpassFilter(wave))
	au.writeWaveFile(filename + "BandPass.wav", bandPassFilter(wave))
	au.writeWaveFile(filename + "BandReject.wav", bandRejectFilter(wave))


def main(file, displaySignal=False):
	filename = file.split(".wav")[0]
	wave = au.readWaveFile(file)
	if(displaySignal):
		displaySignals(wave)
	writeAudioFilters(wave, filename)

# def realFFT(X):
#     return [2.0 * np.absolute(x)/len(X) for x in np.fft.rfft(X)]

# signal = realFFT(au.readWaveFile("BassGuitar.wav"))
# print(signal)

# signal = au.readWaveFile("BassGuitar.wav")#[0:50]
# # print(signal)
# signal = np.fft.rfft(signal)
# # signal = np.fft.irfft(signal)
# print(signal.real)

#Unit Tests
# main("Beethoven.Ninth.wav")
# main("BluesGuitar.wav")
# main("Clarinet01_01.wav")
# main("BassGuitar.wav")
# main("Genesis01.wav")
# main("BitesDust.wav")

