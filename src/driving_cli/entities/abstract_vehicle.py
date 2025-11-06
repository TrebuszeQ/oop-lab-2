"""File for Car class and its complements."""
from abc import ABC
from enum import Enum
from logging import Logger, getLogger
from throttle import Throttle
from brake import Brake

log: Logger = getLogger(__name__)


class AVehicle(ABC):
    """
    Abstract vehicle class.
    """
    _weight = None
    _speed = None
    _acceleration = None
    _throttle = None
    _brake = None

    @property
    def weight(self) -> float:
        return self._weight

    @weight.setter
    def weight(self, value: float) -> None:
        self.weight = self._validate_weight(value)

    @property
    def speed(self) -> float:
        return self._speed

    @property
    def acceleration(self) -> float:
        return self._acceleration

    @acceleration.setter
    def acceleration(self, value: float) -> None:
        self._acceleration = self._validate_acceleration(value)

    def __init__(self, weight: float, acceleration: float, throttle: Throttle, brake: Brake):
        self._weight: float = self._validate_weight(weight)
        self._speed: float = 0
        self._acceleration: float = self._validate_acceleration(acceleration)
        self._throttle: Throttle = throttle
        self._brake: Brake = brake

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
    def _validate_speed(cls, speed) -> float:
        max_speed: float = cls.Constants.MAX_SPEED_KHM.value
        min_speed: float = cls.Constants.MIN_SPEED.value
        if speed > max_speed:
            log.warning("Vehicle speed is greater than: %s|", max_speed)
            log.warning("Vehicle speed set to: $s|", max_speed)
            speed = max_speed
        elif speed < 0:
            log.warning("Vehicle speed cannot be less than: %s|", min_speed)
            log.warning("Vehicle speed set to: $s|", max_speed)
        return speed

    @classmethod
    def _validate_weight(cls, weight) -> float:
        max_weight: float = cls.Constants.MASS_KG.value
        min_weight: float = cls.Constants.MIN_KG.value
        if weight > max_weight:
            log.warning("Vehicle weight cannot be greater than: %s|", max_weight)
            log.warning("Vehicle weight set to: %s|", max_weight)
            weight = max_weight
        elif weight < 0:
            log.warning("Vehicle weight cannot be less than: %s|", min_weight)
            log.warning("Vehicle weight set to: %s|", min_weight)
            weight = min_weight
        return weight

    @classmethod
    def constants(cls):
        return cls.Constants


    def accelerate(self) -> None:
        """Increases speed using throttle."""
        new_speed: float = self._speed * self._throttle.status
        self._speed = self._validate_speed(new_speed)

    def brake(self) -> None:
        """Apply brakes."""

        new_speed = self._speed - self._brake.status
        self._speed = self._validate_speed(new_speed)

    class Constants(Enum):
        MAX_SPEED_KHM = 80
        MIN_SPEED = 0
        MASS_KG = 5000
        MIN_KG = 200
        THROTTLE_MAX = 0
        THROTTLE_MIN = 0
        MIN_ACCELERATION: float = 0.1
        MAX_ACCELERATION: float = 1.0