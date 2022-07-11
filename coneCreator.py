import numpy as np

from point import Point3D


class ConeCreator:

    def calculateConePointByZ(self, z: float, z_factor: float, theta: float, base_point: "Point3D") -> "Point3D":
        point = Point3D(
            x=z * z_factor * np.cos(theta) + base_point.x,
            y=z * z_factor * np.sin(theta) + base_point.y,
            z=z + base_point.z
        )
        return point

    def spiral(self, z_arr: list, z_factor: float, base_point: Point3D, theta: float, alpha: float,
               max_point: Point3D, min_point: Point3D, precision_range: float) -> list:

        data = list()
        for z in z_arr:
            point = self.calculateConePointByZ(
                z=z,
                theta=z,
                z_factor=z_factor,
                base_point=base_point
            )

            point = point.rotation_y(base_point, theta).rotation_z(base_point, alpha)

            if point.inRange(min_point=min_point, max_point=max_point, precision_range=precision_range):
                data.append(point)

        return data


    def circular(self, z_arr: list, z_factor: float, base_point: Point3D, theta: float, alpha: float,
               max_point: Point3D, min_point: Point3D, precision_range: float) -> list:

        data = list()
        for z in z_arr:
            for inner_theta in range(360):
                point = self.calculateConePointByZ(
                    base_point=base_point,
                    theta=inner_theta,
                    z=z * z_factor,
                )

                point.rotation_y(base_point, theta).rotation_z(base_point, alpha)

                if point.inRange(min_point=min_point, max_point=max_point, precision_range=precision_range):
                    data.append(point)

        return data
