"""File for Throttle class."""
from logging import Logger, getLogger
from abstract_vehicle_part import AVehiclePart
from enum import Enum
log: Logger = getLogger(__name__)


class Throttle(AVehiclePart):
    _acceleration = None

    @property
    def acceleration(self):
        return self._acceleration

    def __init__(self, weight: float, acceleration: float):
        super().__init__(weight)
        self._acceleration: float = self.__validate_acceleration(acceleration)

    @classmethod
    def increase_throttle(cls):
        value: float = cls._status + cls._acceleration
        cls._status = cls.__validate_throttle(value)

    @classmethod
    def decrease_throttle(cls, brake_step: float):
        value: float = cls._status - brake_step
        cls._status = cls.__validate_throttle(value)

    @classmethod
    def __validate_throttle(cls, throttle: float):
        max_value: float = cls.Constants.THROTTLE_MAX.value
        min_value: float = cls.Constants.THROTTLE_MIN.value
        param: str = "Throttle"

        if throttle > max_value:
            log.warning("%s cannot be greater than: %s|", param, max_value)
            log.warning("%s set to: %s|", param, max_value)
            throttle = max_value
        elif throttle < min_value:
            log.warning("%s cannot be less than: %s|", param, min_value)
            log.warning("%s set to: %s|", param, min_value)
            throttle = min_value
        cls._throttle = throttle
        return throttle

    @classmethod
    def __validate_acceleration(cls, throttle: float):
        max_value: float = cls.Constants.ACCELERATION_MAX.value
        min_value: float = cls.Constants.ACCELERATION_MIN.value
        param: str = "Acceleration"

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

    class Constants(Enum):
        MASS_KG: float = 500
        MIN_KG: float = 200
        THROTTLE_MAX: float = 1.0
        THROTTLE_MIN: float = 0.0
        ACCELERATION_MAX: float = 1.0
        ACCELERATION_MIN: float = 0.0