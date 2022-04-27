import numpy as np


class PolygonBase:

    def __init__(self, points):
        self.x = points[..., 0]
        self.y = points[..., 1]
        self.z = points[..., 2]
        self.points = np.asarray(zip(self.x, self.y, self.z))


class HierarchicalPolygon:
    ...
