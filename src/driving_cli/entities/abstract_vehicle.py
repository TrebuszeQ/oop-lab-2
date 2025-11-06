"""File for Car class and its complements."""
from abc import ABC
from enum import Enum
from logging import Logger, getLogger
from throttle import Throttle
from brake import Brake
from engine import Engine

log: Logger = getLogger(__name__)


class AVehicle(ABC):
    """
    Abstract vehicle class.
    """
    _speed = None
    _throttle = None
    _brake = None
    _engine = None


    @property
    def speed(self) -> float:
        return self._speed

    @property
    def throttle(self) -> Throttle:
        return self._throttle

    @property
    def brake(self) -> Brake:
        return self._brake

    @property
    def engine(self) -> Engine:
        return self._engine


    def __init__(self, weight: float,
                 throttle: Throttle,
                 brake: Brake,
                 engine: Engine):
        self._weight: float = self._validate_weight(weight)
        self._speed: float = 0
        self._throttle: Throttle = throttle
        self._brake: Brake = brake
        self._engine: Engine = engine

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

    def apply_brake(self) -> None:
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