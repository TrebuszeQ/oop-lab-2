"""File for AThrottle class."""
from logging import Logger, getLogger
from abc import ABC, abstractmethod
from enum import Enum

from driving_cli.entities.abstracts.abstract_vehicle_part import AVehiclePart
from driving_cli.use_cases.validators import clamp_value

log: Logger = getLogger(__name__)


class AThrottle(AVehiclePart, ABC):
    _throttle_value = 0.0
    _step = 0.0

    class Constants(Enum):
        WEIGHT_MIN = 1.0
        WEIGHT_MAX = 1000.0
        THROTTLE_MAX: float = 1.0
        THROTTLE_MIN: float = 0.0
        STEP_MAX: float = 1.0
        STEP_MIN: float = 0.0

    @property
    def throttle_value(self):
        """Current value of throttle"""
        return self._throttle_value

    @property
    def step(self):
        """Throttle step value."""
        return self._step

    def __init__(self, weight: float = None,
                 step: float = None):
        super().__init__(weight)
        self._throttle_value = self.Constants.THROTTLE_MIN.value
        self._step: float = clamp_value(value=step,
                                        min_value=self.Constants.STEP_MIN.value,
                                        max_value=self.Constants.STEP_MAX.value,
                                        name="Step value")

    @abstractmethod
    def increase_throttle(self):
        """Increases throttle by a step."""
        self.reset_throttle()
        value: float = self._throttle_value + self._step
        self._throttle_value = clamp_value(value=value,
                                           min_value=self.Constants.THROTTLE_MIN.value,
                                           max_value=self.Constants.THROTTLE_MAX.value,
                                           name="Throttle value")

    @abstractmethod
    def decrease_throttle(self):
        """Decreases throttle by a step."""
        value: float = self._throttle_value - self._step
        self._throttle_value = clamp_value(value=value,
                                           min_value=self.Constants.THROTTLE_MIN.value,
                                           max_value=self.Constants.THROTTLE_MAX.value,
                                           name="Throttle value")

    @abstractmethod
    def reset_throttle(self):
        self._throttle_value = self.Constants.THROTTLE_MIN.value