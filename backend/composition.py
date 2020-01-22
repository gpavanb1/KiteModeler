from .material_dicts import SurfaceMaterials, FrameMaterials, TailMaterials, LineMaterials


class Composition:
    def __init__(self, surface, frame, tail, line):
        self.surface = SurfaceMaterials[surface]
        self.frame = FrameMaterials[frame]
        self.tail = TailMaterials[tail]
        self.line = LineMaterials[line]
