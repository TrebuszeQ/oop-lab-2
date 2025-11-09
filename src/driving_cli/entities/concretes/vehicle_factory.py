"""File for VehicleFactory and it's complements."""
from logging import Logger, getLogger

from driving_cli.entities.abstracts.abstract_transmission import ATransmission
from driving_cli.entities.abstracts.abstract_engine import AEngine
from driving_cli.entities.abstracts.abstract_fuel_tank import FuelTank
from driving_cli.entities.abstracts.abstract_throttle import AThrottle
from driving_cli.entities.abstracts.abstract_brake import ABrake

log: Logger = getLogger(__name__)


class VehicleFactory:
    """Static factory for creating concrete vehicle objects inheriting from AVehicle."""

    VehicleType = {
        "fuel_car": FuelCar
    }

    # @staticmethod
    # def produce(vehicle_type: str,
    #             acceleration: float,
    #             energy_provider: Type[AEnergyProvider],
    #             throttle: Throttle = Throttle(),
    #             brake: Brake = Brake(),
    #             engine: Engine = Engine()) -> AVehicle:
    #     """Creates and returns a Car instance. Returns Car if not supported vehicle type is provided."""
    #
    #     try:
    #         cls = VehicleFactory.VehicleType[vehicle_type]
    #
    #     except KeyError:
    #         log.warning("Not supported vehicle type: %s|", vehicle_type)
    #         return VehicleFactory.produce_car(weight=weight,
    #                                           acceleration=acceleration,
    #                                           throttle=throttle,
    #                                           brake=brake)


    @staticmethod
    def produce_fuel_car_from_parts(
                    throttle: AThrottle,
                    brake: ABrake,
                    engine: AEngine,
                    fuel_tank: FuelTank,
                    transmission: ATransmission
    ) -> FuelCar:
        """
        Creates and returns a Car instance with provided parts, or instantiates parts with default None.
        :param throttle: Throttle instance.
        :param brake: Brake instance.
        :param engine: Engine instance.
        :param fuel_tank: FuelTank instance.
        :param fuel_tank: Transmission instance.
        :param transmission: Transmission instance.
        :return: Instance of the FuelCar.
        """
        log.info("Producing FuelCar")
        return FuelCar(
            throttle=throttle,
            brake=brake,
            engine=engine,
            fuel_tank=fuel_tank,
            transmission=transmission
        )

    # @staticmethod
    # def produce_something(self):
    #     pass