from enum import Enum


class Material(Enum):
    Nylon = 1
    Steel = 2
    Bronze = 3

    def rho(material):
        nylonRho = 1140
        steelRho = 7800
        bronzeRho = 8500
        if material == Material.Nylon:
            return nylonRho
            if material == Material.Steel:
                return steelRho
            if material == Material.Bronze:
                return bronzeRho
            raise ValueError("Invalid string material")
