import time
from logging import Logger, getLogger
from curses import wrapper, noecho, initscr, napms, KEY_UP, KEY_DOWN
from typing import Type

from driving_cli.entities.abstracts.abstract_vehicle import AVehicle
from driving_cli.entities.concretes.basic.basic_brake import BasicBrake
from driving_cli.entities.concretes.basic.basic_engine import BasicEngine
from driving_cli.entities.concretes.basic.basic_throttle import BasicThrottle
from driving_cli.entities.concretes.basic.basic_transmission import BasicTransmission
from driving_cli.entities.concretes.dashboard import Dashboard
from driving_cli.entities.abstracts.absract_fuel_car import FuelCar
from driving_cli.drivers.cli_steering import CliSteering
from driving_cli.entities.abstracts.abstract_fuel_tank import FuelTank
from driving_cli.entities.concretes.vehicle_factory import VehicleFactory

log: Logger = getLogger(__name__)


def main():
    log.info("Welcome to Driving CLI")
    log.info("CLI simulates vehicle driving")

    real_time_loop(CliSteering.DT.value)


def real_time_loop(dt: float):
    """
    Loop in real time and read user input. Compensates execution time of update() by sleep.
    :return:
    """
    stdscr = initscr()
    noecho()
    # cbreak()
    last_time = time.perf_counter()

    stdscr.addstr(0, 0, "Sterowanie: ↑ przyspiesz, ' ' hamuj, ←/→ skręt, ESC wyjście")

    # choose type of vehicle
    vehicle_factory = VehicleFactory()
    fuel_car: FuelCar = (vehicle_factory.produce_fuel_car_from_parts(
        throttle=BasicThrottle(weight = 200,
                               step = 0.1),
        brake=BasicBrake(weight=200,
                         effectiveness=0.1),
        engine=BasicEngine(weight=1000,
                           force=100,
                           combustion=10),
        fuel_tank=FuelTank(weight=200,
                           max_volume=50),
        transmission=BasicTransmission(
            weight=200,
            ratios=None
        ))
    )
    dashboard: Dashboard[FuelCar] = Dashboard()

    while True:
        now = time.perf_counter()
        elapsed = now - last_time

        if elapsed < dt:
            time.sleep(dt - elapsed)
            continue
        last_time = now
        update_physics(fuel_car, dashboard)

        key = stdscr.getch()
        if key == KEY_UP:
            stdscr.addstr(2, 0, "Up arrow pressed")
            fuel_car.increase_throttle()
        elif key == KEY_DOWN:
            stdscr.addstr(2, 0, "Up arrow pressed")
            fuel_car.decrease_throttle()


        elif key == ord(' '):
            stdscr.addstr(2, 0, "Space pressed")
            fuel_car.engage_brake()

        elif key == 27:
            stdscr.addstr(2, 0, "ESC key pressed")
            log.info("Stopping the CLI")
            stdscr.refresh()
            napms(500)
            break

        update_physics(fuel_car, dashboard)
        stdscr.clear()
        stdscr.addstr(0, 0, "Predkosc: ")
        stdscr.addstr(2, 0, "Kierunek: ")
        stdscr.addstr(3, 0, "Czas symulacji: ")


def update_physics(vehicle: Type[AVehicle], dashboard: Dashboard[AVehicle]) -> None:
    """Applies all forces to calculate the new speed."""
    vehicle.accelerate()
    vehicle.hamper_by_brake()
    dashboard.print_throttle_status()
    dashboard.print_brake_status()
    dashboard.print_speed()
    dashboard.print_acceleration()


if __name__ == "__main__":
    wrapper(main())