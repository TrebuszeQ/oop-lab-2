"""File for energy provider class"""
from logging import Logger, getLogger
from abc import ABC, abstractmethod
from enum import Enum
from abstract_vehicle_part import AVehiclePart

log: Logger = getLogger(__name__)

class AEnergyProvider(AVehiclePart, ABC):
    _volume = None

    @property
    def volume(self) -> float:
        return self._volume

    def __init__(self, weight: float, volume: float):
        super().__init__(weight)
        self._volume = volume

    @classmethod
    def _validate_volume(cls, volume: float):
        max_value: float = cls.Constants.VOLUME_MAX.value
        min_value: float = cls.Constants.VOLUME_MIN.value

        if volume > max_value:
            log.warning("Volume cannot be greater than: %s|", max_value)
            log.warning("Volume set to: %s|", max_value)
            volume: float = max_value
        elif volume < min_value:
            log.warning("Volume cannot be less than: %s|", min_value)
            log.warning("Volume set to: %s|", min_value)
            volume: float = min_value
        cls._volume = volume


    @classmethod
    def decrease_volume(cls, combustion: float):
        cls._volume = cls._volume - combustion


    class Constants(Enum):
        MASS_KG = 0
        MIN_KG = 0
        VOLUME_MIN = 0
        VOLUME_MAX = 0