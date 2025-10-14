from enum import Enum
import argparse
import sys


class TensionRating(Enum):
    Low = 1
    Medium = 2
    High = 3


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

    def fromArgs(args):
        material = args.material.lower()
        if material == "nylon":
            material = String.Material.Nylon
        elif material == "steel":
            material = String.Material.Steel
        elif material == "bronze":
            material = String.Material.Bronze
        else:
            raise ValueError(f"Invalid string material: {material}")

        tension = args.tension.lower()
        if tension == "low":
            tension = TensionRating.Low
        elif tension == "medium":
            tension = TensionRating.Medium
        elif tension == "high":
            tension = TensionRating.High
        else:
            raise ValueError(f"Invalid tension: {tension}")


def main():
    parser = argparse.ArgumentParser(description="Plink plonk")

    parser.add_argument(
        "--material",
        "-m",
        help="Material, can be Nylon, Steel or Bronze",
        required=True,
    )
    parser.add_argument(
        "--tension",
        "-t",
        help="String tension rating, can be Low, Medium or High",
        default="Medium",
    )

    args = parser.parse_args()

    try:
        string = String.fromArgs(args)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    print(string)


if __name__ == "__main__":
    main()
