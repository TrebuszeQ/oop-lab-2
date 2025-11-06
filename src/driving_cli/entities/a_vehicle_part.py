"""File for vehicle part and it's elements"""
from abc import ABC
from logging import getLogger, Logger
from enum import Enum

log: Logger = getLogger(__name__)


class AVehiclePart(ABC):
    _weight: float = None

    @property
    def weight(self) -> float:
        return self._weight

    @weight.setter
    def weight(self, value: float) -> None:
        self.weight = self._validate_weight(value)

    def __init__(self, weight: float):
        self._weight: float = weight

    @classmethod
    def _validate_weight(cls, weight) -> float:
        max_weight: float = cls.Constants.MASS_KG.value
        min_weight: float = cls.Constants.MIN_KG.value
        if weight > max_weight:
            log.warning("Vehicle part weight cannot be greater than: %s|", max_weight)
            log.warning("Vehicle part weight set to: %s|", max_weight)
            weight = max_weight
        elif weight < 0:
            log.warning("Vehicle part weight cannot be less than: %s|", min_weight)
            log.warning("Vehicle part weight set to: %s|", min_weight)
            weight = min_weight
        return weight

    @classmethod
    def constants(cls):
        return cls.Constants

    class Constants(Enum):
        MASS_KG = 0
        MIN_KG = 0