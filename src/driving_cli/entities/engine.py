"""File for Engine class."""
from logging import Logger, getLogger
from enum import Enum
log: Logger = getLogger(__name__)


class Engine:
    @property
    def weight(self) -> float:
        return self._weight

    @weight.setter
    def weight(self, value: float) -> None:
        self.weight = self._validate_weight(value)

    @property
    def acceleration(self) -> float:
        return self._acceleration

    @acceleration.setter
    def acceleration(self, value: float) -> None:
        self._acceleration = self._validate_acceleration(value)

    def __init__(self, weight: float,
                 acceleration: float):
        self._weight = self._validate_weight(weight)
        self._acceleration = self._validate_acceleration(acceleration)

    @classmethod
    def _validate_acceleration(cls, acceleration: float):
        max_value: float = cls.Constants.MAX_ACCELERATION.value
        min_value: float = cls.Constants.MIN_ACCELERATION.value

        if acceleration > max_value:
            log.warning("Throttle cannot be greater than: %s|", max_value)
            log.warning("Throttle set to: %s|", max_value)
            acceleration = max_value
        elif acceleration < min_value:
            log.warning("Throttle cannot be less than: %s|", min_value)
            log.warning("Throttle set to: %s|", min_value)
            acceleration = min_value
        return acceleration



    @classmethod
    def constants(cls):
        return cls.Constants

    class Constants(Enum):
        MASS_KG = 500
        MIN_KG = 10
        MIN_ACCELERATION: float = 0.1
        MAX_ACCELERATION: float = 1.0

