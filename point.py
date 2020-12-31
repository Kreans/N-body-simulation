class Point(object):
    def __init__(self, coords: list, m: float, v: list):
        self.coords = coords
        self.m = m
        self.v = v

    def __repr__(self):
        return f"Point({self.coords}, {self.m}, {self.v})"
