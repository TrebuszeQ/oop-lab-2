"""File for Brake class."""
from logging import Logger, getLogger
from abstract_vehicle_part import AVehiclePart
from enum import Enum
from driving_cli.use_cases.validators import clamp_value

log: Logger = getLogger(__name__)


class Brake(AVehiclePart):

    class Constants(Enum):
        BRAKE_EFFECTIVENESS_MIN = 80
        BRAKE_EFFECTIVENESS_MAX = 80
        BRAKE_STEP_MIN = 0.1
        BRAKE_STEP_MAX = 0.5

    def __init__(self, weight: float = None, effectiveness: float = None):
        super().__init__(weight)
        self.effectiveness = clamp_value(value=effectiveness,
                                         min_value=self.Constants.BRAKE_EFFECTIVENESS_MIN.value,
                                         max_value=self.Constants.BRAKE_EFFECTIVENESS_MAX.value,
                                         name="Brake effectiveness")