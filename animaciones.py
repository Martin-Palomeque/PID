import numpy as np
import matplotlib.pyplot as plt
import time
import matplotlib.animation as animation
import pandas as pd
import matplotlib

###     Seteo de la figura  ###
t0 = 0
tf = 30

fig, ax = plt.subplots()
fig.set_figheight(8)
fig.set_figwidth(12)
ax.grid()
ax.set_ylim(0, 600)
ax.set_xlim(t0,tf)
ax.set_xlabel(f'Time [s]')
ax.set_ylabel(f'Position [pixel]')
matplotlib.rcParams['animation.ffmpeg_path'] = r"C:\Users\lucio\OneDrive\Documentos\Python\ffmpeg-6.0-essentials_build\bin\ffmpeg.exe"



###     Animacion de P      ###
animacion = True
kp_path = [2]
path = [fr'Mediciones\Clase 3\Mediciones\PID\PID-{i}-0-0-barrido.csv' for i in kp_path]

t = []
h = []
P = []
kp = []



for path in path: #Crea una lista de listas
    df = pd.read_csv(path)
    kp.append(df['kp'][0])
    #Selecciona los datos correspondientes al intervalo dado.
    df = df[df['Time']>t0]
    df = df[df['Time']<tf].reset_index()

    t.append(df['Time'])
    h.append(df['Position'])
    P.append(df['P'])
    setpoint = df['Setpoint']

t[0] += 4.5 #Este tiempo lo agrego para que la curva levante mas o menos al mismo timepo. Esto se debe a que la potencia cero en P solo era de 180 bits. Y en PID y PI era de 0.

t_anim = []
h_anim = []
line_P, = ax.plot([],[],color = 'indigo')
def update(frame,t,h,t_max):
    t_anim.append(t[0][frame])
    h_anim.append(h[0][frame])
    # ax.hlines(setpoint,0,t_anim[-1], linestyles='--')
    line_P.set_data(t_anim[:frame],h_anim[:frame])


t_max = round(t[0].iloc[-1])

# line_PID = ax.plot(t[0],h[0]/2,color = 'indigo')
# plt.show()

if animacion == True:
    ani = animation.FuncAnimation(fig,update,frames = len(t[0]),interval = 16.66,fargs = (t,h,t_max),repeat = False)
    writer = animation.FFMpegWriter(fps=60, metadata=dict(artist='Me'), bitrate=800)
    print('Guardando...')
    t1 = time.time()
    ani.save('P60fps.mp4', writer=writer) 
    t2 = time.time()
    print(f'Finished in {t2-t1}')
else:
    line_P = ax.plot(t[0],h[0],color = 'indigo')


# ###     Animacion de PI      ###
animacion = True
ki_path = [0.07]
path = [fr'Mediciones\Clase 3\Mediciones\PID\PID-2-{i}-0-barrido.csv' for i in ki_path]

t = []
h = []
P = []
ki = []


for path in path: #Crea una lista de listas
    df = pd.read_csv(path)
    ki.append(df['ki'][0])
    #Selecciona los datos correspondientes al intervalo dado.
    df = df[df['Time']>t0]
    df = df[df['Time']<tf].reset_index()

    t.append(df['Time'])
    h.append(df['Position'])
    P.append(df['P'])
    setpoint = df['Setpoint']

line_PI, = ax.plot([],[],color = 'cornflowerblue')

t_anim = []
h_anim = []
def update(frame,t,h,t_max):
    t_anim.append(t[0][frame])
    h_anim.append(h[0][frame])
    # ax.hlines(setpoint,0,t_anim[-1], linestyles='--')
    line_PI.set_data(t_anim[:frame],h_anim[:frame])
    

t_max = round(t[0].iloc[-1])

# line_PID = ax.plot(t[0],h[0]/2,color = 'indigo')
# plt.show()

if animacion == True:
    ani = animation.FuncAnimation(fig,update,frames = len(t[0]),interval = 16.66,fargs = (t,h,t_max),repeat = False)
    writer = animation.FFMpegWriter(fps=60, metadata=dict(artist='Me'), bitrate=800)
    name = f'PI60fps.mp4'
    print(f'Guardando como {name}...')
    t1 = time.time()
    ani.save(name, writer=writer) 
    t2 = time.time()
    print(f'Finished in {t2-t1}')
else:
    line_PI = ax.plot(t[0],h[0],color = 'cornflowerblue')



# ###     Animacion de PID    ### -> Falta agregar que plotee sobre P y PI

animacion = True

kd_path = [.75]
path = [fr'Mediciones\Clase 3\Mediciones\PID\PID-2-0.07-{i}-barrido.csv' for i in kd_path]

t = []
h = []
P = []
I = []
D = []
kd = []


for path in path: #Crea una lista de listas
    df = pd.read_csv(path)
    kd.append(df['kd'][0])
    #Selecciona los datos correspondientes al intervalo dado.
    df = df[df['Time']>t0]
    df = df[df['Time']<tf].reset_index()

    t.append(df['Time'])
    h.append(df['Position'])
    P.append(df['P'])
    I.append(df['I'])
    D.append(df['D'])
    setpoint = df['Setpoint']


t_anim = []
h_anim = []
line_PID, = ax.plot([],[],color = 'tomato')

def update(frame,t,h,t_max):
    t_anim.append(t[0][frame])
    h_anim.append(h[0][frame])
    # line_PID = ax.plot(t_anim,h_anim,color = 'tomato')
    line_PID.set_data(t_anim[:frame],h_anim[:frame])


t_max = round(t[0].iloc[-1])

if animacion == True:
    ani = animation.FuncAnimation(fig,update,frames = len(t[0]),interval = 16.66,fargs = (t,h,t_max),repeat = False)
    writer = animation.FFMpegWriter(fps=60, metadata=dict(artist='Me'), bitrate=800)
    name = f'PID60fps.mp4'
    print(f'Guardando como {name}...')
    t1 = time.time()
    ani.save('', writer=writer) 
    t2 = time.time()
    print(f'Finished in {t2-t1}')
else:
    line_PID = ax.plot(t[0],h[0],color = 'tomato')

# plt.show()

