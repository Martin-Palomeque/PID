import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Rectangle

### Datos   ###
path = r'C:\Users\lucio\OneDrive\Documentos\GitHub\Shared_PID\Mediciones\posiciones-onoff2.csv'

df = pd.read_csv(path,header = None,names = ['Time','Position','On-Off'])

t = df['Time']
pos = df['Position']
power = df['On-Off']

### Indices ###

indices_on = []
indices_off = []
for i in range(len(t)-1):
    if power[i] - power[i+1] == -1:
        indices_on.append(i)
    elif power[i] - power[i+1] == 1:
        indices_off.append(i)

t_on = [t[i] for i in indices_on]
t_off = [t[i] for i in indices_off]
pos_on = [pos[i] for i in indices_on]
pos_off = [pos[i] for i in indices_off]

### Figura  ###
fig,ax = plt.subplots()

ax.plot(t,pos,color = 'cornflowerblue',label = f'Posicion')

ax.axhline(200,color = 'indigo',alpha = 0.3, label = f'Setpoint')
# ax.scatter(t_on,pos_on,marker = '.',color = 'darkgreen',s = 50)
# ax.scatter(t_off,pos_off,marker = '.',color = 'tomato',s=50)
fig.set_figwidth(12)
fig.set_figheight(8)
ax.grid()
ax.set_ylabel('Altura [pixeles]')


fig.suptitle(f'On-Off 2')
plt.xlabel(f'Tiempo [s]')

###  Intervalos de prendido y apagado  ####
On_1 = t[:indices_off[0]]
On_2 = t[indices_on[0]:indices_off[1]]
On_3 = t[indices_on[1]:indices_off[2]]
On_4 = t[indices_on[2]:indices_off[3]]
On_5 = t[indices_on[3]:indices_off[4]]
On_6 = t[indices_on[4]:indices_off[5]]
On_7 = t[indices_on[5]:indices_off[6]]
On_8 = t[indices_on[6]:indices_off[7]]
On_9 = t[indices_on[7]:indices_off[8]]
On_10 = t[indices_on[8]:indices_off[9]]
On_11 = t[indices_on[9]:indices_off[10]]
On_12 = t[indices_on[10]:indices_off[11]]

Off_1 = t[indices_off[0]:indices_on[0]]
Off_2 = t[indices_off[1]:indices_on[1]]
Off_3 = t[indices_off[2]:indices_on[2]]
Off_4 = t[indices_off[3]:indices_on[3]]
Off_5 = t[indices_off[4]:indices_on[4]]
Off_6 = t[indices_off[5]:indices_on[5]]
Off_7 = t[indices_off[6]:indices_on[6]]
Off_8 = t[indices_off[7]:indices_on[7]]
Off_9 = t[indices_off[8]:indices_on[8]]
Off_10 = t[indices_off[9]:indices_on[9]]
Off_11 = t[indices_off[10]:indices_on[10]]
Off_12 = t[indices_off[11]::]

