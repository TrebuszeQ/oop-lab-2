"""File for energy provider class"""
from logging import Logger, getLogger
from abc import ABC
from enum import Enum
from abstract_vehicle_part import AVehiclePart
from driving_cli.use_cases.validators import clamp_value

log: Logger = getLogger(__name__)

class AEnergyProvider(AVehiclePart, ABC):
    _max_volume = None
    _volume = None

    @property
    def max_volume(self) -> float:
        return self._volume

    @property
    def volume(self) -> float:
        return self._current_volume

    @volume.setter
    def volume(self, new_volume: float) -> None:
        self._volume = clamp_value(value=new_volume,
                                   min_value=self.Constants.VOLUME_MIN.value,
                                   max_value=self.Constants.VOLUME_MAX.value,
                                   name="Volume")

    def __init__(self, weight: float = None,
                    max_volume: float = None):
        super().__init__(weight)
        self._max_volume = max_volume
        self.Constants.VOLUME_MAX = max_volume
        self._current_volume = max_volume

    @classmethod
    def decrease_volume(cls, combustion: float):
        cls._volume = cls._volume - combustion

    class Constants(Enum):
        MASS_KG = 0
        MIN_KG = 0
        VOLUME_MIN = 0
        VOLUME_MAX = 0