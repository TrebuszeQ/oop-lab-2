"""File for vehicle part and it's elements"""
from abc import ABC
from logging import getLogger, Logger
from enum import Enum

log: Logger = getLogger(__name__)


class AVehiclePart(ABC):
    _weight: float = None
    _status: float = None

    @property
    def throttle_value(self):
        return self._status

    @property
    def step(self):
        return self._status

    @property
    def weight(self) -> float:
        return self._weight

    @weight.setter
    def weight(self, value: float) -> None:
        self.weight = self._validate_weight(value)

    def __init__(self, weight: float = None):
        self._weight: float = weight
        self._status = 0.0

    @classmethod
    def _validate_weight(cls, weight) -> float:
        max_weight: float = cls.Constants.MASS_KG.value
        min_weight: float = cls.Constants.MIN_KG.value

        if weight > max_weight:
            log.warning("Vehicle part weight cannot be greater than: %s", max_weight)
            log.warning("Vehicle part weight set to: %s", max_weight)
            weight = max_weight
        elif weight < 0 or weight is None:
            log.warning("Vehicle part weight cannot be less than: %s", min_weight)
            log.warning("Vehicle part weight set to: %s", min_weight)
            weight = min_weight
        return weight

    @classmethod
    def constants(cls):
        return cls.Constants

    class Constants(Enum):
        STATUS_MIN: float = 0.0
        STATUS_MAX: float = 0.0
        MASS_KG: float = 0.0
        MIN_KG: float = 0.0