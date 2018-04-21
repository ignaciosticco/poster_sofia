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
z = np.genfromtxt('out_press_225p_v4_g5_python.txt', delimiter = ' ')
minimo = 0
maximo = 20
x=np.linspace(minimo,maximo,len(z))
y=np.linspace(minimo,maximo,len(z))


#################### PLOT specification ##############################
#pylab.figure(1)
#pylab.clf()
levels=np.linspace(2000,9000,9,endpoint=True)
levbar=np.linspace(2000,9000,5,endpoint=True)
plt.contour(x, y, z,levels, linewidths=0.5, colors='k',zorder=2)
plt.contourf(x, y, z, levels, cmap=plt.cm.jet,zorder=1)
plt.colorbar(ticks=levbar)
plt.plot([20,20],[0,6.3],color='r',lw=3,zorder=3)
plt.plot([20,20],[7.5,12.5],color='r',lw=3,zorder=3)
plt.plot([20,20],[13.7,20],color='r',lw=3,zorder=3)
plt.plot([19.9,19.9],[0,6.3],color='r',lw=3,zorder=3)
plt.plot([19.9,19.9],[7.5,12.5],color='r',lw=3,zorder=3)
plt.plot([19.9,19.9],[13.7,20],color='r',lw=3,zorder=3)

'''
pylab.axes([0.125,0.2,0.95-0.125,0.95-0.2])
pylab.errorbar(gap1,te1,yerr=yerr1,fmt='-o',mfc='white',markersize=8, color='black')
#pylab.errorbar(gap1,te1,yerr=yerr1,marker='o',markersize=10, color='white')
#plt.scatter(gap1,te1, s=40, marker='o', edgecolor='black', linewidth='1.0', facecolor='white')
plt.axhline(y=31, xmin=0, xmax=8, linewidth=1, color = 'black',ls='dashed')
plt.axhline(y=42, xmin=0, xmax=8, linewidth=1, color = 'black',ls='dashed')
pylab.xticks(np.arange(0,10,2))
pylab.yticks(np.arange(30,70,10))
pylab.xlabel('Gap~(m)')
pylab.ylabel('Evacuation Time~(s)')
pylab.legend()
pylab.ylim(30, 60)
pylab.xlim(0, 8)
pylab.grid(True)   
'''
pylab.xlabel('x~(m)')
pylab.ylabel('y~(m)')
pylab.ylim(2, 18)
pylab.xlim(14, 20)
pylab.xticks(np.arange(14,22,2))
pylab.yticks(np.arange(2,20,4))
#pylab.show()
pylab.savefig('isobaras_g5.eps', format='eps', bbox_inches='tight')
