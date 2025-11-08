"""File for Dashboard class."""
from logging import Logger, getLogger

from driving_cli.entities.abstracts.abstract_vehicle import AVehicle
from driving_cli.use_cases.observer import Observer
from typing import Generic, TypeVar

log: Logger = getLogger(__name__)
T = TypeVar('T')


class Dashboard(Observer, Generic[T]):
    """Vehicle dashboard class"""

    def __init__(self, vehicle: T | None = None):
        self._vehicle: AVehicle = vehicle

    def update(self, subject: T) -> None:
        pass

    def print_speed(self):
        """Prints vehicle speed."""
        value: float = self._vehicle.speed
        print("Speed: %s", value)
        log.info("Speed: %s", value)

    def print_acceleration(self):
        """Prints vehicle acceleration."""
        value: float = self._vehicle.acceleration
        print("Acceleration: %s", value)
        log.info("Speed: %s", value)

    def print_throttle_status(self):
        """Prints vehicle throttle status."""
        value: float = self._vehicle.throttle.throttle_value
        print("Throttle status: %s", value)
        log.info("Throttle status: %s", value)

    def print_brake_status(self):
        """Prints vehicle brake status."""
        value: float = self._vehicle.brake.brake_value
        print("Throttle status: %s", value)
        log.info("Throttle status: %s", value)