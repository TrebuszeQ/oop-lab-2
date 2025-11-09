"""File for BasicEngine class."""
from logging import Logger, getLogger
from enum import Enum

from driving_cli.entities.abstracts.abstract_engine import AEngine
from driving_cli.use_cases.validators import clamp_value

log: Logger = getLogger(__name__)


class BasicEngine(AEngine):
    """Represents a physical basic engine that provides force and consumes fuel through combustion."""

    _force: float = 0.0
    _combustion: float = 0.0
    _power_output: float = 0.0

    class Constants(Enum):
        WEIGHT_MIN = 1.0
        WEIGHT_MAX = 1000.0
        FORCE_MAX = 1000.0
        FORCE_MIN = 0.0
        POWER_OUTPUT_MAX = 1000.0
        POWER_OUTPUT_MIN = 0.0
        COMBUSTION_MIN: float = 0.0
        COMBUSTION_MAX: float = 100
        TRANSMISSION_TORQUE_MULTIPLIER: float = 0.1

    @property
    def power_output(self) -> float:
        """Power output based on combustion efficiency."""
        return self._power_output

    @property
    def force(self) -> float:
        value: float = self.Constants.FORCE_MAX.value * self._power_output
        log.info("New engine force: %s", value)
        return value

    @property
    def combustion(self) -> float:
        value: float = self.Constants.COMBUSTION_MAX.value * self._power_output
        log.info("New combustion: %s", value)
        return value

    def __init__(self, weight: float = None, force: float = None, combustion: float = None):
        super().__init__(weight, force, combustion)
        self._force = clamp_value(value=force,
                                  min_value=self.Constants.FORCE_MIN.value,
                                  max_value=self.Constants.FORCE_MAX.value,
                                  name="Engine force")
        self._combustion = clamp_value(value=combustion,
                                       min_value=self.Constants.COMBUSTION_MIN.value,
                                       max_value=self.Constants.COMBUSTION_MAX.value,
                                       name="Engine combustion")


    def increase_power_output(self, throttle_value: float, transmission_ratio: float) -> None:
        """
        Adjusts combustion intensity based on throttle and transmission rate.
        With combustion engine force changes.

        :param throttle_value: Status of throttle input.
        :param transmission_ratio: Torque multiplier.
        """
        log.info("Increasing power output.")

        desired_output = throttle_value * (1.0 + transmission_ratio * self.Constants.TRANSMISSION_TORQUE_MULTIPLIER.value)
        final_output_level = clamp_value(value=desired_output,
                                       min_value=self.Constants.POWER_OUTPUT_MIN.value,
                                       max_value=self.Constants.POWER_OUTPUT_MAX.value,
                                       name="Engine power output")
        self._power_output = final_output_level
        self._force = clamp_value(value=self.force,
                                  min_value=self.Constants.FORCE_MIN.value,
                                  max_value=self.Constants.FORCE_MAX.value,
                                  name="Engine force")
        self._combustion = clamp_value(value=self.combustion,
                                  min_value=self.Constants.COMBUSTION_MIN.value,
                                  max_value=self.Constants.COMBUSTION_MAX.value,
                                  name="Engine combustion")
        log.info("New power output: %s", self._power_output)
