"""File for FuelCar class."""
from logging import Logger, getLogger
from typing import Type

from driving_cli.entities.abstracts.abstract_throttle import AThrottle
from driving_cli.entities.abstracts.abstract_brake import ABrake
from driving_cli.entities.abstracts.abstract_engine import AEngine
from driving_cli.entities.abstracts.absract_fuel_car import AFuelCar
from driving_cli.entities.abstracts.abstract_fuel_tank import FuelTank
from driving_cli.entities.abstracts.abstract_transmission import ATransmission

log: Logger = getLogger(__name__)

class FuelCar(AFuelCar):
    def __init__(self, throttle: Type[AThrottle],
                 brake: Type[ABrake],
                 engine: Type[AEngine],
                 fuel_tank: Type[FuelTank],
                 transmission: Type[ATransmission]
                 ):

        super().__init__(throttle=throttle,
                         brake=brake,
                         engine=engine,
                         fuel_tank=fuel_tank,
                         transmission=transmission)