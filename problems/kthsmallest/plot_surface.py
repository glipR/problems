from mayavi import mlab
import numpy as np

# with open("data_log_sol_dynamic_march.csv", "r") as file:
#     lines = list(map(lambda x: list(map(float, x.split(","))), list(file.readlines())[1:]))

k = np.array([[1]*4, [3]*4, [9]*4, [27]*4])
r = np.array([[1, 2, 3, 4] for _ in range(4)])
Q = np.array([[1, 2, 3, 4], [1, 4, 9, 16], [1, 8, 27, 64], [1, 16, 81, 256]])

k2 = np.array([[1]*4, [3]*4, [9]*4, [27]*4])
r2 = np.array([[1, 2, 3, 4] for _ in range(4)])
Q2 = np.array([[1, 2, 3, 4][::-1], [1, 4, 9, 16][::-1], [1, 8, 27, 64][::-1], [1, 16, 81, 256][::-1]])

fig = mlab.figure()

s1 = mlab.surf(k, r, Q)
s2 = mlab.surf(k2, r2, Q2)

ax_ranges = [0, 30, 0, 4, 0, 256]
ax_scale = [1.0, 1.0, 0.4]
ax_extent = ax_ranges * np.repeat(ax_scale, 2)

s1.actor.actor.scale = ax_scale
s2.actor.actor.scale = ax_scale

mlab.view(60, 74, 17, [-2.5, -4.6, -0.3])
mlab.outline(s1, color=(.7, .7, .7), extent=ax_extent)
mlab.axes(s1, color=(.7, .7, .7), extent=ax_extent, ranges=ax_ranges, xlabel='x', ylabel='y', zlabel='z')



# Matplotlib doesn't render multiple overlapping surfaces well.
# fig = plt.figure(figsize=(14, 9))
# ax = plt.axes(projection='3d')
# surf = ax.plot_surface(k, r, Q)
# surf2 = ax.plot_surface(k2, r2, Q2)
# fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

# ax.set_title("Surface plot")

# plt.show()
