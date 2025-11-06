"""File for Dashboard class."""
from logging import Logger, getLogger
from observer import Observer
from vehicle import Vehicle

log: Logger = getLogger(__name__)


class Dashboard(Observer):
    """Vehicle dashboard class"""


    def __init__(self):
        pass

    def update(self, subject: Vehicle) -> None:
        pass

    def print_speed(self):
        pass

    def print_throttle_status(self):
        pass

    def print_brake_status(self):
        pass