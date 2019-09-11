from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()

ax = fig.gca(projection='3d')
ax.scatter(verts[:,0],verts[:,1],verts[:,2],label='blob:'+str(selected_cell), c=np.random.rand(len(verts)))
ax.legend()

plt.show()
