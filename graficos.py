import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# plt.style.use('informes')

###     Figuras de PI   ###
# path = [fr'Mediciones\Clase 3\Mediciones\PID\PID-2-{i}-0-barrido.csv' for i in[0,0.01,0.03,0.05,0.07,.09]]

# fig, ax = plt.subplots(6,1,sharex=True)
# fig.set_figheight(8)
# fig.set_figwidth(12)
# ki_list = []

# t = []
# h =[]
# P = []
# I = []
# D = []
# ki = []
# for path in path:
#     df = pd.read_csv(path)
#     t.append(df['Time'])
#     h.append(df['Position'])
#     P.append(['P'])
#     I.append(['I'])
#     D.append(df['D'])
#     ki.append(df['ki'][0])
#     kp = df['kp'][0]
#     kd = df['kd'][0]
#     setpoint = df['Setpoint']
#     # ki_list.append(ki)
# for i in range(6):
#     for j in range(6):
#         if i == j:
#             color = 'tomato' 
#             ax[i].plot(t[j],h[j],label = f'{ki[i]}',color = color)
#         else:
#             ax[i].plot(t[j],h[j],label = None,color = 'gray',alpha = 0.3)
#     ax[i].legend()

            

    # plt.legend()
    # plt.show()

###     Figuras PID     ###
kd_path = [.25,.75,4]
path = [fr'Mediciones\Clase 3\Mediciones\PID\PID-2-0.07-{i}-barrido.csv' for i in kd_path]

# fig, ax = plt.subplots(len(kd_path),1,sharex=True)
fig, ax = plt.subplots()

fig.set_figheight(8)
fig.set_figwidth(12)

t = []
h = []
P = []
I = []
D = []
kd = []
for path in path:
    df = pd.read_csv(path)
    t.append(df['Time'])
    h.append(df['Position'])
    P.append(df['P'])
    I.append(df['I'])
    D.append(df['D'])
    kd.append(df['kd'][0])
    kp = df['kp'][0]
    # kd = df['kd'][0]
    setpoint = df['Setpoint']
# ki_list.append(ki)
###     Subplot de 6 filas
# for i in range(len(kd_path)):
#     for j in range(len(kd_path)):
#         if i == j:
#             color = 'tomato' 
#             ax[i].plot(t[j],h[j],label = f'{kd[i]}',color = color)
#         else:
#             ax[i].plot(t[j],h[j],label = None,color = 'gray',alpha = 0.3)
#     ax[i].legend()
###     Figura de 1 plot
for i in range(len(kd_path)):
    ax.plot(t[i],h[i],label = f'kd={kd_path[i]}')
ax.legend()
plt.show()
###     Figuras P   ###
 
# kp_path = [0.7,1,2,3,4]
# path = [fr'Mediciones\Clase 3\Mediciones\PID\PID-{i}-0-0-barrido.csv' for i in kp_path]

# fig, ax = plt.subplots(len(kp_path),1,sharex=True)
# fig.set_figheight(8)
# fig.set_figwidth(12)

# t = []
# h = []
# P = []
# I = []
# D = []
# kp = []
# for path in path:
#     df = pd.read_csv(path)
#     t.append(df['Time'])
#     h.append(df['Position'])
#     P.append(df['P'])
#     I.append(df['I'])
#     D.append(df['D'])
#     kp.append(df['kp'][0])
#     # kp = df['kp'][0]
#     # kd = df['kd'][0]
#     setpoint = df['Setpoint']
# # ki_list.append(ki)
# for i in range(len(kp_path)):
#     for j in range(len(kp_path)):
#         if i == j:
#             color = 'tomato' 
#             ax[i].plot(t[j],h[j],label = f'{kp[i]}',color = color)
#         else:
#             ax[i].plot(t[j],h[j],label = None,color = 'gray',alpha = 0.3)
#     ax[i].legend()
# plt.show()