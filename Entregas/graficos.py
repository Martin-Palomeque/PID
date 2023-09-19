import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('informes.mplstyle')

###                   Figuras P                   ###
 
kp_path = [0.7,2,4]
path = [fr'Mediciones\Clase 3\PID\PID-{i}-0-0-barrido.csv' for i in kp_path]

# fig_P, ax_P = plt.subplots(len(kp_path),1,sharex=True)

t_P = []
h_P = []
P_P = []
I_P = []
D_P = []
kp = []
for path in path:
    df = pd.read_csv(path)
    t_P.append(df['Time'])
    h_P.append(df['Position'])
    P_P.append(df['P'])
    I_P.append(df['I'])
    D_P.append(df['D'])
    kp.append(df['kp'][0])
    # kp = df['kp'][0]
    # kd = df['kd'][0]
    setpoint_P = df['Setpoint'][0]

# for i in range(len(kp_path)):
#     for j in range(len(kp_path)):
#         if i == j:
#             color = 'tomato' 
#             ax_P[i].plot(t_P[j],h_P[j],label = f'{kp[i]}',color = color)
#             ax_P[i].hlines(setpoint,t_P[j].iloc[0],t_P[j].iloc[-1],linestyle = '--',alpha = 0.2)
#         else:
#             ax_P[i].plot(t_P[j],h_P[j],label = None,color = 'gray',alpha = 0.3)
#     ax_P[i].legend(fontsize = 'medium')

# plt.legend()    
# plt.show()

###            Figuras de PI              ###
# Todos los Ki [0,0.01,0.03,0.05,0.07,.09]
ki_path = [0.03,0.07,.09]
path = [fr'Mediciones\Clase 3\PID\PID-2-{i}-0-barrido.csv' for i in ki_path]

# fig_PI, ax_PI = plt.subplots(6,1,sharex=True)

t_PI = []
h_PI =[]
P_PI = []
I_PI = []
D_PI = []
ki = []
for path in path:
    df = pd.read_csv(path)
    t_PI.append(df['Time'])
    h_PI.append(df['Position'])
    P_PI.append(['P'])
    I_PI.append(['I'])
    D_PI.append(df['D'])
    ki.append(df['ki'][0])
    kd = df['kd'][0]
    setpoint_PI = df['Setpoint'][0]

# for i in range(6):
#     for j in range(6):
#         if i == j:
#             color = 'tomato' 
#             ax_PI[i].plot(t_PI[j],h_PI[j],label = f'{ki[i]}',color = color)
#             ax_PI[i].hlines(setpoint,t_PI[j].iloc[0],t_PI[j].iloc[-1],linestyle = '--',alpha = 0.2)
#         else:
#             ax_PI[i].plot(t_PI[j],h_PI[j],label = None,color = 'gray',alpha = 0.3)
#     ax_PI[i].legend()

            

# plt.legend()
# plt.show()

###           Figuras PID            ###

kd_path = [.25,.75,4]
path = [fr'Mediciones\Clase 3\PID\PID-2-0.07-{i}-barrido.csv' for i in kd_path]

# fig_PID, ax_PID = plt.subplots(len(kd_path),1,sharex=True)

t_PID = []
h_PID = []
P_PID = []
I_PID = []
D_PID = []
kd = []
for path in path:
    df = pd.read_csv(path)
    t_PID.append(df['Time'])
    h_PID.append(df['Position'])
    P_PID.append(df['P'])
    I_PID.append(df['I'])
    D_PID.append(df['D'])
    kd.append(df['kd'][0])
    setpoint_PID = df['Setpoint'][0]

# for i in range(len(kd_path)):
#     for j in range(len(kd_path)):
#         if i == j:
#             color = 'tomato' 
#             ax_PID[i].plot(t_PID[j],h_PID[j],label = f'{kd[i]}',color = color)
#             ax_PID[i].hlines(setpoint,t_PID[j].iloc[0],t_PID[j].iloc[-1],linestyle = '--',alpha = 0.2)
#         else:
#             ax_PID[i].plot(t_PID[j],h_PID[j],label = None,color = 'gray',alpha = 0.3)
#     ax_PID[i].legend()
# plt.legend()
# plt.show()

fig, ax = plt.subplots(3,1,sharex = True)

ax[0].plot(t_P[0],h_P[0],label = f'{kp[0]}')
ax[0].plot(t_P[1],h_P[1],label = f'{kp[1]}')
ax[0].plot(t_P[2],h_P[2],label = f'{kp[2]}')
ax[0].hlines(setpoint_P,t_P[0].iloc[0],t_P[0].iloc[-1],linestyle = '--',alpha = 0.85,color = 'indigo')
ax[0].legend(fontsize = 'medium')

ax[1].plot(t_PI[0],h_PI[0],label = f'{ki[0]}')
ax[1].plot(t_PI[1],h_PI[1],label = f'{ki[1]}')
ax[1].plot(t_PI[2],h_PI[2],label = f'{ki[2]}')
ax[1].hlines(setpoint_PI,t_PI[0].iloc[0],t_PI[0].iloc[-1],linestyle = '--',alpha = 0.85,color = 'indigo')
ax[1].legend(fontsize = 'medium')

ax[2].plot(t_PID[0],h_PID[0],label = f'{kd[0]}')
ax[2].plot(t_PID[1],h_PID[1],label = f'{kd[1]}')
ax[2].plot(t_PID[2],h_PID[2],label = f'{kd[2]}')
ax[2].hlines(setpoint_PID,t_PID[0].iloc[0],t_PID[0].iloc[-1],linestyle = '--',alpha = 0.85,color = 'indigo')
ax[2].legend(fontsize = 'medium')

plt.show()