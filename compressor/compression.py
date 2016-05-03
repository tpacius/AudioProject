import numpy as np
import math
import matplotlib.pyplot as plt
import audioUtilities as au

def getMaxAmp_Wave(filename):
    wave = au.readWaveFile(filename)
    maxAmp = max(wave)
    return (maxAmp, wave)

def decibelReduce(value, diff, ratio):
    # if 16 bit rate then max possible amp is 32767
    maxValue  = 32767
    r = abs(diff) / maxValue
    find_decibel = 20 * math.log10(r)
    ratio_apply = (find_decibel / ratio)
    # convert back to amplitude then subtract that original value
    new_amp_r = (10**(ratio_apply / 20))
    new_amp = maxValue * new_amp_r
    if value < 0:
        final = value + new_amp
    else:
        final = value - new_amp
    return final

def compress_wav(filename, threshLimit, ratio):
    (_sourceMax, _sourceWave)  = getMaxAmp_Wave(filename)
    threshold = int(_sourceMax / threshLimit)
    _new = []
    for elem in _sourceWave:
        if abs(elem) > threshold:
            # use decibel reduce function to find new amp add to list
            diff = threshold - elem
            dr = decibelReduce(elem, diff, ratio)
            _new.append(dr)
        else:
            _new.append(elem)
    return _new


test = au.readWaveFile("Bn.wav")
test_compress = compress_wav("Bn.wav", 2, 2)
#
au.displaySignal(test)
au.displaySignal(test_compress)
# au.writeWaveFile("BnNew2.wav", test_compress)


#
