from enum import Enum


class Material(Enum):
    Nylon = 1
    Steel = 2
    Bronze = 3

    def fromString(s):
        if s == "nylon":
            return Material.Nylon
        elif s == "steel":
            return Material.Steel
        elif s == "bronze":
            return Material.Bronze
        else:
            raise ValueError(f"Invalid string material: {s}")

    def rho(material):
        nylonRho = 1140
        steelRho = 7800
        bronzeRho = 8500
        if material == Material.Nylon:
            return nylonRho
        elif material == Material.Steel:
            return steelRho
        elif material == Material.Bronze:
            return bronzeRho
        else:
            raise ValueError("Invalid string material")
