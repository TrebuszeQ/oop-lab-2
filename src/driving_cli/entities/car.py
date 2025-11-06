"""File for Car class."""
from logging import Logger, getLogger
from abstract_vehicle import AVehicle
from driving_cli.entities.brake import Brake
from driving_cli.entities.throttle import Throttle

log: Logger = getLogger(__name__)


class Car(AVehicle):
    def __init__(self, weight: float, acceleration: float, throttle: Throttle, brake: Brake):
        super().__init__(weight, acceleration, throttle, brake)
