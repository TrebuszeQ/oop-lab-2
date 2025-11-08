"""File for FuelTank class."""
from logging import Logger, getLogger
from enum import Enum

from driving_cli.entities.abstracts.abstract_energy_provider import AEnergyProvider

log: Logger = getLogger(__name__)


class FuelTank(AEnergyProvider):
    class Constants(Enum):
        WEIGHT_MIN = 100.0
        WEIGHT_MAX = 5000.0
        VOLUME_MIN = 0.0
        VOLUME_MAX = 5000.0

    @property
    def weight(self) -> float:
        return self._weight + self._volume

    def __init__(self, weight: float = None, max_volume: float = None):
        super().__init__(weight, max_volume)
