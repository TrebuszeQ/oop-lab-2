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

    class Constants(Enum):
        MASS_KG = 0
        MIN_KG = 0
        MIN_VOLUME = 0
        MAX_VOLUME = 0