from enum import Enum


class String:
    class Material(Enum):
        Nylon = 1
        Steel = 2
        Bronze = 3

        def rho(material):
            nylonRho = 1140
            steelRho = 7800
            bronzeRho = 8500
            if material == String.Material.Nylon:
                return nylonRho
            if material == String.Material.Steel:
                return steelRho
            if material == String.Material.Bronze:
                return bronzeRho
            raise ValueError("Invalid string material")

    def __init__(self, length, material, gauge):
        self.length = length
        self.material = material
        self.gauge = gauge


scaleLength = 123
lowTensionNylon = String(scaleLength, String.Material.Nylon, 0.001)
