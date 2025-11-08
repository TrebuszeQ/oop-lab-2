"""File for VehicleFactory and it's complements."""
from logging import Logger, getLogger

from fuel_car import FuelCar
from driving_cli.entities.engine import Engine
from driving_cli.entities.fuel_tank import FuelTank
from throttle import Throttle
from brake import Brake

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
    def produce_fuel_car_and_parts(
            throttle_weight: float,
            acceleration: float,
            brake_weight: float,
            brake_effectiveness: float,
            engine_weight: float,
            combustion: float,
            fuel_tank_weight: float,
            fuel_tank_max_volume: float
            ) -> FuelCar:
        """
        Creates and returns FuelCar instance and its parts.
        :param throttle_weight: Weight of the throttle.
        :param acceleration: Throttle acceleration step.
        :param brake_weight: Weight of the brakes.
        :param brake_effectiveness: Effectiveness of the brakes.
        :param engine_weight: Weight of the engine.
        :param acceleration: Acceleration of the engine.
        :param combustion: Combustion of the engine.
        :param fuel_tank_weight: Weight of the fuel tank.
        :param fuel_tank_max_volume: Maximum volume of the fuel tank.
        :return: Instance of the FuelCar.
        """
        log.info("Producing FuelCar and it's parts.")
        return FuelCar(
            throttle=Throttle(weight=throttle_weight,
                              acceleration=acceleration),
            brake=Brake(weight=brake_weight,
                        effectiveness=brake_effectiveness),
            engine=Engine(weight=engine_weight,
                          combustion=combustion),
            fuel_tank=FuelTank(weight=fuel_tank_weight,
                               max_volume=fuel_tank_max_volume)
        )

    @staticmethod
    def produce_fuel_car_from_parts(
                    throttle: Throttle = None,
                    brake: Brake = None,
                    engine: Engine = None,
                    fuel_tank: FuelTank = None) -> FuelCar:
        """
        Creates and returns a Car instance with provided parts, or instantiates parts with default None.
        :param throttle: Throttle instance or None for defaults.
        :param brake: Brake instance or None for the defaults.
        :param engine: Engine instance or None for the defaults.
        :param fuel_tank: FuelTank instance or None for the defaults.
        :return: Instance of the FuelCar.
        """
        log.info("Producing FuelCar")
        return FuelCar(
            throttle,
            brake,
            engine,
            fuel_tank
        )

    # @staticmethod
    # def produce_something(self):
    #     pass