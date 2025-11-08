"""File for ATransmission class."""
from logging import Logger, getLogger
from abc import ABC, abstractmethod
from enum import Enum
from array import array
from collections.abc import MutableSequence

from driving_cli.entities.abstracts.abstract_vehicle_part import AVehiclePart
from driving_cli.use_cases.validators import clamp_value

log: Logger = getLogger(__name__)


class ATransmission(AVehiclePart, ABC):
    _ratio: float = 0.0
    _ratios: MutableSequence[float] = array('d')
    _gears_count: int = 0
    _current_gear: int = 0

    class Constants(Enum):
        WEIGHT_MIN = 1.0
        WEIGHT_MAX = 2000.0
        RATIO_MAX: float = 5.0
        RATIO_MIN: float = 0.5
        DEFAULT_GEAR_COUNT: int = 6

    @property
    def ratio(self) -> float:
        """Transmission ratio"""
        return self._ratio

    @property
    def ratios(self) -> MutableSequence[float]:
        """Transmission ratios of gears."""
        return self._ratios

    @property
    def gear_count(self) -> int:
        """Number of gears."""
        return len(self._ratios)

    @property
    def current_gear(self) -> int:
        """Number of current gear"""
        return self._current_gear

    def __init__(self, weight: float, ratios: list[float] | None = None):
        super().__init__(weight)
        self._ratios: MutableSequence[float] = self._validate_ratios(ratios or self._generate_default_ratios())
        self._current_gear: int = 0

    @abstractmethod
    def shift_up(self) -> None:
        """Shifts to a higher gear."""
        log.info("Shifting up")
        if self._current_gear < self._gears_count:
            self._current_gear += 1
            log.info("Gear shifted to: %s", self._current_gear)
        else:
            log.info("Already on the highest gear: %s", self._current_gear)

    @abstractmethod
    def shift_down(self) -> None:
        """Shifts to a lower gear."""
        log.info("Shifting down")
        if self._current_gear != 0:
            self._current_gear -= 1
        else:
            log.info("Already on the lowest gear: %s", self._current_gear)

    @abstractmethod
    def update_ratio(self) -> None:
        """Updates gear transmission ratio."""

        self._ratio = self._ratios[self._current_gear]
        log.info("Current gears ratio: %s", self._ratio)

    @abstractmethod
    def _generate_default_ratios(self) -> MutableSequence[float]:
        """Generates default evenly spaced gear rations."""
        max_ratio = self.Constants.RATIO_MAX.value
        min_ratio = self.Constants.RATIO_MIN.value
        gears = self.Constants.DEFAULT_GEAR_COUNT.value

        step: float = (max_ratio - min_ratio) / (gears - 1)
        ratios: list[float] = [round(max_ratio - step * i, 2) for i in range(gears)]
        return array('d', ratios)

    @abstractmethod
    def _validate_ratios(self, ratios: list[float]) -> MutableSequence[float]:
        """Validates all ratios are within valid range."""
        valid_ratios: MutableSequence[float] = array('d')
        min_value: float = self.Constants.RATIO_MIN.value
        max_value: float = self.Constants.RATIO_MAX.value
        [valid_ratios.append(clamp_value(ratio, min_value, max_value, "Transmission ratio"))
         for ratio in ratios]

        return valid_ratios