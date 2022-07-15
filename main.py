import math

import numpy as np
from coneCreator import ConeCreator
from point import Point3D
from matplotlib import pyplot as plt
from progress.bar import Bar


dz = 10
theta = np.deg2rad(45)
alpha = np.deg2rad(45)
point_0 = Point3D(0, 0, 0)
min_point = Point3D(0, 0, 0)
max_point = Point3D(500, 500, 500)
factor_z = np.tan(np.deg2rad(10))

cube_size_x = 15
cube_size_y = 15
cube_size_z = 15



def findEquivalentCubeOfPoint(point: Point3D) -> Point3D:
    index_x = math.floor(point.x / cube_size_x)
    index_y = math.floor(point.y / cube_size_y)
    index_z = math.floor(point.z / cube_size_z)

    return Point3D(index_x, index_y, index_z)



def plotPoint3D(points: list):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim3d(min_point.x, max_point.x)
    ax.set_ylim3d(min_point.y, max_point.y)
    ax.set_zlim3d(min_point.z, max_point.z)

    xs = list(map(lambda point: point.x, points))
    ys = list(map(lambda point: point.y, points))
    zs = list(map(lambda point: point.z, points))

    ax.scatter3D(xs, ys, zs, linewidths=1)

    plt.show()
    pass


def plotCubes(cube_indexes: list):
    data = np.empty([
        int((max_point.x - min_point.x)/cube_size_x),  # x cube count
        int((max_point.y - min_point.y)/cube_size_y),  # y cube count
        int((max_point.z - min_point.z)/cube_size_z)   # z cube count
    ], dtype=bool)

    data[:][:][:] = False

    for index in cube_indexes:
        data[index.x][index.y][index.z] = True

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.voxels(data)
    plt.show()
    pass


def writeToFile(cube_indexes: list, file_name: str):
    file = open(file_name, "w")
    file.writelines(f'{len(cube_indexes)}\n')

    pr = Bar('writing include cube index', max=len(cube_indexes), check_tty=False)

    for point in cube_indexes:
        file.writelines(f'{point.x} {point.y} {point.z}\n')
        pr.next()

    pr.finish()
    file.close()
    pass



def main():
    z_list = np.arange(min_point.z, max_point.z, dz)
    cone_axis = ConeCreator().circular(
        z_arr=z_list,
        theta=theta,
        alpha=alpha,
        z_factor=factor_z,
        base_point=point_0,
        max_point=max_point,
        min_point=min_point,
        precision_range=dz
    )

    cube_indexes = [findEquivalentCubeOfPoint(point) for point in cone_axis]
    writeToFile(cube_indexes, 'cubeIndexes.txt')

    # plotPoint3D(cone_axis)
    plotCubes(cube_indexes)
    pass


if __name__ == '__main__':
    main()
