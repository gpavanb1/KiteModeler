import material_dicts as md


class Composition:
    def __init__(self, surface, frame, tail, line):
        self.surface = md.SurfaceMaterials[surface]
        self.frame = md.FrameMaterials[frame]
        self.tail = md.TailMaterials[tail]
        self.line = md.LineMaterials[line]
