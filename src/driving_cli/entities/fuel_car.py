"""File for FuelCar class."""
from logging import Logger, getLogger
from abstract_vehicle import AVehicle
from driving_cli.entities.throttle import Throttle
from driving_cli.entities.brake import Brake
from driving_cli.entities.engine import Engine
from driving_cli.entities.fuel_tank import FuelTank


log: Logger = getLogger(__name__)


class FuelCar(AVehicle):
    def __init__(self, throttle: Throttle,
                 brake: Brake,
                 engine: Engine,
                 fuel_tank: FuelTank
                 ):
        super().__init__(throttle, brake, engine, fuel_tank)
