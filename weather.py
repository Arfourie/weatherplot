#read in all 7 files
#calculate the min,max avg for all four columns
#Plot a graph for each column, thus four graphs. With just avg min and max
#Will need three columns (min, max, avg) with data from Monday to Friday
#create index for a list
import numpy as np
import matplotlib.pyplot as pl
import glob
Alldays = glob.glob("*day.csv") #list all files with this extension. Save list to variable and loop through it
min1=np.zeros([7,4])
max1=np.zeros([7,4])
mean1=np.zeros([7,4])
i=0
j=0
for filename in Alldays:
    data=np.loadtxt(filename,delimiter = ",", skiprows=1, usecols=(1,2,3,4))
    datatr=np.transpose(data)
    j=0    
    for col in datatr:
        min1[i,j]=np.min(col)
        max1[i,j]=np.max(col)
        mean1[i,j]=np.mean(col)
        j=j+1
    i=i+1
           
print(min1)
days=np.arange(0,7,1)
pl.subplot(2,2,1)
pl.plot(days,min1[:,0],"r--")
pl.plot(days,max1[:,0],"r*")
pl.plot(days,mean1[:,0],"r-")
pl.title("Temp")
pl.legend(["min","max","mean"])

pl.subplot(2,2,2)
pl.plot(days,min1[:,1],"y--")
pl.plot(days,max1[:,1],"y*")
pl.plot(days,mean1[:,1],"y-")
pl.ylim(ymax = 1.4)
pl.title("Pressure")
pl.legend(["min","max","mean"])

pl.subplot(2,2,3)
pl.plot(days,min1[:,2],"g--")
pl.plot(days,max1[:,2],"g*")
pl.plot(days,mean1[:,2],"g-")
pl.ylim(ymax = 23)
pl.title("Wind")
pl.legend(["min","max","mean"])

pl.subplot(2,2,4)
pl.plot(days,min1[:,3],"g--")
pl.plot(days,max1[:,3],"g*")
pl.plot(days,mean1[:,3],"g-")
pl.title("Direction")
pl.legend(["min","max","mean"])

pl.show()


#OR
#data=[]
#for fname in files:
#    data.append(np.loadtxt(fname,delimiter=",",usecols(1,2,3,4)
#dailyavg=np.zeros(shape=(7,4))
#dailymax
