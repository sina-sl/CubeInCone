import numpy as np


class Point3D:
    x: float
    y: float
    z: float

    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        self.x = x
        self.y = y
        self.z = z

    def inRangeX(self, x_min: float, x_max: float, precision_range: float) -> bool:
        return x_min - precision_range <= self.x <= x_max + precision_range

    def inRangeY(self, y_min: float, y_max: float, precision_range: float) -> bool:
        return y_min - precision_range <= self.y <= y_max + precision_range

    def inRangeZ(self, z_min: float, z_max: float, precision_range: float) -> bool:
        return z_min - precision_range <= self.z <= z_max + precision_range

    def inRange(self, min_point: "Point3D", max_point: "Point3D", precision_range: float):
        return (
                self.inRangeX(min_point.x, max_point.x, precision_range) and
                self.inRangeY(min_point.y, max_point.y, precision_range) and
                self.inRangeZ(min_point.z, max_point.z, precision_range)
        )

    def rotation_y(self, point_0: "Point3D", rotation_deg: float) -> "Point3D":
        return Point3D(
            x=(self.x - point_0.x) * np.cos(rotation_deg) + (self.z - point_0.z) * np.sin(rotation_deg) + point_0.x,
            z=(self.z - point_0.z) * np.cos(rotation_deg) - (self.x - point_0.x) * np.sin(rotation_deg) + point_0.z,
            y=self.y
        )

    def rotation_z(self, point_0: "Point3D", rotation_deg: float) -> "Point3D":
        return Point3D(
            y=(self.y - point_0.y) * np.cos(rotation_deg) + (self.x - point_0.x) * np.sin(rotation_deg) + point_0.y,
            x=(self.x - point_0.x) * np.cos(rotation_deg) - (self.y - point_0.y) * np.sin(rotation_deg) + point_0.x,
            z=self.z
        )

    def rotation_x(self, point_0: "Point3D", rotation_deg: float) -> "Point3D":
        return Point3D(
            y=(self.y - point_0.y) * np.cos(rotation_deg) - (self.z - point_0.z) * np.sin(rotation_deg) + point_0.y,
            z=(self.z - point_0.z) * np.cos(rotation_deg) + (self.y - point_0.y) * np.sin(rotation_deg) + point_0.z,
            x=self.x
        )


    def __str__(self):
        return f'x:{self.x} y:{self.y} z:{self.z}'

    pass
