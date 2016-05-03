import numpy as np
import audioUtilities as au

def window_traverse(filename):
    X = au.readWaveFile(filename)
    window = 2250
    test = X[:window]
    return test

thing = window_traverse("SteelString.wav")
c = np.fft.fft(thing)

for elem in c:
    print(elem)
