"""File for Dashboard class."""
from logging import Logger, getLogger
from typing import Generic, TypeVar
from abc import ABC, abstractmethod

from driving_cli.use_cases.observer import Observer

log: Logger = getLogger(__name__)
T = TypeVar('T')


class ADashboard(Observer, Generic[T], ABC):
    """Vehicle dashboard class"""

    def __init__(self, vehicle: T):
        self._vehicle: T = vehicle

    @abstractmethod
    def update(self, subject: T) -> None:
        pass

    @abstractmethod
    def print_speed(self):
        pass

    @abstractmethod
    def print_acceleration(self):
        pass

    @abstractmethod
    def print_throttle_status(self):
        pass

    @abstractmethod
    def print_brake_status(self):
        pass

    @abstractmethod
    def print_combustion(self):
        pass