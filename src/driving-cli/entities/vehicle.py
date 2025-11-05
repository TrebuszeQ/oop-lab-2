"""File for Car class."""
from distutils.command.install import value
from logging import Logger, getLogger
from vehicle_constants import VehicleConstants

log: Logger = getLogger(__name__)


class Vehicle:
    @property
    def weight(self) -> float:
        return self._weight

    @weight.setter
    def weight(self, value: float) -> None:
        self.weight = self.__validate_weight(value)

    @property
    def speed(self) -> float:
        return self._speed

    @speed.setter
    def speed(self, value) -> None:
        self._speed = self.__validate_speed(value)

    def __init__(self, weight: float, speed: float):
        self._weight: float = weight
        self._speed: float = speed

    def __validate_weight(self, weight) -> float:
        max_weight: float = VehicleConstants.MASS_KG.value
        min_weight: float = VehicleConstants.MIN_KG.value
        if weight > max_weight:
            log.warning("Vehicle weight cannot be greater than: %s|", max_weight)
            log.warning("Vehicle weight set to: %s|", max_weight)
            weight = max_weight
        elif weight < 0:
            log.warning("Vehicle weight cannot be less than: %s|", min_weight)
            log.warning("Vehicle weight set to: %s|", min_weight)
            weight = min_weight
        return weight

    def __validate_speed(self, speed) -> float:
        max_speed: float = VehicleConstants.MAX_SPEED_KHM.value
        min_speed: float = VehicleConstants.MIN_SPEED.value
        if speed > max_speed:
            log.warning("Vehicle speed is greater than: %s|", max_speed)
            log.warning("Vehicle speed set to: $s|", max_speed)
            speed = max_speed
        elif speed < 0:
            log.warning("Vehicle speed cannot be less than: %s|", min_speed)
            log.warning("Vehicle speed set to: $s|", max_speed)
        return speed