### Rectangulos On-Off  ###
Opacidad = 0.15
# ax.add_patch(Rectangle((t[0],pos[0]),On_1.values[-1]-On_1.values[0],400,alpha = Opacidad,color = 'darkgreen',label = f'Fuente Encendida'))
# ax.add_patch(Rectangle((t_on[0],pos[0]),On_2.values[-1]-On_2.values[0],400,alpha = Opacidad,color = 'darkgreen'))
# ax.add_patch(Rectangle((t_on[1],pos[0]),On_3.values[-1]-On_3.values[0],400,alpha = Opacidad,color = 'darkgreen'))
# ax.add_patch(Rectangle((t_on[2],pos[0]),On_4.values[-1]-On_4.values[0],400,alpha = Opacidad,color = 'darkgreen'))
# ax.add_patch(Rectangle((t_on[3],pos[0]),On_5.values[-1]-On_5.values[0],400,alpha = Opacidad,color = 'darkgreen'))
# ax.add_patch(Rectangle((t_on[4],pos[0]),On_6.values[-1]-On_6.values[0],400,alpha = Opacidad,color = 'darkgreen'))
# ax.add_patch(Rectangle((t_on[5],pos[0]),On_7.values[-1]-On_7.values[0],400,alpha = Opacidad,color = 'darkgreen'))
# ax.add_patch(Rectangle((t_on[6],pos[0]),On_8.values[-1]-On_8.values[0],400,alpha = Opacidad,color = 'darkgreen'))
# ax.add_patch(Rectangle((t_on[7],pos[0]),On_9.values[-1]-On_9.values[0],400,alpha = Opacidad,color = 'darkgreen'))
# ax.add_patch(Rectangle((t_on[8],pos[0]),On_10.values[-1]-On_10.values[0],400,alpha = Opacidad,color = 'darkgreen'))
# ax.add_patch(Rectangle((t_on[9],pos[0]),On_11.values[-1]-On_11.values[0],400,alpha = Opacidad,color = 'darkgreen'))
# ax.add_patch(Rectangle((t_on[10],pos[0]),On_12.values[-1]-On_12.values[0],400,alpha = Opacidad,color = 'darkgreen'))
###
ax.add_patch(Rectangle((t[0],pos[0]),On_1.values[-1]-On_1.values[0],50,alpha = 0.3,color = 'darkgreen',label = f'Fuente Encendida'))
ax.add_patch(Rectangle((t_on[0],pos[0]),On_2.values[-1]-On_2.values[0],50,alpha = 0.3,color = 'darkgreen'))
ax.add_patch(Rectangle((t_on[1],pos[0]),On_3.values[-1]-On_3.values[0],50,alpha = 0.3,color = 'darkgreen'))
ax.add_patch(Rectangle((t_on[2],pos[0]),On_4.values[-1]-On_4.values[0],50,alpha = 0.3,color = 'darkgreen'))
ax.add_patch(Rectangle((t_on[3],pos[0]),On_5.values[-1]-On_5.values[0],50,alpha = 0.3,color = 'darkgreen'))
ax.add_patch(Rectangle((t_on[4],pos[0]),On_6.values[-1]-On_6.values[0],50,alpha = 0.3,color = 'darkgreen'))
ax.add_patch(Rectangle((t_on[5],pos[0]),On_7.values[-1]-On_7.values[0],50,alpha = 0.3,color = 'darkgreen'))
ax.add_patch(Rectangle((t_on[6],pos[0]),On_8.values[-1]-On_8.values[0],50,alpha = 0.3,color = 'darkgreen'))
ax.add_patch(Rectangle((t_on[7],pos[0]),On_9.values[-1]-On_9.values[0],50,alpha = 0.3,color = 'darkgreen'))
ax.add_patch(Rectangle((t_on[8],pos[0]),On_10.values[-1]-On_10.values[0],50,alpha = 0.3,color = 'darkgreen'))
ax.add_patch(Rectangle((t_on[9],pos[0]),On_11.values[-1]-On_11.values[0],50,alpha = 0.3,color = 'darkgreen'))
ax.add_patch(Rectangle((t_on[10],pos[0]),On_12.values[-1]-On_12.values[0],50,alpha = 0.3,color = 'darkgreen'))
###
# ax.add_patch(Rectangle((t_off[0],pos[0]),Off_1.values[-1]-Off_1.values[0],50,alpha = 0.3,color = 'tomato'))
# ax.add_patch(Rectangle((t_off[1],pos[0]),Off_2.values[-1]-Off_2.values[0],50,alpha = 0.3,color = 'tomato'))
# ax.add_patch(Rectangle((t_off[2],pos[0]),Off_3.values[-1]-Off_3.values[0],50,alpha = 0.3,color = 'tomato'))
# ax.add_patch(Rectangle((t_off[3],pos[0]),Off_4.values[-1]-Off_4.values[0],50,alpha = 0.3,color = 'tomato'))
# ax.add_patch(Rectangle((t_off[4],pos[0]),Off_5.values[-1]-Off_5.values[0],50,alpha = 0.3,color = 'tomato'))
# ax.add_patch(Rectangle((t_off[5],pos[0]),Off_6.values[-1]-Off_6.values[0],50,alpha = 0.3,color = 'tomato'))
# ax.add_patch(Rectangle((t_off[6],pos[0]),Off_7.values[-1]-Off_7.values[0],50,alpha = 0.3,color = 'tomato'))
# ax.add_patch(Rectangle((t_off[7],pos[0]),Off_8.values[-1]-Off_8.values[0],50,alpha = 0.3,color = 'tomato'))
# ax.add_patch(Rectangle((t_off[8],pos[0]),Off_9.values[-1]-Off_9.values[0],50,alpha = 0.3,color = 'tomato'))
# ax.add_patch(Rectangle((t_off[9],pos[0]),Off_10.values[-1]-Off_10.values[0],50,alpha = 0.3,color = 'tomato'))
# ax.add_patch(Rectangle((t_off[10],pos[0]),Off_11.values[-1]-Off_11.values[0],50,alpha = 0.3,color = 'tomato'))
# ax.add_patch(Rectangle((t_off[11],pos[0]),Off_12.values[-1]-Off_12.values[0],50,alpha = 0.3,color = 'tomato'))

### Linea Vertical  ###

Opacity = 0.65
# ax.axvline(t_on[0],0.25,0.75,linestyle = ':',color = 'darkgreen',alpha = Opacity)
# ax.axvline(t_on[1],.35,.65,linestyle = ':',color = 'darkgreen',alpha = Opacity)
# ax.axvline(t_on[2],.45,.6,linestyle = ':',color = 'darkgreen',alpha = Opacity)
# ax.axvline(t_on[3],.45,.6,linestyle = ':',color = 'darkgreen',alpha = Opacity)
# ax.axvline(t_on[4],.45,.6,linestyle = ':',color = 'darkgreen',alpha = Opacity)
# ax.axvline(t_on[5],.45,.6,linestyle = ':',color = 'darkgreen',alpha = Opacity)
# ax.axvline(t_on[6],.45,.6,linestyle = ':',color = 'darkgreen',alpha = Opacity)
# ax.axvline(t_on[7],.45,.6,linestyle = ':',color = 'darkgreen',alpha = Opacity)
# ax.axvline(t_on[8],.45,.6,linestyle = ':',color = 'darkgreen',alpha = Opacity)
# ax.axvline(t_on[9],.45,.6,linestyle = ':',color = 'darkgreen',alpha = Opacity)
# ax.axvline(t_on[10],.45,.6,linestyle = ':',color = 'darkgreen',alpha = Opacity)





plt.legend()
plt.show()
# print(On_1.values[-1])