"""File for energy provider class"""
from logging import Logger, getLogger
from abc import ABC
from enum import Enum

from driving_cli.entities.abstract_vehicle_part import AVehiclePart
from driving_cli.use_cases.validators import clamp_value

log: Logger = getLogger(__name__)

class AEnergyProvider(AVehiclePart, ABC):
    _max_volume = 0.0
    _volume = 0.0

    class Constants(Enum):
        WEIGHT_MIN = 0.0
        WEIGHT_MAX = 0.0
        VOLUME_MIN = 0.0
        VOLUME_MAX = 0.0

    @property
    def max_volume(self) -> float:
        return self._max_volume

    @property
    def volume(self) -> float:
        return self._current_volume

    @volume.setter
    def volume(self, max_volume: float) -> None:
        self._max_volume = clamp_value(value=max_volume,
                                   min_value=self.Constants.VOLUME_MIN.value,
                                   max_value=self.Constants.VOLUME_MAX.value,
                                   name="Max volume")
        self._volume = self.Constants.VOLUME_MIN.value

    def __init__(self, weight: float = None,
                    max_volume: float = None):
        super().__init__(weight)
        self._max_volume = max_volume
        self._current_volume = max_volume