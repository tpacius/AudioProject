import numpy as np
import audioUtilities as au

signal = au.readWaveFile("SteelString.wav")
# print(len(signal))
amp_envelope = au.getEnvelope(signal, 2205, 2205)
print(amp_envelope)
signal = signal[:44100]

# tx = [ 5 , 6, 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 ]
tx = signal
ta = [ 0.5 , 0.7 ]

intermediateWindows = []
window = len(amp_envelope)

def zeroPadLeft(lst,m):
    for j in range(m):
        lst.insert(j, 0)
    return lst

for i in range(0, len(tx) - 1, 2):
    for j in range(len(amp_envelope)):
        intermediateWindows.append(amp_envelope[j] * tx[i])

q = [intermediateWindows[i:i+window] for i  in range(0, len(intermediateWindows), window)]
z = []

for i in range(len(q)):
    if i == 0:
        z.append(q[i])
    else:
        z.append(zeroPadLeft(q[i], i))

for i in range(len(z)):
    if len(z[i]) != len(z[-1]):
        diff = len(z[-1]) - len(z[i])
        for j in range(diff):
            z[i].append(0)

#print([sum(elem) for elem in z])
# print(len(signal))
output = [elem for elem in z]
print(z)
# au.writeWaveFile("SteelReverb.wav", output)

