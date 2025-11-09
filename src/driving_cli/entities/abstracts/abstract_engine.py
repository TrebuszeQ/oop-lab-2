"""File for AEngine class."""
from enum import Enum
from abc import ABC, abstractmethod

from driving_cli.entities.abstracts.abstract_vehicle_part import AVehiclePart
from driving_cli.use_cases.validators import clamp_value


class AEngine(AVehiclePart, ABC):
    """Represents a physical engine that provides force and consumes fuel through combustion."""

    _force: float = 0.0
    _combustion: float = 0.0
    _power_output: float = 0.0

    class Constants(Enum):
        WEIGHT_MIN = 0.0
        WEIGHT_MAX = 0.0
        FORCE_MAX = 0.0
        FORCE_MIN = 0.0
        POWER_OUTPUT_MAX = 0.0
        POWER_OUTPUT_MIN = 0.0
        COMBUSTION_MIN: float = 0.0
        COMBUSTION_MAX: float = 0.0
        TRANSMISSION_TORQUE_MULTIPLIER: float = 0.0


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

    def __init__(self, weight: float, force: float, combustion: float):
        super().__init__(weight)
        self._force = clamp_value(value=force,
                                  min_value=self.Constants.FORCE_MIN.value,
                                  max_value=self.Constants.FORCE_MAX.value,
                                  name="Engine force")
        self._combustion = clamp_value(value=combustion,
                                       min_value=self.Constants.COMBUSTION_MIN.value,
                                       max_value=self.Constants.COMBUSTION_MAX.value,
                                       name="Engine combustion")


    @abstractmethod
    def increase_power_output(self, throttle_value: float, transmission_ratio: float) -> None:
        pass