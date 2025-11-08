
"""File for vehicle part and it's elements"""
from abc import ABC
from logging import getLogger, Logger
from enum import Enum

from driving_cli.use_cases.validators import clamp_value

log: Logger = getLogger(__name__)


class AVehiclePart(ABC):
    _weight: float = None

    class Constants(Enum):
        WEIGHT_MAX: float = 1000.0
        WEIGHT_MIN: float = 1.0

    @property
    def weight(self) -> float:
        return self._weight

    @weight.setter
    def weight(self, value: float) -> None:
        self.weight = clamp_value(value=value,
                                  min_value=self.Constants.WEIGHT_MIN.value,
                                  max_value=self.Constants.WEIGHT_MAX.value,
                                  name="Vehicle part weight"
                                  )

    def __init__(self, weight: float = None):
        self._weight: float = weight

    @classmethod
    def constants(cls):
        return cls.Constants