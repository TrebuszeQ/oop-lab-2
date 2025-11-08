"""File for Engine class."""
from logging import Logger, getLogger
from enum import Enum
from abstract_vehicle_part import AVehiclePart

log: Logger = getLogger(__name__)


class Engine(AVehiclePart):
    """Represents a physical engine that provides force and consumes fuel through combustion."""

    _force: float = 0.0
    _combustion: float = 0.0
    _power_output: float = 0.0

    class Constants(Enum):
        MASS_KG = 500
        MIN_KG = 10
        FORCE_MAX = 10000
        FORCE_MIN = 1
        COMBUSTION_MIN: float = 0.1
        COMBUSTION_MAX: float = 100

    @property
    def power_output(self) -> float:
        """Power output based on combustion efficiency."""
        return self._force * self._combustion

    @property
    def force(self) -> float:
        return self._force

    @property
    def combustion(self) -> float:
        return self._combustion

    def __init__(self, weight: float = None, force: float = None, combustion: float = None):
        super().__init__(weight)
        self._force = self._validate_force(force)
        self._combustion = self._validate_combustion(combustion)

    @classmethod
    def _validate_force(cls, force: float):
        max_value: float = cls.Constants.FORCE_MAX.value
        min_value: float = cls.Constants.FORCE_MIN.value
        param: str = "Force"

        if force > max_value:
            log.warning("%s cannot be greater than: %s|", param, max_value)
            log.warning("%s set to: %s|", param, max_value)
            force = max_value
        elif force < min_value or force is None:
            log.warning("%s cannot be less than: %s|", param, min_value)
            log.warning("%s set to: %s|", param, min_value)
            force = min_value
        return force

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
    def increase_combustion(cls, throttle_value: float, transmission_ratio: float) -> None:
        """
        Adjusts combustion intensity based on throttle and transmission rate.
        With combustion engine force changes.

        :param throttle_value: Status of throttle input.
        :param transmission_ratio: Torque multiplier.
        """
        log.info("Increasing combustion.")
        if throttle_value < 0 or throttle_value > 1:
            log.warning("Throttle status out of 0-1 range: %s", throttle_value)
            throttle_value = max(0.0, min(1.0, throttle_value))

        delta = throttle_value * (1 + transmission_ratio * 0.1)
        new_combustion = cls._combustion + delta
        cls._combustion = cls._validate_combustion(new_combustion)

        cls._update_force()
        log.info("New combustion: %s", new_combustion)

    @classmethod
    def _update_force(cls):
        """Updates force value bases on combustion."""
        k: float = cls.Constants.FORCE_MAX.value / cls.Constants.COMBUSTION_MAX.value
        delta: float = cls._combustion * k
        cls._force = cls._validate_force(delta)

    @classmethod
    def constants(cls):
        return cls.Constants

