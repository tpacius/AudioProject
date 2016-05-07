import numpy as np
import audioUtilities as au

# 5/500 = x/44100, x = 441
# 30/500 = x/44100, x = 2646

low = 441
high = 2646

def lowpass_ifft(X, low=low, sampleRate=44100):
	m = np.size(X)
	spectrum = np.fft.rfft(X, n=m).real
	low_point = int(low/sampleRate * m/2)
	#The size of m alone will always cause an index out of bounds error but
	#this is most likely the variable that can be altered to change the output
	#wave
	filtered = [spectrum[i] if i >= low_point else 0 for i in range(m//2)]
	newSignal = np.fft.irfft(filtered, n=m)
	return newSignal

def highpass_ifft(X, high=high, sampleRate=44100):
	m = np.size(X)
	spectrum = np.fft.rfft(X, n=m).real
	high_point = int(high/sampleRate * m/2)
	#The size of m alone will always cause an index out of bounds error but
	#this is most likely the variable that can be altered to change the output
	#wave
	filtered = [spectrum[i] if i <= high_point else 0 for i in range(m//2)]
	newSignal = np.fft.irfft(filtered, n=m)
	return newSignal

def bandpass_ifft(X, low=low, high=high, sampleRate=44100):
	m = np.size(X)
	spectrum = np.fft.rfft(X, n=m).real
	low_point = int(low/sampleRate * m//2)
	high_point = int(high/sampleRate * m//2)
	filtered = [spectrum[i] if i >= low_point and i <= high_point else 0.0 for i in range(m)]
	newSignal = np.fft.irfft(filtered, n=m)
	return newSignal

def displaySignals(wave):
	#Original Signal
	au.displaySignal(wave)
	#Low Pass
	au.displaySignal(lowpass_ifft(wave))
	#High Pass
	au.displaySignal(lowpass_ifft(wave))
	#Band Pass
	au.displaySignal(bandpass_ifft(wave))

def writeAudioFilters(wave, filename):
	au.writeWaveFile(filename + "Low.wav",lowpass_ifft(wave))
	au.writeWaveFile(filename + "High.wav",highpass_ifft(wave))
	au.writeWaveFile(filename + "BandPass.wav", bandpass_ifft(wave))

def main(file, displaySignal=False):
	filename = file.split(".wav")[0]
	wave = au.readWaveFile(file)
	if(displaySignal):
		displaySignals(wave)
	writeAudioFilters(wave, filename)

# main("BassGuitar.wav")
main("Bach.wav")
# main('Bach.wav', displaySignal=True)

