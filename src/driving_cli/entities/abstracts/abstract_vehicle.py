"""File for Car class and its complements."""
from abc import ABC
from enum import Enum
from typing import Type
from logging import Logger, getLogger

from driving_cli.entities.abstracts.abstract_transmission import ATransmission
from driving_cli.entities.abstracts.abstract_throttle import Throttle
from driving_cli.entities.abstracts.abstract_brake import Brake
from driving_cli.entities.abstracts.abstract_engine import Engine
from driving_cli.entities.abstracts.abstract_energy_provider import AEnergyProvider
from driving_cli.use_cases.validators import clamp_value


log: Logger = getLogger(__name__)


class AVehicle(ABC):
    """
    Abstract vehicle class.
    """
    _weight: float = 0.0
    _speed: float = 0.0
    _acceleration: float = 0.0
    _throttle: Throttle = None
    _brake: Brake = None
    _engine: Engine = None
    _energy_provider: Type[AEnergyProvider] = None
    _transmission: ATransmission = None

    class Constants(Enum):
        SPEED_MAX = 500.0
        SPEED_MIN = 0.0
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
        self._acceleration =  clamp_value(value=raw_acceleration,
                                          min_value=self.Constants.ACCELERATION_MIN.value,
                                          max_value=self.Constants.ACCELERATION_MAX.value,
                                          name="Acceleration"
                                          )
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
    def transmission(self) -> ATransmission:
        return self._transmission

    @property
    def weight(self) -> float:
        """Sum of weight of vehicle part."""
        return self._weight

    def __init__(self, throttle: Throttle,
                 brake: Brake,
                 engine: Engine,
                 energy_provider: Type[AEnergyProvider],
                 transmission: ATransmission):
        self._throttle: Throttle = throttle
        self._brake: Brake = brake
        self._engine: Engine = engine
        self._energy_provider: Type[AEnergyProvider] = energy_provider
        self._transmission: ATransmission = transmission
        self._weight: float = (self.throttle.weight +
                               self.brake.weight +
                               self.engine.weight +
                               self.energy_provider.weight)
        self._speed: float = 0

    # classify_by_weight()
    # vehicle_types

    @classmethod
    def constants(cls):
        return cls.Constants

    @classmethod
    def increase_throttle(cls) -> None:
        """Increases vehicle throttle instance throttle value and resets brake."""
        cls._brake.reset_brake()
        cls._throttle.increase_throttle()

    @classmethod
    def decrease_throttle(cls) -> None:
        """Increases vehicle throttle instance throttle value."""
        cls._throttle.decrease_throttle()

    @classmethod
    def engage_brake(cls) -> None:
        """Increase vehicle brake instance brake value and reset throttle."""
        cls._throttle.reset_throttle()
        cls._brake.engage_brake()

    @classmethod
    def disengage_brake(cls) -> None:
        """Decrease vehicle brake instance brake value."""
        cls._brake.disengage_brake()

    # @abstractmethod
    # def drive(self) -> None:
    #     """Subclasses must implement driving logic."""
    #     pass

    @classmethod
    def accelerate(cls) -> None:
        """Increases speed using throttle and engine force and gear_ratio."""
        gear_ratio: float = cls._transmission.ratio
        throttle_value: float = cls._throttle.throttle_value
        cls._engine.increase_combustion(throttle_value, gear_ratio)
        new_speed: float = cls._acceleration + cls._speed
        cls._speed = clamp_value(value=new_speed,
                                 min_value=cls.Constants.SPEED_MIN.value,
                                 max_value=cls.Constants.SPEED_MAX.value,
                                 name="Speed"
                                 )

    # @abstractmethod
    # def hamper_by_frictions(self) -> None:
    #     """Reduces speed due to natural forces when engine force is not actively overcoming them."""
    #     # friction, drag
    #     pass

    @classmethod
    def hamper_by_brake(cls) -> None:
        """Reduce speed according to brake intensity."""
        delta = max(cls._speed - cls._brake.brake_value * cls._brake.effectiveness, 0.0)
        cls._speed = clamp_value(value=delta,
                                 min_value=cls.Constants.SPEED_MIN.value,
                                 max_value=cls.Constants.SPEED_MAX.value,
                                 name="Speed"
                                 )

    @classmethod
    def decrease_energy_volume(cls):
        """Reduces volume of energy provider by engine combustion."""
        log.info("Decreasing energy volume")
        value: float = min(cls._energy_provider.volume - cls._engine.combustion, 0.0)
        cls._energy_provider.volume = value
