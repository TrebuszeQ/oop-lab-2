"""File for Throttle class."""
from logging import Logger, getLogger
from abstract_vehicle_part import AVehiclePart
from enum import Enum
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
        self._step: float = self.__validate_step(step)

    @classmethod
    def increase_throttle(cls):
        value: float = cls._status + cls._step
        cls._status = cls.__validate_throttle_value(value)

    @classmethod
    def decrease_throttle(cls):
        value: float = cls._status - cls._step
        cls._status = cls.__validate_throttle_value(value)

    @classmethod
    def __validate_throttle_value(cls, throttle: float):
        max_value: float = cls.Constants.THROTTLE_MAX.value
        min_value: float = cls.Constants.THROTTLE_MIN.value
        param: str = "Throttle value"

        if throttle > max_value:
            log.warning("%s cannot be greater than: %s|", param, max_value)
            log.warning("%s set to: %s|", param, max_value)
            throttle = max_value
        elif throttle < min_value or throttle is None:
            log.warning("%s cannot be less than: %s|", param, min_value)
            log.warning("%s set to: %s|", param, min_value)
            throttle = min_value
        cls._throttle = throttle
        return throttle

    @classmethod
    def __validate_step(cls, throttle: float):
        max_value: float = cls.Constants.STEP_MAX.value
        min_value: float = cls.Constants.STEP_MIN.value
        param: str = "Throttle step"

        if throttle > max_value:
            log.warning("%s cannot be greater than: %s|", param, max_value)
            log.warning("%s set to: %s|",param, max_value)
            throttle = max_value
        elif throttle < min_value:
            log.warning("%s cannot be less than: %s|", param, min_value)
            log.warning("%s set to: %s|", param, min_value)
            throttle = min_value
        cls._throttle = throttle
        return throttle