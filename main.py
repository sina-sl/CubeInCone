import numpy as np
from point import Point3D
from matplotlib import pyplot as plt

dz = 0.5
point_0 = Point3D(100, 250, 0)
min_point = Point3D(0, 0, 0)
max_point = Point3D(500, 500, 500)
factor_z = np.tan(np.deg2rad(10))
rotation_y = np.deg2rad(-60)
rotation_z = np.deg2rad(0)


def cone(z_arr) -> list:
    data = list()
    for z in z_arr:
        teta = z
        point = Point3D(
            x=z * factor_z * np.cos(teta) + point_0.x,
            y=z * factor_z * np.sin(teta) + point_0.y,
            z=z + point_0.z
        )
        point = point.rotation_y(point_0, rotation_y)
        point = point.rotation_z(point_0, rotation_z)

        if point.inRange(min_point=min_point, max_point=max_point, precision_range=dz):
            data.append(point)

    return data


z_list = np.arange(min_point.z, max_point.z, dz)
axis = cone(z_list)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim3d(min_point.x, max_point.x)
ax.set_ylim3d(min_point.y, max_point.y)
ax.set_zlim3d(min_point.z, max_point.z)

ax.scatter3D(
    list(map(lambda point: point.x, axis)),
    list(map(lambda point: point.y, axis)),
    list(map(lambda point: point.z, axis)),
    linewidths=1
)

plt.show()
