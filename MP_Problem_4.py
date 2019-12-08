#MP4-Python
import matplotlib.pylab as plt
import numpy as np
import math as m
yo = float(input('Input the initial height of the launch point(m): '))
vo = float(input('Input the initial velocity(m/s): '))
angle = float(input('Input angle at which projectile is fired(wrt Ground): '))
ax = float(input('Input x-component of acceleration(Note: Mind the sign.): '))
ay = float(input('Input y-component of acceleration(Note: Mind the sign.): '))

if ay == 0:
    raise Exception('No free fall detected. The y-component of accelaration should not be zero.')
else:
    vox = vo*m.cos(m.radians(angle))
    voy = vo*m.sin(m.radians(angle))
    d = np.sqrt((voy**2)-4*(1/2*ay)*yo)
    tfin = ((-voy + d)/ay)
    t = np.arange(0,tfin,0.5)
    if tfin <= 0:
        tfin = ((-voy - d)/ay)
        t = np.arange(0,tfin,0.5)
    xni = vox*t + 0.5*ax*(t**2)
    xi = vox*t
    y = yo + voy*t + 0.5*ay*(t**2)
plt.plot(xni,y,'ro-',label = 'Non-Ideal Motion')
plt.plot(xi,y,'bo-',label = 'Ideal Motion')
plt.xlabel('Distance travelled,wrt ground(m)')
plt.ylabel('Height(m)')
plt.legend(loc="upper right")
plt.grid()
plt.show()
        
