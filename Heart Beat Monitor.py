#!/usr/bin/env python
# coding: utf-8

# In[1]:


#%matplotlib inline
import serial
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML
import heartpy as hp



print("hi")

# Parameters
x_len = 300         # Number of points to display
y_range = [0, 4096]  # Range of possible Y values to display

data=[]

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = list(range(0, 300))
ys = [0] * x_len
ax.set_ylim(y_range)

# Create a blank line. We will update the line in animate
line, = ax.plot(xs, ys)

# Add labels
plt.title('AD8323 ECG over Time')
plt.xlabel('Samples')
plt.ylabel('Data')

ser = serial.Serial('COM8', 9600, timeout=1) 
print(ser.is_open)


#c=0
# initialization function: plot the background of each frame
def init():
    line.set_ydata([])
    return line,
# This function is called periodically from FuncAnimation
def animate(i, ys):

    # Read temperature (Celsius) from TMP102
     
     #t0= time.time()
     #for x in range(9001): #check if last 1 empty   
    line2 = ser.readline()
     #t1= time.time()
     #tt=t1-t0
     #print(tt)
    n0 = line2.decode("ascii")
    # Add y to list
    if((n0!='')and(n0!='\n')):
        print(line2)
        n = int(line2.decode("ascii"))
        ys.append(n)
        data.append(n)
        
    #c=c+1
    # Limit y list to set number of items
    ys = ys[-x_len:]

    # Update line with new Y values
    line.set_ydata(ys)

    return line,

# Set up plot to call animate() function periodically
#t0= time.time()
flag= False
#while True:
inp = input("Please Enter Command, Sampling(S0150), Collecting Data(C0000), Report BPM(R0000): ")
if(inp.startswith('S')):
    ser.write(inp.encode())
    samp=int(inp.strip('S'))
    #print(samp)
else:
    if((inp!='C0000')and(inp!='R0000')):
        print("Wrong command please reenter")
    else:
        if(inp.startswith('R')):
             print("Report Not Working")
        if(inp.startswith('C')):
            flag=True
            ser.write(b'C0000')
            ani = animation.FuncAnimation(fig,
                animate,
                init_func=init,
                fargs=(ys,),
                frames = 9001, 
                interval = 6.7,
                blit=True)
#if(flag):
HTML(ani.to_html5_video())                       
#plt.show()
#t1= time.time()
#tt=t1-t0
#print(tt)
#print(c2)
#print("hii")
#ser.close()


# In[ ]:


ser.close()


# In[ ]:


import numpy as np
sample_rate=150.0
m=np.array(data)
print("before")
wd, m = hp.process(m, sample_rate)
print("After")
for measure in m.keys():
    print('%s: %f' %(measure, m[measure]))
#print(wd)
#print(m)


# In[ ]:





# In[ ]:




