import matplotlib.pyplot as plt
import csv 
import numpy as np
from pylab import *
from matplotlib.font_manager import FontProperties

x=[]
y=[]
n=[]
i=0


with open ('THE15-16.csv','rt') as csvfile:
	plots= csv.reader(csvfile,delimiter=',')
	for row in plots:
			#print i,row
			#i=i+1
			
		n.append(row[0])
		x.append(float(row[1]))
		y.append(float(row[2]))
			
fig, ax=plt.subplots()
ax.scatter(x,y, label='Ranking')
ax.set_xlim(xmin=0)
ax.set_ylim(ymin=0)
	
m, b = np.polyfit(x, y, 1)

plt.plot(x, y, '.')
l1=plt.plot(x, m*np.array(x) + b, '-')
plt.xlabel('THE15', fontsize=16)
plt.ylabel('THE16', fontsize=16)
setp(l1,linewidth=2)
plt.plot([0, 500], [0, 500], 'r', lw=1)
	#text(0.1, 0.9,'R^2=0.542', horizontalalignment='center', verticalalignment='center',transform = ax.transAxes)
plt.show()

