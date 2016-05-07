import numpy as np
import audioUtilities as au

# SR = 44100
# maxAmp = 2**15 -1

# def exponentialDecay(i,h):
#     return 2**(-i/(SR*h)) 

# amps = [i/SR for i in range(SR)], [exponentialDecay(i,0.6) for i in range(SR)][1] 

# bach = au.readWaveFile("Bach.wav")

# def reverb(amps, X):
# 	for i in range(len(amps)-1,len(X)):
# 		for j in range(len(amps)):
# 			out[i] += amps[j]*X[i-j]
# 	return out

# print(reverb(amps,bach))

signal = au.readWaveFile("BassGuitar.wav")
impulse = au.readWaveFile("ConcertHall.wav")

# print(len(impulse), len(signal))

# convolved = np.convolve(signal,impulse)
# print(convolved[0:100])

au.writeWaveFile("BassConcert.wav", np.convolve(signal,impulse,'valid'))

