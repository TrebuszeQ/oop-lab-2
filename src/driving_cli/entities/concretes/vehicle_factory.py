"""File for VehicleFactory and its complements."""
from logging import Logger, getLogger

from driving_cli.entities.abstracts.abstract_brake import ABrake
from driving_cli.entities.abstracts.abstract_engine import AEngine
from driving_cli.entities.abstracts.abstract_fuel_tank import AFuelTank
from driving_cli.entities.abstracts.abstract_throttle import AThrottle
from driving_cli.entities.abstracts.abstract_transmission import ATransmission
from driving_cli.entities.concretes.basic.basic_fuel_car import BasicFuelCar

log: Logger = getLogger(__name__)


class VehicleFactory:
    """Concrete factory for creating concrete vehicle objects."""

    @staticmethod
    def produce_basic_fuel_car_from_parts(
            throttle: AThrottle,
            brake: ABrake,
            engine: AEngine,
            fuel_tank: AFuelTank,
            transmission: ATransmission
    ) -> BasicFuelCar:
        """
        Creates and returns a concrete FuelCar instance with provided parts,
        accepting any concrete class that implements the abstract interfaces.
        """
        log.info("Producing BasicFuelCar")
        return BasicFuelCar(
            throttle=throttle,
            brake=brake,
            engine=engine,
            fuel_tank=fuel_tank,
            transmission=transmission
        )