import numpy as np
import matplotlib.pyplot as plt
plt.style.use('informes')

t, h, P = np.loadtxt('Mediciones/crtl_P_Kp5.csv', delimiter=',', unpack=True)

fig, ax = plt.subplots(2, 1, sharex=True)
ax[1].set_xlabel('Tiempo [s]')
ax[0].set_ylabel('Altura [pixeles]')
ax[1].set_ylabel('P [bits]')

ax[0].plot(t, h, 'C6')
ax[1].plot(t, P, 'C2')

ax[0].axhline(250, c='k')
ax[1].axhline(255, c='C4')
ax[1].axhline(200, c='C5')

plt.show()