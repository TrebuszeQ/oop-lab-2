from enum import Enum


class CliSteering(Enum):
    DT: float = 0.02
    SPEED: float = 0.0
    DIRECTION: float = 0.0
    ACCELERATION: float = 2.0
    TURN_SPEED: float = 90.0
    DRAG: float = 0.98
