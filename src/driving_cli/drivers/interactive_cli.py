"""File for InteractiveCli class."""
from logging import Logger, getLogger
import time
import readchar

from driving_cli.entities.abstracts.abstract_dashboard import ADashboard
from driving_cli.entities.abstracts.abstract_vehicle import AVehicle

log: Logger = getLogger(__name__)


class InteractiveCli:
    _dt: float = 0.0
    _simulation_running: bool = False
    _key_actions = dict()

    @property
    def dt(self) -> float:
        return self._dt

    @property
    def simulation_running(self) -> bool:
        return self._simulation_running

    @property
    def key_actions(self) -> dict:
        return self._key_actions

    def __init__(self, dt: float):
        self._dt = dt
        self._key_actions = {
            readchar.key.UP: lambda vehicle: InteractiveCli.on_up_arrow(vehicle),
            readchar.key.DOWN: lambda vehicle: InteractiveCli.on_down_arrow(vehicle),
            readchar.key.SPACE: lambda vehicle: InteractiveCli.on_space_bar(vehicle),
            readchar.key.ESC: lambda: self.on_esc()
        }

    def real_time_loop(self, vehicle: AVehicle, dashboard: ADashboard):
        """
        Loop in real time and read user input. Compensates execution time of update() by sleep.
        """
        log.info("CLI started")
        self._simulation_running = True
        last_time = time.perf_counter()
        print("↑ accelerate, ' ' hamper, ESC exit")

        counter: int = 0
        while self._simulation_running:
            log.info("Loop no.: %s", counter)
            now = time.perf_counter()
            elapsed = now - last_time

            if elapsed < self._dt:
                time.sleep(self._dt - elapsed)
                continue
            last_time = now

            key = None
            try:
                key = readchar.readkey()
                print(key)
            except IOError:
                pass
            except Exception as e:
                if str(e) == "KeyboardInterrupt":
                    break

            if key in self._key_actions:
                self._key_actions[key](vehicle)

            vehicle.accelerate()
            dashboard.print_throttle_status()
            dashboard.print_brake_status()
            dashboard.print_speed()
            dashboard.print_acceleration()
            dashboard.print_combustion()

            log.info("Simulation time: %s", elapsed)
            counter += 1

        log.info("Simulation finished")

    @staticmethod
    def on_up_arrow(vehicle: AVehicle):
        message: str = "Key: Up (Accelerate)"
        log.info(message)
        print(message)
        vehicle.increase_throttle()

    @staticmethod
    def on_down_arrow(vehicle: AVehicle):
        message: str = "Key: Down (Decelerate)"
        log.info(message)
        print(message)
        vehicle.decrease_throttle()

    @staticmethod
    def on_space_bar(vehicle: AVehicle):
        message: str = "Key: Space (Brake)"
        log.info(message)
        print(message)
        vehicle.engage_brake()

    def on_esc(self):
        message: str = "Key: ESC (Quit)"
        log.info(message)
        print(message)
        self._simulation_running = False
