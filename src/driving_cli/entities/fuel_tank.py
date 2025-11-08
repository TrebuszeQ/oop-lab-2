"""File for FuelTank class."""
from logging import Logger, getLogger
from enum import Enum
from abstract_energy_provider import AEnergyProvider

log: Logger = getLogger(__name__)


class FuelTank(AEnergyProvider):
    @property
    def weight(self) -> float:
        return self._weight * self._volume

    def __init__(self, weight: float = None, max_volume: float = None):
        super().__init__(weight, max_volume)

    class Constants(Enum):
        MASS_KG: float = 1000
        MIN_KG: float = 0
