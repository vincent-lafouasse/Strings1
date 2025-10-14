from Material import Material
from enum import Enum


class TensionRating(Enum):
    Low = 1
    Medium = 2
    High = 3


class String:
    def __init__(self, length, material, gauge):
        self.length = length
        self.material = material
        self.gauge = gauge

    def parse(args):
        material = args.material.lower()
        try:
            material = Material.fromString(material)
        except ValueError as e:
            raise e

        tension = args.tension.lower()
        if tension == "low":
            tension = TensionRating.Low
        elif tension == "medium":
            tension = TensionRating.Medium
        elif tension == "high":
            tension = TensionRating.High
        else:
            raise ValueError(f"Invalid tension: {tension}")
