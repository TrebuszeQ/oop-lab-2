"""File for Car class."""
from logging import Logger, getLogger
from abstract_vehicle import AVehicle
from driving_cli.entities.throttle import Throttle
from driving_cli.entities.brake import Brake
from driving_cli.entities.engine import Engine
from driving_cli.entities.fuel_tank import FuelTank


log: Logger = getLogger(__name__)


class Car(AVehicle):
    def __init__(self, weight: float,
                 acceleration: float,
                 throttle: Throttle,
                 brake: Brake,
                 engine: Engine,
                 fuel_tank: FuelTank):
        super().__init__(weight, acceleration, throttle, brake)
