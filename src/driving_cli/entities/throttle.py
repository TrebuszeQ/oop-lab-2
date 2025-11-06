"""File for Throttle class."""
from logging import Logger, getLogger
from abstract_vehicle_part import AVehiclePart
from enum import Enum
log: Logger = getLogger(__name__)


class Throttle(AVehiclePart):

    def __init__(self, weight: float):
        super().__init__(weight)
        self._status: float = 0.0
        self._step: float = 0.1

    def increase_throttle(self):
        value: float = self._status + self._step
        self._status = self.__validate_throttle(value)

    def decrease_throttle(self, brake_step: float):
        value: float = self._status - brake_step
        self._status = self.__validate_throttle(value)

    def __validate_throttle(self, throttle: float):
        max_value: float = self.Constants.THROTTLE_MAX.value
        min_value: float = self.Constants.THROTTLE_MIN.value

        if throttle > max_value:
            log.warning("Throttle cannot be greater than: %s|", max_value)
            log.warning("Throttle set to: %s|", max_value)
            throttle = max_value
        elif throttle < min_value:
            log.warning("Throttle cannot be less than: %s|", min_value)
            log.warning("Throttle set to: %s|", min_value)
            throttle = min_value
        self._throttle = throttle
        return throttle

    class Constants(Enum):
        MASS_KG = 500
        MIN_KG = 200
        THROTTLE_MAX = 0
        THROTTLE_MIN = 0