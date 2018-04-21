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
          'legend.fontsize': 8,
          'figure.dpi': 300,
          'figure.figsize': fig_size,
          'savefig.dpi': 300,
         }

pylab.rcParams.update(params)
#################### DATA ##############################


data = np.genfromtxt('gap_vs_te_225_v4.txt', delimiter = '   ')
gap=data[:,0]
te=data[:,1]
yerr=data[:,2]
#for i in range(0,len(yerr)/4):
#	yerr[4*i]=0
yerr[::4]=0
yerr[1::8]=0
#yerr[2::4]=0
#yerr[3::4]=0
#print(yerr)

data2 = np.genfromtxt('gap_vs_te_v8.txt', delimiter = '   ')
gap2=data2[:,0]
te2=data2[:,1]
yerr2=data2[:,2]
for i in range(1,len(yerr2)/2):
     yerr2[2*i]=0
#print(yerr)

#################### PLOT specification ##############################
pylab.figure(1)
pylab.clf()

plt.plot(gap2,te2,'rs',markersize=7,label='$v_d=$ 8~m/s',zorder=3) 
plt.plot(gap2,te2,'k',lw=1.0,zorder=2)     
#plt.errorbar(gap2,te2,yerr2,linestyle='-',marker='.',color='k') 

plt.plot(gap[::3],te[::3],'bo',markersize=8,label='$v_d=$ 4~m/s',zorder=3) 
plt.plot(gap[::3],te[::3],'k',lw=1.0,zorder=2)     
#plt.errorbar(gap[::3],te[::3],yerr[::3],linestyle='-',marker='.',color='k')

  
pylab.xticks(np.arange(0,20,2))
pylab.yticks(np.arange(30,70,10))
pylab.xlabel('Gap~(m)')
pylab.ylabel('Evacuation Time~(s)')
pylab.legend()
pylab.ylim(28,60)
pylab.xlim(-0.2, 10)
lgd=plt.legend(numpoints=1,prop={'size':6},loc=4) 
lgd.set_visible(False)  
pylab.savefig('gap_vste_225_v4_v8.eps', format='eps', dpi=600, bbox_inches='tight')
