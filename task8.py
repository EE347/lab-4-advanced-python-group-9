import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 10, 101)
print(x)

sin_wave=np.load("task7_sin.npy")
cos_wave=np.load("task7_cos.npy")
plt.plot(x,sin_wave)
plt.plot(x,cos_wave)
plt.legend(['Sin(X)','Cos(X)'])
plt.show()