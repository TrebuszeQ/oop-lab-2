from logging import Logger, getLogger

from driving_cli.entities.concretes.basic.basic_brake import BasicBrake
from driving_cli.entities.concretes.basic.basic_engine import BasicEngine
from driving_cli.entities.concretes.basic.basic_fuel_car import BasicFuelCar
from driving_cli.entities.concretes.basic.basic_fuel_tank import BasicFuelTank
from driving_cli.entities.concretes.basic.basic_throttle import BasicThrottle
from driving_cli.entities.concretes.basic.basic_transmission import BasicTransmission
from driving_cli.entities.concretes.basic_dashboard import Dashboard
from driving_cli.drivers.interactive_cli import InteractiveCli
from driving_cli.entities.concretes.vehicle_factory import VehicleFactory

log: Logger = getLogger(__name__)


def main():
    log.info("Welcome to Driving CLI")
    log.info("CLI simulates vehicle driving")

    vehicle_factory: VehicleFactory = VehicleFactory()
    fuel_car: BasicFuelCar = (vehicle_factory.produce_basic_fuel_car_from_parts(
        throttle=BasicThrottle(weight=200,
                               step=0.1),
        brake=BasicBrake(weight=200,
                         effectiveness=500),
        engine=BasicEngine(weight=1000,
                           force=100,
                           combustion=10),
        fuel_tank=BasicFuelTank(weight=200,
                                max_volume=50),
        transmission=BasicTransmission(
            weight=200,
            ratios=None
        ))
    )
    dashboard: Dashboard[BasicFuelCar] = Dashboard(fuel_car)
    interactive_cli: InteractiveCli = InteractiveCli(0.02)
    interactive_cli.real_time_loop(fuel_car, dashboard)


if __name__ == "__main__":
    main()