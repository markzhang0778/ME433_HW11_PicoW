import board
import time
import digitalio
import analogio
from ulab import numpy as np

def make_fft(DAT, SR):
    print(len(DAT))
    N = len(DAT) # length of the signal
    k = np.arange(N) #frequencies
    T = N/SR
    frq = k/T # two sides frequency range
    frq = frq[0:512] # one side frequency range
    Y = np.fft.fft(DAT)# fft computing and normalization
    Y = Y[0][0:512]
    #print(len(Y))
    return [frq, Y, N]

#make an array with 1024 values
#and sum the 3 sine waves at different frequencies
t = np.linspace(0, 10, num=1024)
s1 = 10*np.sin(t * 10)
s2 = 10*np.sin(t * 2)
s3 = 10*np.sin(t * 0.5)
ss = s1 + s2 + s3
ss_sr = 1024/10

[f,y,n] = make_fft(ss, ss_sr)

for i in range(512):
    print('(' +str(np.log10(y[i]))+ ')') # print with plotting format
    time.sleep(.025)
