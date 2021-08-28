import numpy as np
xn = np.array([1, 2, 3, 4])
hn = np.array([2, 3, 4, 5])
Xk = np.array([0+0j, 0+0j, 0+0j, 0+0j])
inv = np.array([0+0j, 0+0j, 0+0j, 0+0j])
N = xn.shape[0]

def dft(xn):
    Xk = np.array([0+0j, 0+0j, 0+0j, 0+0j])
    for n in range(N):
        a = 0
        b = 0
        c = 0

        for k in range(N):
            a = a + xn[k]*np.cos((2*np.pi*n*k)/N)
            b = b + xn[k]*np.sin((2*np.pi*n*k)/N)
            c = np.complex(a, -b)

        Xk[n] = c
    return Xk

for k in range(N):
    a = 0
    b = 0
    c = 0

    for n in range(N):
        a = a + xn[n] * np.cos((2 * np.pi * n * k) / N)
        b = b + xn[n] * np.sin((2 * np.pi * n * k) / N)
        c = np.complex(a/N, b/N)

    inv[k] = c
print(inv)

#dft = np.fft.fft(xn)
#print(dft)

X = dft(xn)
Y = dft(hn)
print(X)
l = np.multiply(X,Y)
ifft = np.fft.ifft(X)
print(ifft)
conv = np.convolve(xn, hn)
#print(conv, ifft)




