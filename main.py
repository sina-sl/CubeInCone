import math

import numpy as np
from coneCreator import ConeCreator
from point import Point3D
from matplotlib import pyplot as plt

dz = 0.5
theta = np.deg2rad(45)
alpha = np.deg2rad(45)
point_0 = Point3D(0, 0, 0)
min_point = Point3D(0, 0, 0)
max_point = Point3D(500, 500, 500)
factor_z = np.tan(np.deg2rad(10))

cube_size_x = dz
cube_size_y = dz
cube_size_z = dz


def findEquivalentCubeOfPoint(point: Point3D) -> Point3D:
    index_x = math.floor(point.x / cube_size_x)
    index_y = math.floor(point.y / cube_size_y)
    index_z = math.floor(point.z / cube_size_z)

    return Point3D(index_x, index_y, index_z)


def main():
    z_list = np.arange(min_point.z, max_point.z, dz)
    cone_axis = ConeCreator().spiral(
        z_arr=z_list,
        theta=theta,
        alpha=alpha,
        z_factor=factor_z,
        base_point=point_0,
        max_point=max_point,
        min_point=min_point,
        precision_range=dz
    )

    axes = [
        math.ceil((max_point.x - min_point.x) / cube_size_x),  # x count
        math.ceil((max_point.y - min_point.y) / cube_size_y),  # y count
        math.ceil((max_point.z - min_point.z) / cube_size_z),  # z count
    ]

    data = np.empty([100, 1000, 1000], dtype=bool)

    data[:][:][:] = False

    indexes = [findEquivalentCubeOfPoint(point) for point in cone_axis]
    for index in indexes[:100]:
        if index.z >= 0 and index.x >= 0 and index.y >= 0:
            data[index.x][index.y][index.z] = True

    # Plot figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Voxels is used to customizations of the
    # sizes, positions and colors.
    ax.voxels(data)
    plt.show()

    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    # ax.set_xlim3d(0, axes[0])
    # ax.set_ylim3d(0, axes[1])
    # ax.set_zlim3d(0, axes[2])
    #
    # ax.scatter3D(
    #     list(map(lambda point: point.x, indexes)),
    #     list(map(lambda point: point.y, indexes)),
    #     list(map(lambda point: point.z, indexes)),
    #     linewidths=1
    # )
    #
    # plt.show()


if __name__ == '__main__':
    main()
