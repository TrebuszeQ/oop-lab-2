"""File for FuelCar class."""
from logging import Logger, getLogger

from driving_cli.entities.abstracts.abstract_vehicle import AVehicle
from driving_cli.entities.abstracts.abstract_throttle import Throttle
from driving_cli.entities.abstracts.abstract_brake import Brake
from driving_cli.entities.abstracts.abstract_engine import Engine
from driving_cli.entities.fuel_tank import FuelTank
from driving_cli.entities.abstracts.abstract_transmission import ATransmission

log: Logger = getLogger(__name__)


class FuelCar(AVehicle):
    def __init__(self, throttle: Throttle,
                 brake: Brake,
                 engine: Engine,
                 fuel_tank: FuelTank,
                 transmission: ATransmission
                 ):

        super().__init__(throttle=throttle,
                         brake=brake,
                         engine=engine,
                         energy_provider=fuel_tank,
                         transmission=transmission)
