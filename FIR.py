#FIR filter
import numpy as np 
import matplotlib.pyplot as plt
from scipy import signal
fs = 4000 # Sampling frequency
t =  np.arange(0,1,1/fs)
signala=np.sin(2*np.pi*500*t)+np.sin(2*np.pi*700*t)+np.sin(2*np.pi*900*t)+np.sin(2*np.pi*1500*t)+np.sin(2*np.pi*1700*t)+np.sin(2*np.pi*1900*t)   #signal 
plt.tight_layout()
plt.plot(signala[0:100])
plt.legend(['signal'])
plt.title("111807066")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.show()
a=5      
M=2*a+1
Wc=1200

										        
#filter coefficients 
h=np.zeros(M)
for n in range(M): 
    if n!=5:
        h[n]=(np.sin(n-a)*Wc)/(np.pi*(n-a))
    else:
        h[n]=Wc/4

print("filter coefficients\n")
print(h,"\n")
plt.stem(h)
plt.legend(["filter coefficients"])
plt.title("111807066")
plt.xlabel("n")
plt.ylabel("f(n)")
plt.show()
#hamming window
W=np.zeros(M)
for n in range(M):
    W[n]=0.54-0.46*np.cos((2*np.pi*n)/10)    

print("hamming window  coefficients")
print(W,"\n")
plt.stem(W)
plt.legend(["hamming coefficients"])
plt.title("111807066")
plt.xlabel("n")
plt.ylabel("h(n)")
plt.show()

										            
#multiply  the filter coefficients and window coefficients
H=np.zeros(M)    
H=h*W
print(H)
y=np.convolve(signala,H)           # concolve the multiplyed signal with the input signal
plt.plot(y[0:100])
plt.legend(['Filtered Signal'])
plt.title("111807066")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.show()

Y = abs(np.fft.fft(signala))     # dft and normalization
freq=np.linspace(0,fs,len(Y))
N=len(y)
plt.plot(freq[0:(N//2)+1],Y[0:(N//2)+1])   # plotting the spectrum
plt.xlabel('Freq (Hz)')
plt.ylabel('|Y(freq)|')
plt.legend(['Signal Freq response'], loc='upper right')
plt.title('111807066')
plt.show()
Y = abs(np.fft.fft(y))           # dft and normalization
freq=np.linspace(0,fs,len(Y))
N=len(y)
plt.plot(freq[0:(N//2)+1],Y[0:(N//2)+1])   # plotting the spectrum
plt.xlabel('Freq (Hz)')
plt.ylabel('|Y(freq)|')
plt.legend(['Filtered Signal Freq response'], loc='upper right')
plt.title('111807066')
plt.show()
