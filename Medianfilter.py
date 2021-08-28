import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(1,50,num=2000 )
pure=np.sin(x)
plt.subplot(3,1,1)
plt.plot(x,pure)
plt.title('Pure wave-111807066')

imp_noise=np.zeros(2000)
imp_noise[300]=2
imp_noise[600]=4
imp_noise[800]=2
imp_noise[1100]=-3
imp_noise[1500]=4
imp_noise[1700]=6
imp_noise[1860]=-4

appended=pure+imp_noise

plt.subplot(3,1,2)
plt.plot(x,appended)
plt.title("Noisy-111807066")

final=np.zeros(2000)
for i in range(1,2000-1):
    temp=(appended[i-1],appended[i],appended[i+1])
    sort_temp=sorted(temp)
    final[i-1]=sort_temp[1]

plt.subplot(3,1,3)
plt.plot(x,final)
plt.title("Filtered-111807066")
plt.show()
