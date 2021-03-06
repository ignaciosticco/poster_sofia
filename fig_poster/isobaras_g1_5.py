# Sacado de https://scipy.github.io/old-wiki/pages/Cookbook/Matplotlib/LaTeX_Examples.html

import matplotlib.pyplot as plt
import pylab
import numpy as np
import matplotlib.pyplot as plt
import math
from pylab import arange,pi,sin,cos,sqrt,savefig

# a dos columnas: 3+3/8 (ancho, in)
# a una columna : 6.5   (ancho  in)

golden_mean = (math.sqrt(5)-1.0)/2.0        # Aesthetic ratio
fig_width = 3+3/8  			    # width  in inches
fig_height = fig_width*golden_mean          # height in inches
fig_size =  [fig_width,fig_height]

params = {'backend': 'ps',
          'axes.titlesize': 8,
          'axes.labelsize': 12,
          'axes.linewidth': 0.5, 
          'axes.grid': True,
          'axes.labelweight': 'normal',  
          'font.family': 'serif',
          'font.size': 8.0,
          'font.weight': 'normal',
          'text.color': 'black',
          'xtick.labelsize': 14,
          'ytick.labelsize': 14,
          'text.usetex': True,
          'legend.fontsize': 10,
          'figure.dpi': 300,
          'figure.figsize': fig_size,
          'savefig.dpi': 300,
         }

pylab.rcParams.update(params)
#################### DATA ##############################
z = np.genfromtxt('out_press_225p_v4_g1.5_python.txt', delimiter = ' ')
minimo = 0
maximo = 20
x=np.linspace(minimo,maximo,len(z))
y=np.linspace(minimo,maximo,len(z))


#################### PLOT specification ##############################
levels=np.linspace(2000,9000,9,endpoint=True)
levbar=np.linspace(2000,9000,5,endpoint=True)
plt.contour(x, y, z,levels, linewidths=0.5, colors='k',zorder=2)
plt.contourf(x, y, z, levels, cmap=plt.cm.jet,zorder=1)
plt.colorbar(ticks=levbar)
plt.plot([20,20],[0,8.05],color='r',lw=3,zorder=3)
plt.plot([20,20],[9.25,10.75],color='r',lw=3,zorder=3)
plt.plot([20,20],[11.95,20],color='r',lw=3,zorder=3)
plt.plot([19.9,19.9],[0,8.05],color='r',lw=3,zorder=3)
plt.plot([19.9,19.9],[9.25,10.75],color='r',lw=3,zorder=3)
plt.plot([19.9,19.9],[11.95,20],color='r',lw=3,zorder=3)

pylab.xlabel('x~(m)')
pylab.ylabel('y~(m)')
pylab.ylim(2, 18)
pylab.xlim(14, 20)
pylab.xticks(np.arange(14,22,2))
pylab.yticks(np.arange(2,20,4))
#pylab.show()
plt.savefig('isobaras_g1_5.eps', format='eps', bbox_inches='tight')