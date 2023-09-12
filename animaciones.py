import numpy as np
import matplotlib.pyplot as plt
import time
import matplotlib.animation as animation
import pandas as pd
import matplotlib

fig, ax = plt.subplots()
fig.set_figheight(8)
fig.set_figwidth(12)
matplotlib.rcParams['animation.ffmpeg_path'] = r"C:\Users\lucio\OneDrive\Documentos\Python\ffmpeg-6.0-essentials_build\bin\ffmpeg.exe"

kd_path = [.75]
path = [fr'Mediciones\Clase 3\Mediciones\PID\PID-2-0.07-{i}-barrido.csv' for i in kd_path]

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
    setpoint = df['Setpoint']




def onClick(event): #Simplemente es una funcion que cambia el estado de la variable pause
    global pause
    pause ^= True 
pause = False
t_anim = []
h_anim = []
def update(frame,t,h):
    ax.cla()
    t_anim.append(t[0][frame])
    h_anim.append(h[0][frame])
    ax.hlines(setpoint,0,t_anim[-1], linestyles='--')
    ax.grid()
    ax.set_ylim(0, 500)
    ax.set_xlim(0,None)
    ax.set_xlabel(f'Time [s]')
    ax.set_ylabel(f'Position [pixel]')
    ax.plot(t_anim,h_anim,color = 'cornflowerblue')





fig.canvas.mpl_connect('scroll_event',onClick) #Conecta la figura a un evento. El evento es el scroll del mouse en la figura ('scroll_event') y ejecuta la funcion 'onClick'


ani = animation.FuncAnimation(fig,update,frames = len(t[0]),interval = 16.66,fargs = (t,h))
writer = animation.FFMpegWriter(fps=120, metadata=dict(artist='Me'), bitrate=5000)
print('Guardando...')
ani.save('PID120fps.mp4', writer=writer) 
print("Ç'est fini")
# plt.show()