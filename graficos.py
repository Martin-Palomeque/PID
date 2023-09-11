import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# plt.style.use('informes')
path = [fr'Mediciones\Clase 3\Mediciones\PID\PID-2-{i}-0-barrido.csv' for i in[0,0.01,0.03,0.05,0.07,.09]]

fig, ax = plt.subplots(6,1,sharex=True)
fig.set_figheight(8)
fig.set_figwidth(12)
ki_list = []

t = []
h =[]
P = []
I = []
D = []
ki = []
for path in path:
    df = pd.read_csv(path)
    t.append(df['Time'])
    h.append(df['Position'])
    P.append(['P'])
    I.append(['I'])
    D.append(df['D'])
    ki.append(df['ki'][0])
    kp = df['kp'][0]
    kd = df['kd'][0]
    setpoint = df['Setpoint']
    # ki_list.append(ki)
for i in range(6):
    for j in range(6):
        if i == j:
            color = 'tomato' 
            ax[i].plot(t[j],h[j],label = f'{ki[i]}',color = color)
        else:
            ax[i].plot(t[j],h[j],label = None,color = 'gray',alpha = 0.3)
    ax[i].legend()

        

# plt.legend()
plt.show()