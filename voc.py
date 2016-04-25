import audioUtilities as au
import numpy as np

# window_size = 2048 and h = window_size//4 = 512
def stretch(sound_array, f, window_size, h):
    """ Stretches the sound by a factor `f` """

    phase  = np.zeros(window_size)
    hanning_window = np.hanning(window_size)
    result = np.zeros( len(sound_array) /f + window_size)

    for i in np.arange(0, len(sound_array)-(window_size+h), h*f):

        # two potentially overlapping subarrays
        a1 = sound_array[int(i): int(i) + window_size]
        a2 = sound_array[int(i + h): int(i) + window_size + h]

        # resynchronize the second array on the first
        s1 =  np.fft.fft(hanning_window * a1)
        s1 = [np.float64(i.real) for i in s1]
        s1 = np.asarray(s1)
        s2 =  np.fft.fft(hanning_window * a2)
        s2 = [np.float64(i.real) for i in s2]
        s2 = np.asarray(s2)
        phase = (phase + np.angle(s2/s1)) % 2*np.pi
        a2_rephased = np.fft.ifft(np.abs(s2)*np.exp(1j*phase))
        a2_rephased = [np.float64(i.real) for i in a2_rephased]

        # add to result
        i2 = int(i/f)
        result[i2 : i2 + window_size] += hanning_window*a2_rephased

    result = ((2**(16-4)) * result/result.max()) # normalize (16bit)

    return result.astype('int16')

ninth = au.readWaveFile("Beethoven.Ninth.wav")
window_size = 2**13
h = 2**11
n = 10
factor = 2**(1.0*n/12.0)
test = stretch(ninth, 1/factor, window_size, h)
# test = stretch(ninth, 1, 2048, 1024)
# slower = stretch(ninth, 0.5, 2048, 512)
# faster = stretch(ninth, 1.5, 2048, 512)
au.writeWaveFile("BeethovenNinth10.wav", test)
# au.writeWaveFile("BeethovenNinthHalf.wav", slower)
# au.writeWaveFile("BeethovenNinthOneAndAHalf.wav", faster)

