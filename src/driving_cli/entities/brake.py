"""File for Brake class."""
from logging import Logger, getLogger
from abstract_vehicle_part import AVehiclePart
from enum import Enum

log: Logger = getLogger(__name__)


class Brake(AVehiclePart):

    def __init__(self, weight: float = None, effectiveness: float = None):
        super().__init__(weight)
        self.effectiveness = effectiveness

    @classmethod
    def _validate_effectiveness(cls, effectiveness: float):
        max_value: float = cls.Constants.BRAKE_EFFECTIVENESS_MAX.value
        min_value: float = cls.Constants.BRAKE_EFFECTIVENESS_MIN.value
        param: str = "Effectiveness"

        if effectiveness > max_value:
            log.warning("%s cannot be greater than: %s|", param, max_value)
            log.warning("%s set to: %s|", param, max_value)
            effectiveness: float = max_value
        elif effectiveness < min_value or effectiveness is None:
            log.warning("%s cannot be less than: %s|", param, min_value)
            log.warning("%s set to: %s|", param, min_value)
            effectiveness: float = min_value
        cls._effectiveness = effectiveness

    class Constants(Enum):
        BRAKE_EFFECTIVENESS_MIN = 80
        BRAKE_EFFECTIVENESS_MAX = 80
        BRAKE_STEP_MIN = 0.1
        BRAKE_STEP_MAX = 0.5
