
#IIR filter 
import numpy as np 
import matplotlib.pyplot as plt
from scipy import signal
fs = 1000 # Sampling frequency
# Generate the time vector properly
t = np.arange(1000) / fs
signala = np.sin(2*np.pi*60*t)+np.sin(2*np.pi*20*t) # with frequency of 60 and 20Hz
plt.plot(t, signala)
plt.legend(['mixture of 60 and 20Hz'])
plt.title("111807066")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.show()
										            
fc = 30  # Cut-off frequency of the filter
w = fc / (fs / 2) # Normalize the frequency
b, a = signal.butter(5, w, 'low')                             #butterworth low pass filter
output = signal.filtfilt(b, a, signala)
plt.plot(t, output)
plt.legend(['Filtered signal'])
plt.title("111807066_butterworth filter low pass")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.show()

Y = abs(np.fft.fft(output))# dft and normalization
freq=np.linspace(0,fs,len(Y))
N=len(Y)
plt.plot(freq[0:(N//4)+1],Y[0:(N//4)+1])   # plotting the spectrum
plt.xlabel('Freq (Hz)')
plt.ylabel('|Y(freq)|')
plt.legend(['Filtered signal Freq response'], loc='upper right')
plt.title('111807066_butterworth filter low pass')
plt.show()

b, a = signal.butter(5, w, 'high')                   #butterworth high pass filter
output1 = signal.filtfilt(b, a, signala)
plt.plot(t, output1)
plt.legend(['Filtered signal'])
plt.title("111807066_butterworth filter high pass")
plt.xlabel("time")

										            
plt.ylabel("amplitude")
plt.show()

Y = abs(np.fft.fft(output1))# dft and normalization
freq=np.linspace(0,fs,len(Y))
N=len(Y)
plt.plot(freq[0:(N//4)+1],Y[0:(N//4)+1])   # plotting the spectrum
plt.xlabel('Freq (Hz)')
plt.ylabel('|Y(freq)|')
plt.legend(['Filtered signal Freq response'], loc='upper right')
plt.title('111807066_butterworth filter high pass')
plt.show()

fc = 30  # Cut-off frequency of the filter
w = fc / (fs / 2) # Normalize the frequency
b, a = signal.cheby1(5,3, w, 'low')                     #chebyshev low pass filter
output2 = signal.filtfilt(b, a, signala)
plt.plot(t, output2)
plt.legend(['Filtered signal'])
plt.title("111807066_chebyshev filter low pass")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.show()

Y = abs(np.fft.fft(output2))# dft and normalization
freq=np.linspace(0,fs,len(Y))
N=len(Y)
plt.plot(freq[0:(N//4)+1],Y[0:(N//4)+1])   # plotting the spectrum
plt.xlabel('Freq (Hz)')
										        
plt.ylabel('|Y(freq)|')
plt.legend(['Filtered signal Freq response'], loc='upper right')
plt.title('111807066_chebyshev filter low pass')
plt.show()

b, a = signal.cheby1(5,3, w, 'high')      #chebyshev high pass filter
output3 = signal.filtfilt(b, a, signala)
plt.plot(t, output3)
plt.legend(['Filtered signal'])
plt.title("111807066_chebyshev filter high pass")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.show()

Y = abs(np.fft.fft(output3))         # dft and normalization
freq=np.linspace(0,fs,len(Y))
N=len(Y)
plt.plot(freq[0:(N//4)+1],Y[0:(N//4)+1])   # plotting the spectrum
plt.xlabel('Freq (Hz)')
plt.ylabel('|Y(freq)|')
plt.legend(['Filtered signal Freq response'], loc='upper right')
plt.title('111807066_chebyshev filter low pass')
plt.show()


