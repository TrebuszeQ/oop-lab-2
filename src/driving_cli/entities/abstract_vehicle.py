"""File for Car class and its complements."""
from abc import ABC, abstractmethod
from enum import Enum
from typing import Type
from logging import Logger, getLogger

from driving_cli.entities.transmission import Transmission
from throttle import Throttle
from brake import Brake
from engine import Engine
from abstract_energy_provider import AEnergyProvider

log: Logger = getLogger(__name__)


class AVehicle(ABC):
    """
    Abstract vehicle class.
    """
    _weight: float = None
    _speed: float = None
    _acceleration: float = None
    _throttle: float = None
    _brake: float = None
    _engine: float = None
    _energy_provider: float = None

    class Constants(Enum):
        MAX_SPEED = 80.0
        MIN_SPEED = 0.0
        ACCELERATION_MAX = 1.0
        ACCELERATION_MIN = 0.0

    @property
    def speed(self) -> float:
        return self._speed

    @property
    def acceleration(self) -> float:
        if self.weight <= 0:
            log.warning("Invalid weight: %s", self.weight)
            return 0.0
        effective_force = self.engine.force * self.engine.combustion
        raw_acceleration: float = effective_force / self.weight
        self._acceleration =  self._validate_acceleration(raw_acceleration)
        return self._acceleration

    @property
    def throttle(self) -> Throttle:
        return self._throttle

    @property
    def brake(self) -> Brake:
        return self._brake

    @property
    def engine(self) -> Engine:
        return self._engine

    @property
    def energy_provider(self) -> Type[AEnergyProvider]:
        return self._energy_provider

    @property
    def transmission(self) -> Transmission:
        return self._transmission

    @property
    def weight(self) -> float:
        """Sum of weight of vehicle part."""
        return self._weight

    def __init__(self, throttle: Throttle,
                 brake: Brake,
                 engine: Engine,
                 energy_provider: Type[AEnergyProvider],
                 transmission: Transmission):
        self._weight: float = (self.throttle.weight +
                self.brake.weight +
                self.engine.weight +
                self.energy_provider.weight)
        self._speed: float = 0
        self._throttle: Throttle = throttle
        self._brake: Brake = brake
        self._engine: Engine = engine
        self._energy_provider: Type[AEnergyProvider] = energy_provider
        self._transmission: Transmission = transmission

    @classmethod
    def _validate_speed(cls, speed) -> float:
        """
        Validates speed argument.
        If argument is below MIN_SPEED or None it defaults to MIN_SPEED.
        If argument is above MAX_SPEED it defaults to MAX_SPEED.
        :param speed: Given speed
        :return: Returns validated speed between MIN and MAX speed inclusively.
        """
        max_speed: float = cls.Constants.MAX_SPEED.value
        min_speed: float = cls.Constants.MIN_SPEED.value
        if speed > max_speed:
            log.warning("Vehicle speed is greater than: %s", max_speed)
            log.warning("Vehicle speed set to: %s", max_speed)
            speed = max_speed
        elif speed < 0:
            log.warning("Vehicle speed cannot be less than: %s", min_speed)
            log.warning("Vehicle speed set to: %s", max_speed)
        return speed

    @classmethod
    def _validate_acceleration(cls, acceleration: float):
        max_value: float = cls.Constants.ACCELERATION_MAX.value
        min_value: float = cls.Constants.ACCELERATION_MIN.value
        param: str = "Acceleration"

        if acceleration > max_value:
            log.warning("%s cannot be greater than: %s|", param, max_value)
            log.warning("%s set to: %s|", param, max_value)
            acceleration = max_value
        elif acceleration < min_value or acceleration is None:
            log.warning("%s cannot be less than: %s|", param, min_value)
            log.warning("%s set to: %s|", param, min_value)
            acceleration = min_value
        return acceleration

    # classify_by_weight()
    # vehicle_types

    @classmethod
    def constants(cls):
        return cls.Constants

    def accelerate(self) -> None:
        """Increase speed using throttle and engine force."""
        gear_ratio: float = self._transmission.ratio
        throttle_value: float = self._throttle.throttle_value
        self._engine.increase_combustion(throttle_value, gear_ratio)
        self._speed = self._validate_speed(self._speed + self._acceleration)

    def apply_brake(self) -> None:
        """Reduce speed according to brake intensity."""
        delta = max(self._speed - self._brake.throttle_value, 0.0)
        self._speed = self._validate_speed(delta)

    @abstractmethod
    def drive(self) -> None:
        """Subclasses must implement driving logic."""
        pass