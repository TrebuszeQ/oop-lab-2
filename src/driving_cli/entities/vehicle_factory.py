"""File for VehicleFactory and it's complements."""
from logging import Logger, getLogger

from abstract_vehicle import AVehicle
from car import Car
from throttle import Throttle
from brake import Brake

log: Logger = getLogger(__name__)


class VehicleFactory:
    """Static factory for creating vehicle objects."""

    VehicleType = {
        "car": Car
    }

    @staticmethod
    def produce(vehicle_type: str,
                weight: float,
                acceleration: float,
                throttle: Throttle = Throttle(),
                brake: Brake = Brake()) -> AVehicle:
        """Creates and returns a Car instance. Returns Car if not supported vehicle type is provided."""

        try:
            cls = VehicleFactory.VehicleType[vehicle_type]
            return cls(weight=weight,
                       acceleration=acceleration,
                       throttle=throttle,
                       brake=brake)
        except KeyError:
            log.warning("Not supported vehicle type: %s|", vehicle_type)
            return VehicleFactory.produce_car(weight=weight,
                                              acceleration=acceleration,
                                              throttle=throttle,
                                              brake=brake)


    @staticmethod
    def produce_car(weight: float,
                    acceleration: float,
                    throttle: Throttle = None,
                    brake: Brake = None) -> Car:
        """Creates and returns a Car instance."""
        log.info("Producing car")
        return Car(weight=weight,
                   acceleration=acceleration,
                   throttle=Throttle(),
                   brake=Brake())

    # @staticmethod
    # def produce_something(self):
    #     pass