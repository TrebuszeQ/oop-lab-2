"""File for Throttle class."""
from logging import Logger, getLogger
from abstract_vehicle_part import AVehiclePart
from enum import Enum
from driving_cli.use_cases.validators import clamp_value

log: Logger = getLogger(__name__)


class Throttle(AVehiclePart):
    _throttle_value = None
    _step = None

    class Constants(Enum):
        MASS_KG: float = 500
        MIN_KG: float = 200
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

    def __init__(self, weight: float = None, step: float = None):
        super().__init__(weight)
        self._throttle_value = self.Constants.THROTTLE_MIN.value
        self._step: float = clamp_value(value=step,
                                        min_value=self.Constants.STEP_MIN.value,
                                        max_value=self.Constants.STEP_MAX.value,
                                        name="Step value")

    @classmethod
    def increase_throttle(cls):
        value: float = cls._status + cls._step
        cls._throttle_value = clamp_value(value=value,
                                          min_value=cls.Constants.THROTTLE_MIN.value,
                                          max_value=cls.Constants.THROTTLE_MAX.value,
                                          name="Throttle value")

    @classmethod
    def decrease_throttle(cls):
        value: float = cls._status - cls._step
        cls._throttle_value = clamp_value(value=value,
                                          min_value=cls.Constants.THROTTLE_MIN.value,
                                          max_value=cls.Constants.THROTTLE_MAX.value,
                                          name="Throttle value")