"""File for FuelTank class."""
from logging import Logger, getLogger
from enum import Enum
from abstract_energy_provider import AEnergyProvider

log: Logger = getLogger(__name__)


class FuelTank(AEnergyProvider):

    def __init__(self, weight: float, volume: float):
        super().__init__(weight, volume)

    class Constants(Enum):
        MASS_KG: float = 0
        MIN_KG: float = 0
