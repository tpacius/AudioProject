import numpy as np
import audioUtilities as au

signal = au.readWaveFile("SteelString.wav")
amp_envelope = au.getEnvelope(signal, 2205, 2205)

tx = [ 5 , 6, 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 ]
ta = [ 0.5 , 0.7 ]

intermediateTwos = []

def zeroPadLeft(lst,m):
    for j in range(m):
        lst.insert(j, 0)
    return lst

for i in range(0, len(tx) - 1, 2):
    for j in range(len(ta)):
        intermediateTwos.append(ta[j] * tx[i])

q = [intermediateTwos[i:i+2] for i  in range(0, len(intermediateTwos), 2)]
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

print([sum(elem) for elem in z])
