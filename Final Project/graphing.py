import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a = ([50,50,100],
     [50,50,80],
     [50,50,75],
     [50,50,50],
     [50,60,50],
     [50,60,30],
     [50,60,10],
     [50,40,50],
     [50,40,30],
     [50,40,10],
     [50,60,75],
     [50,75,60],
     [50,85,55],
     [50,40,75],
     [50,25,60],
     [50,15,55],
    )

#xyz=np.array(np.random.random((100,3)))
print(np.shape(a))
xyz = np.array(a)
x=xyz[:,0]
y=xyz[:,1]
z=xyz[:,2]

fig = plt.figure()


ax = fig.add_subplot(111, projection='3d')
ax.scatter(x,y,z)
pnt3d=ax.scatter(x,y,z,c=z)
cbar=plt.colorbar(pnt3d)
cbar.set_label("Values (units)")
plt.show()