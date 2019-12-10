import matplotlib.pyplot as plt
import numpy as np
import time

#fig = plt.figure()
#fig.suptitle('No axes on this figure')  # Ad
#fig, ax_lst = plt.subplots(2, 2)

def my_plotter(ax,total_cityx,total_cityy,param_dict):
    global city1
    out = ax.plot(total_cityx,total_cityy, **param_dict)
    ax.annotate('1', city1,  xycoords='data',
                xytext=city1+.05,size=6,color='red')

    return(out)

city1 = np.array([2,3])
city2 = np.array([5,7])
city3 = np.array([1,1])
city4 = np.array([10,4])

x = np.array([])
y = np.array([])
x , y = np.split(city1,[1],axis=0)
x2 , y2 = np.split(city2,[1],axis=0)
x3 , y3 = np.split(city3,[1],axis=0)
figura , ax = plt.subplots(1,1)

total_cityx = np.concatenate((x,x2,x3), axis=0)
total_cityy = np.concatenate((y,y2,y3), axis=0)

\


my_plotter(ax,total_cityx,total_cityy,{'marker': 'o'})

plt.xlabel('x location')
plt.ylabel('y location')
plt.title("My first graph")

plt.legend()
plt.show()
