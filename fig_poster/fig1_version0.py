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

### DATA

data1 = np.genfromtxt('gap_vs_te_225_v4.txt', delimiter = '   ')
gap1=data1[:,0]
te1=data1[:,1]/159
yerr1=data1[:,2]/159
for i in range(0,len(yerr1)):
	if (i+1)%5 != 0:
		yerr1[i]=0

data2 = np.genfromtxt('gap_vs_te_30x30.txt', delimiter = '   ')
gap2=data2[:,0]
te2=data2[:,1]/529
yerr2=data2[:,2]/529

data3 = np.genfromtxt('gap_vs_te_40x40.txt', delimiter = '   ')
gap3=data3[:,0]
te3=data3[:,1]/864
yerr3=data3[:,2]/864
for i in range(0,len(yerr3)/2):
	yerr3[2*i]=0

### PLOT

pylab.figure(1)
pylab.clf()


plt.plot(gap3,te3,'ro',label='N=961',markersize=7,zorder=3) 
plt.plot(gap3,te3,'k',lw=1.0,zorder=2)     
plt.errorbar(gap3,te3,yerr3,linestyle='-',marker='.',color='k') 

plt.plot(gap2,te2,'ys',label='N=583',markersize=7,zorder=3) 
plt.plot(gap2,te2,'k',lw=1.0,zorder=2)
plt.errorbar(gap2,te2,yerr2,linestyle='-',marker='.',color='k')

plt.plot(gap1,te1,'b^',label='N=225',markersize=7,zorder=3) 
plt.plot(gap1,te1,'k',lw=1.0,zorder=2) 
plt.errorbar(gap1,te1,yerr1,linestyle='-',fmt='.',color='w',ecolor='k',zorder=1) 
   
pylab.xticks(np.arange(0,8,2))
pylab.yticks(np.arange(0.2,0.8,0.1))
pylab.xlabel('Gap~(m)')
pylab.ylabel('Evacuation time$\,/\,$N~(s)')
pylab.legend()
pylab.ylim(0.2, 0.5)
pylab.xlim(0, 6)

lgd=plt.legend(numpoints=1,prop={'size':5.5}) 
lgd.set_visible(False)
   
pylab.savefig('fig1_version0.eps', format='eps', dpi=300, bbox_inches='tight')


