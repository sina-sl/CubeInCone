import numpy as np

from point import Point3D
from progress.bar import Bar


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

        pr = Bar('computing cone points by spiral method', max=len(z_arr), check_tty=False)

        data = list()
        for z in z_arr:
            point = self.calculateConePointByZ(
                z=z,
                theta=z,
                z_factor=z_factor,
                base_point=base_point
            )

            point = point.rotation_y(base_point, theta).rotation_z(base_point, alpha)

            if point.inRange(min_point=min_point, max_point=max_point, precision_range=0):
                data.append(point)

            pr.next()
        pr.finish()
        return data



    def circular(self, z_arr: list, z_factor: float, base_point: Point3D, theta: float, alpha: float,
                 max_point: Point3D, min_point: Point3D, precision_range: float) -> list:

        pr = Bar('computing cone points by circular method', max=len(z_arr), check_tty=False)

        data = list()
        for z in z_arr:
            theta_factor = z / precision_range
            theta_count = int(360 * theta_factor)

            for theta_index in range(theta_count):
                point = self.calculateConePointByZ(
                    base_point=base_point,
                    z_factor=z_factor,
                    theta=theta_index / theta_factor,
                    z=z,
                )

                point = point.rotation_y(base_point, theta).rotation_z(base_point, alpha)

                if point.inRange(min_point=min_point, max_point=max_point, precision_range=precision_range):
                    data.append(point)

            pr.next()
        pr.finish()
        return data
