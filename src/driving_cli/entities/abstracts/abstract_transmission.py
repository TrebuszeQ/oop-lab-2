"""File for ATransmission class."""
from abc import ABC, abstractmethod
from enum import Enum
from array import array
from collections.abc import MutableSequence

from driving_cli.entities.abstracts.abstract_vehicle_part import AVehiclePart


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

    def __init__(self, weight: float, ratios: list[float]):
        super().__init__(weight)
        self._ratios: MutableSequence[float] = self._validate_ratios(ratios or self._generate_default_ratios())
        self._current_gear: int = 0

    @abstractmethod
    def shift_up(self) -> None:
       pass

    @abstractmethod
    def shift_down(self) -> None:
        pass

    @abstractmethod
    def update_ratio(self) -> None:
        pass

    @abstractmethod
    def _generate_default_ratios(self) -> MutableSequence[float]:
        pass

    @abstractmethod
    def _validate_ratios(self, ratios: list[float]) -> MutableSequence[float]:
        pass