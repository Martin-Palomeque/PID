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
ax.set_xlabel(f'Time [s]',fontsize = 'large')
ax.set_ylabel(f'Position [pixel]',fontsize = 'large')
matplotlib.rcParams['animation.ffmpeg_path'] = r"C:\Users\lucio\OneDrive\Documentos\Python\ffmpeg-6.0-essentials_build\bin\ffmpeg.exe"
plt.rcParams["animation.convert_path"] = r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"

###     Animacion de P      ###
animacion = True
kp_path = [2]
path = [fr'Mediciones\Clase 3\PID\PID-{i}-0-0-barrido.csv' for i in kp_path]

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
line_P, = ax.plot([],[],color = 'indigo',linewidth = 3,alpha = 0.8,label = 'P')
ax.hlines(400,t0,tf,linestyles='--',color = 'dimgray',alpha= 0.4,label = 'Setpoint')
ax.legend(fontsize = 'xx-large')
def update(frame,t,h,t_max):
    t_anim.append(t[0][frame])
    h_anim.append(h[0][frame])
    # ax.hlines(setpoint,0,t_anim[-1], linestyles='--')
    line_P.set_data(t_anim[:frame],h_anim[:frame])


t_max = round(t[0].iloc[-1])

# line_PID = ax.plot(t[0],h[0]/2,color = 'indigo')
# plt.show()

if animacion == True:
    fps = 120
    ani = animation.FuncAnimation(fig,update,frames = len(t[0]),interval = 16.66,fargs = (t,h,t_max),repeat = False)
    writer = animation.FFMpegWriter(fps=fps, metadata=dict(artist='Me'), bitrate=8000)
    # writer = animation.PillowWriter(fps=fps,metadata=dict(artist='Me'),bitrate=300)
    # writer = animation.PillowWriter(fps=fps)
    name = f'P-{fps}.mp4'
    print(f'Guardando como {name}...')
    t1 = time.time()
    ani.save(name, writer=writer)
    t2 = time.time()
    print(f'Finished in {t2-t1}')
else:
    line_P = ax.plot(t[0],h[0],color = 'indigo')


# ###     Animacion de PI      ###
animacion = True
ki_path = [0.07]
path = [fr'Mediciones\Clase 3\PID\PID-2-{i}-0-barrido.csv' for i in ki_path]

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

line_PI, = ax.plot([],[],color = 'cornflowerblue',linewidth = 3,alpha = 0.8,label = 'PI')
ax.legend(fontsize = 'xx-large')

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
    fps = 120
    ani = animation.FuncAnimation(fig,update,frames = len(t[0]),interval = 16.66,fargs = (t,h,t_max),repeat = False)
    writer = animation.FFMpegWriter(fps=fps, metadata=dict(artist='Me'), bitrate=8000)
    # writer = animation.PillowWriter(fps=fps,metadata=dict(artist='Me'),bitrate=300)
    name = f'PI-{fps}.mp4'
    print(f'Guardando como {name}...')
    t1 = time.time()
    ani.save(name, writer=writer) 
    t2 = time.time()
    print(f'Finished in {t2-t1}')
    line_PI = ax.plot(t[0],h[0],color = 'cornflowerblue')



# ###     Animacion de PID    ### -> Falta agregar que plotee sobre P y PI

animacion = True

kd_path = [.75]
path = [fr'Mediciones\Clase 3\PID\PID-2-0.07-{i}-barrido.csv' for i in kd_path]

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
line_PID, = ax.plot([],[],color = 'tomato',linewidth = 3,alpha = 0.8,label = 'PID')
ax.legend(fontsize = 'xx-large')

def update(frame,t,h,t_max):
    t_anim.append(t[0][frame])
    h_anim.append(h[0][frame])
    # line_PID = ax.plot(t_anim,h_anim,color = 'tomato')
    line_PID.set_data(t_anim[:frame],h_anim[:frame])


t_max = round(t[0].iloc[-1])

if animacion == True:
    fps = 120
    ani = animation.FuncAnimation(fig,update,frames = len(t[0]),interval = 16.66,fargs = (t,h,t_max),repeat = False)
    writer = animation.FFMpegWriter(fps=fps, metadata=dict(artist='Me'), bitrate=8000)
    # writer = animation.PillowWriter(fps=fps,metadata=dict(artist='Me'),bitrate=300)
    name = f'PID-{fps}.mp4'
    print(f'Guardando como {name}...')
    t1 = time.time()
    ani.save(name, writer=writer) 
    t2 = time.time()
    print(f'Finished in {t2-t1}')
else:
    line_PID = ax.plot(t[0],h[0],color = 'tomato')

# plt.show()

