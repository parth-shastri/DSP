# Name - Parth Shastri 
import numpy as np

x = [1, 2, 3, 4]
h = [0, 1, 2]

conv = np.convolve(x,h)
print("linear convolution: ", conv)
ccnlen = np.maximum(len(x), len(h))
ccn = conv[:ccnlen]
residual = conv[ccnlen:]
residual = np.append(residual, [0 for i in range(ccnlen-len(residual))])

for i in range(ccnlen):
    ccn[i] = ccn[i] + residual[i]

print(ccn)





