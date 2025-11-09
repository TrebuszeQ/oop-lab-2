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
        WEIGHT_MIN = 1.0
        WEIGHT_MAX = 5000.0
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

    def __init__(self, weight: float, force: float, combustion: float):
        super().__init__(weight)
        self._force = clamp_value(value=force,
                                  min_value=self.Constants.FORCE_MIN.value,
                                  max_value=self.Constants.FORCE_MAX.value,
                                  name="Engine force")
        self._combustion = clamp_value(value=combustion,
                                       min_value=self.Constants.COMBUSTION_MIN.value,
                                       max_value=self.Constants.COMBUSTION_MIN.value,
                                       name="Engine combustion")


    @abstractmethod
    def increase_combustion(self, throttle_value: float, transmission_ratio: float) -> None:
        pass

    @abstractmethod
    def _update_force(self):
        pass