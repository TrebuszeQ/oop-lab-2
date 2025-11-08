"""File for Dashboard class."""
from logging import Logger, getLogger

from driving_cli.entities.abstract_vehicle import AVehicle
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
        """Prints vehicle speed"""
        print("Speed: %s")
        log.info("Speed: %s", self._vehicle.speed)

    def print_throttle_status(self):
        """Prints throttle status"""
        print("Throttle status: %s")
        log.info("Throttle status: %s", self._vehicle.throttle.throttle_value)
    #
    # def print_brake_status(self):
    #     """Prints vehicle speed"""
    #     pass