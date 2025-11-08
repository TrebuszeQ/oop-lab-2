"""File for VehicleFactory and it's complements."""
from logging import Logger, getLogger

from driving_cli.entities.abstracts.abstract_transmission import ATransmission
from driving_cli.entities.concretes.fuel_car import FuelCar
from driving_cli.entities.abstracts.abstract_engine import AEngine
from driving_cli.entities.concretes.fuel_tank import FuelTank
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
    def produce_fuel_car_and_parts(
            throttle_weight: float,
            throttle_step: float,
            brake_weight: float,
            brake_effectiveness: float,
            engine_weight: float,
            engine_force: float,
            combustion: float,
            fuel_tank_weight: float,
            fuel_tank_max_volume: float,
            transmission_weight: float,
            transmission_ratios: list[float] = None
    ) -> FuelCar:
        """
        Creates and returns FuelCar instance and its parts.
        :param throttle_weight: Weight of the throttle.
        :param throttle_step: Throttle step value.
        :param brake_weight: Weight of the brakes.
        :param brake_effectiveness: Effectiveness of the brakes.
        :param engine_weight: Weight of the engine.
        :param engine_force: Force of the engine.
        :param combustion: Combustion of the engine.
        :param fuel_tank_weight: Weight of the fuel tank.
        :param fuel_tank_max_volume: Maximum volume of the fuel tank.
        :param transmission_weight: Weight of the transmission.
        :param transmission_ratios: Ratios of the transmission. If None, defaults would be generated.
        :return: Instance of the FuelCar.
        """
        log.info("Producing FuelCar and it's parts.")
        return FuelCar(
            throttle=AThrottle(weight=throttle_weight,
                               step=throttle_step),
            brake=ABrake(weight=brake_weight,
                         effectiveness=brake_effectiveness),
            engine=AEngine(weight=engine_weight,
                           force=engine_force,
                           combustion=combustion),
            fuel_tank=FuelTank(weight=fuel_tank_weight,
                               max_volume=fuel_tank_max_volume),
            transmission=ATransmission(weight=transmission_weight,
                                       ratios=transmission_ratios)
        )

    @staticmethod
    def produce_fuel_car_from_parts(
                    throttle: AThrottle = None,
                    brake: ABrake = None,
                    engine: AEngine = None,
                    fuel_tank: FuelTank = None,
                    transmission: ATransmission = None
    ) -> FuelCar:
        """
        Creates and returns a Car instance with provided parts, or instantiates parts with default None.
        :param throttle: Throttle instance or None for defaults.
        :param brake: Brake instance or None for the defaults.
        :param engine: Engine instance or None for the defaults.
        :param fuel_tank: FuelTank instance or None for the defaults.
        :param fuel_tank: Transmission instance or None for the defaults.
        :param transmission: Transmission instance or None for the defaults.
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