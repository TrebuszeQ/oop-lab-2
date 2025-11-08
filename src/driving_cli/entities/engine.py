"""File for Engine class."""
from logging import Logger, getLogger
from enum import Enum
from abstract_vehicle_part import AVehiclePart

log: Logger = getLogger(__name__)


class Engine(AVehiclePart):
    _acceleration: float = 0.0
    _combustion: float = 0.0

    @property
    def acceleration(self) -> float:
        return self._acceleration

    @property
    def combustion(self) -> float:
        return self._combustion

    @acceleration.setter
    def acceleration(self, value: float) -> None:
        self._acceleration = self._validate_acceleration(value)

    def __init__(self, weight: float = None, acceleration: float = None, combustion: float = None):
        super().__init__(weight)
        self._acceleration = self._validate_acceleration(acceleration)
        self._combustion = self._validate_combustion(combustion)

    @classmethod
    def _validate_acceleration(cls, acceleration: float):
        max_value: float = cls.Constants.ACCELERATION_MAX.value
        min_value: float = cls.Constants.ACCELERATION_MIN.value
        param: str = "Acceleration"

        if acceleration > max_value:
            log.warning("%s cannot be greater than: %s|", param, max_value)
            log.warning("%s set to: %s|", param, max_value)
            acceleration = max_value
        elif acceleration < min_value or acceleration is None:
            log.warning("%s cannot be less than: %s|", param, min_value)
            log.warning("%s set to: %s|", param, min_value)
            acceleration = min_value
        return acceleration

    @classmethod
    def _validate_combustion(cls, combustion: float):
        max_value: float = cls.Constants.COMBUSTION_MAX.value
        min_value: float = cls.Constants.COMBUSTION_MIN.value
        param: str = "Combustion"

        if combustion > max_value:
            log.warning("%s cannot be greater than: %s|", param, max_value)
            log.warning("%s set to: %s|", param, max_value)
            combustion = max_value
        elif combustion < min_value or combustion is None:
            log.warning("%s cannot be less than: %s|", param, min_value)
            log.warning("%s set to: %s|", param, min_value)
            combustion = min_value
        return combustion

    @classmethod
    def constants(cls):
        return cls.Constants

    class Constants(Enum):
        MASS_KG = 500
        MIN_KG = 10
        ACCELERATION_MIN: float = 0.1
        ACCELERATION_MAX: float = 1.0
        COMBUSTION_MIN: float = 0.1
        COMBUSTION_MAX: float = 100

