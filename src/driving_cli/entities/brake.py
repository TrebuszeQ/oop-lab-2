"""File for Brake class."""
from logging import Logger, getLogger
from abstract_vehicle_part import AVehiclePart
from enum import Enum

log: Logger = getLogger(__name__)


class Brake(AVehiclePart):

    def __init__(self, weight: float, effectiveness: float):
        super().__init__(weight)
        self.effectiveness = effectiveness

    @classmethod
    def _validate_effectiveness(cls, effectiveness: float):
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

    class Constants(Enum):
        BRAKE_EFFECTIVENESS_MIN = 80
        BRAKE_EFFECTIVENESS_MAX = 80
        BRAKE_STEP_MIN = 0.1
        BRAKE_STEP_MAX = 0.5
