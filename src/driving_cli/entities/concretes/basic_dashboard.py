"""File for Dashboard class."""
from logging import Logger, getLogger
from typing import TypeVar

from driving_cli.entities.abstracts.abstract_dashboard import ADashboard

log: Logger = getLogger(__name__)
T = TypeVar('T')


class Dashboard(ADashboard):
    """Vehicle dashboard class"""

    def __init__(self, vehicle: T):
        super().__init__(vehicle)

    def update(self, subject: T) -> None:
        pass

    def print_speed(self):
        """Prints vehicle speed."""
        value: float = self._vehicle.speed
        print("Speed: ", value)
        log.info("Speed: %s", value)

    def print_acceleration(self):
        """Prints vehicle acceleration."""
        value: float = self._vehicle.acceleration
        print("Acceleration: ", value)
        log.info("Speed: %s", value)

    def print_throttle_status(self):
        """Prints vehicle throttle status."""
        value: float = self._vehicle.throttle.throttle_value
        print("Throttle status: ", value)
        log.info("Throttle status: %s", value)

    def print_brake_status(self):
        """Prints vehicle brake status."""
        value: float = self._vehicle.brake.brake_value
        print("Brake status: ", value)
        log.info("Brake status: %s", value)

    def print_combustion(self):
        """Prints combustion value."""
        value: float = self._vehicle.engine.combustion
        print("Combustion: ", value)
        log.info("Combustion: %s", value)