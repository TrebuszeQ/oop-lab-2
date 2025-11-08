"""File for FuelCar class."""
from logging import Logger, getLogger
from abstract_vehicle import AVehicle
from driving_cli.entities.throttle import Throttle
from driving_cli.entities.brake import Brake
from driving_cli.entities.engine import Engine
from driving_cli.entities.fuel_tank import FuelTank
from driving_cli.entities.transmission import Transmission

log: Logger = getLogger(__name__)


class FuelCar(AVehicle):
    def __init__(self, throttle: Throttle,
                 brake: Brake,
                 engine: Engine,
                 fuel_tank: FuelTank,
                 transmission: Transmission
                 ):
        super().__init__(throttle=throttle,
                         brake=brake,
                         engine=engine,
                         energy_provider=fuel_tank,
                         transmission=transmission)
