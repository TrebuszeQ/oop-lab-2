"""File for Transmission class."""
from logging import Logger, getLogger
from enum import Enum
from array import array, ArrayType

from driving_cli.entities.abstract_vehicle_part import AVehiclePart
from driving_cli.use_cases.validators import clamp_value

log: Logger = getLogger(__name__)


class Transmission(AVehiclePart):
    _ratio: float = 0.0
    _ratios: ArrayType[float] = None
    _gears_count: int = 0
    _current_gear: int = 0

    class Constants(Enum):
        MASS_KG: float = 1000
        MIN_KG: float = 200
        RATIO_MAX: float = 5.0
        RATIO_MIN: float = 0.5
        DEFAULT_GEAR_COUNT: int = 6

    @property
    def ratio(self) -> float:
        """Transmission ratio"""
        return self._ratio

    @property
    def ratios(self) -> ArrayType[float]:
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

    def __init__(self, weight: float, ratios: list[float] = ()):
        super().__init__(weight)
        self._ratios: ArrayType[float] = self._validate_ratios(ratios or self._generate_default_ratios())
        self._current_gear: int = 0

    @classmethod
    def shift_up(cls) -> None:
        """Shifts to a higher gear."""
        log.info("Shifting up")
        if cls._current_gear < cls._gears_count:
            cls._current_gear += 1
            log.info("Gear shifted to: %s", cls._current_gear)
        else:
            log.info("Already on the highest gear: %s", cls._current_gear)

    @classmethod
    def shift_down(cls) -> None:
        """Shifts to a lower gear."""
        log.info("Shifting down")
        if cls._current_gear != 0:
            cls._current_gear -= 1
        else:
            log.info("Already on the lowest gear: %s", cls._current_gear)

    @classmethod
    def update_ratio(cls) -> None:
        """Updates gear transmission ratio."""

        cls._ratio = cls._ratios[cls._current_gear]
        log.info("Current gears ratio: %s", cls._ratio)

    @classmethod
    def _generate_default_ratios(cls) -> ArrayType[float]:
        """Generates default evenly spaced gear rations."""
        max_ratio = cls.Constants.RATIO_MAX.value
        min_ratio = cls.Constants.RATIO_MIN.value
        gears = cls.Constants.DEFAULT_GEAR_COUNT.value

        step: float = (max_ratio - min_ratio) / (gears - 1)
        ratios: list[float] = [round(max_ratio - step * i, 2) for i in range(gears)]
        return array('d', ratios)

    @classmethod
    def _validate_ratios(cls, ratios: list[float]) -> ArrayType[float]:
        """Validates all ratios are within valid range."""
        valid_ratios = array('d')
        min_value: float = cls.Constants.RATIO_MIN.value
        max_value: float = cls.Constants.RATIO_MAX.value
        [valid_ratios.append(clamp_value(ratio, min_value, max_value, "Transmission ratio"))
         for ratio in ratios]

        return valid_ratios