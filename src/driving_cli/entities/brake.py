"""File for Brake class."""
from logging import Logger, getLogger
from abstract_vehicle_part import AVehiclePart
from enum import Enum

log: Logger = getLogger(__name__)


class Brake(AVehiclePart):

    def __init__(self, weight: float):
        super().__init__(weight)

    class Constants(Enum):
        BRAKE_EFFECTIVENESS_KMH = 80
        BRAKE_STEP_MIN = 0.1
        BRAKE_STEP_MAX = 0.5
