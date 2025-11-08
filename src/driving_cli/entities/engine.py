"""File for Engine class."""
from logging import Logger, getLogger
from enum import Enum
from abstract_vehicle_part import AVehiclePart
from driving_cli.use_cases.validators import clamp_value

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
        self._force = clamp_value(value=force,
                                  min_value=self.Constants.FORCE_MIN.value,
                                  max_value=self.Constants.FORCE_MAX.value,
                                  name="Engine force")
        self._combustion = clamp_value(value=combustion,
                                       min_value=self.Constants.COMBUSTION_MIN.value,
                                       max_value=self.Constants.COMBUSTION_MIN.value,
                                       name="Engine combustion")


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
        cls._combustion = clamp_value(value=new_combustion,
                                       min_value=cls.Constants.COMBUSTION_MIN.value,
                                       max_value=cls.Constants.COMBUSTION_MIN.value,
                                       name="Engine combustion")

        cls._update_force()
        log.info("New combustion: %s", new_combustion)

    @classmethod
    def _update_force(cls):
        """Updates force value bases on combustion."""
        k: float = cls.Constants.FORCE_MAX.value / cls.Constants.COMBUSTION_MAX.value
        delta: float = cls._combustion * k
        cls._force = clamp_value(value=delta,
                                   min_value=cls.Constants.COMBUSTION_MIN.value,
                                   max_value=cls.Constants.COMBUSTION_MIN.value,
                                   name="Engine combustion")

    @classmethod
    def constants(cls):
        return cls.Constants

