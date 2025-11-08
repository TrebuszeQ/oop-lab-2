"""File for Transmission class."""
from logging import Logger, getLogger

from driving_cli.entities.abstract_vehicle_part import AVehiclePart

log: Logger = getLogger(__name__)


class Transmission(AVehiclePart):
    def __init__(self, weight: float, ratio: float):
        super().__init__(weight, ratio)
