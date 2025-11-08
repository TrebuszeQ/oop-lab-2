"""File for ABrake class."""
from logging import Logger, getLogger
from enum import Enum
from abc import ABC, abstractmethod

from driving_cli.entities.abstract_vehicle_part import AVehiclePart
from driving_cli.use_cases.validators import clamp_value

log: Logger = getLogger(__name__)


class Brake(AVehiclePart, ABC):
    _effectiveness = 0.0
    _brake_value = 0.0

    class Constants(Enum):
        BRAKE_EFFECTIVENESS_MIN = 0.0
        BRAKE_EFFECTIVENESS_MAX = 1.0
        BRAKE_VALUE_MAX = 1.0
        BRAKE_VALUE_MIN = 0.0
        WEIGHT_MIN = 1.0
        WEIGHT_MAX = 500.0

    @property
    def brake_effectiveness(self):
        return self._effectiveness

    @property
    def brake_value(self):
        return self._brake_value

    def __init__(self, weight: float = None, effectiveness: float = None):
        super().__init__(weight)
        self._brake_value = self.Constants.BRAKE_VALUE_MIN.value
        self.effectiveness = clamp_value(value=effectiveness,
                                         min_value=self.Constants.BRAKE_EFFECTIVENESS_MIN.value,
                                         max_value=self.Constants.BRAKE_EFFECTIVENESS_MAX.value,
                                         name="Brake effectiveness")

    @abstractmethod
    def engage_brake(self):
        value: float = self._brake_value + self._effectiveness
        self._brake_value = clamp_value(value=value,
                                        min_value=self.Constants.BRAKE_VALUE_MIN.value,
                                        max_value=self.Constants.BRAKE_VALUE_MAX.value,
                                        name="Brake value")

    @abstractmethod
    def disengage_brake(self):
        value: float = self._brake_value - self._effectiveness
        self._brake_value = clamp_value(value=value,
                                        min_value=self.Constants.BRAKE_VALUE_MIN.value,
                                        max_value=self.Constants.BRAKE_VALUE_MAX.value,
                                        name="Brake value")

    @abstractmethod
    def reset_brake(self):
        self._brake_value = self.Constants.BRAKE_VALUE_MIN.value