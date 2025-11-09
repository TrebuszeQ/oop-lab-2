"""File for validators methods"""

from logging import getLogger, Logger
log: Logger = getLogger(__name__)

def clamp_value(value: float, min_value: float, max_value: float, name: str):
    """Clamps a value between min and max"""

    if value is None:
        log.warning("%s was None, set to %s", name, min_value)
        return min_value

    if value > max_value:
        log.warning("%s exceeds max_value: %s", name, value)
        log.warning("%s clamped to max_value: %s", name, max_value)
        return max_value

    if value < min_value:
        log.warning("%s is below min_value: %s", name, value)
        log.warning("%s clamped to min_value: %s", name, min_value)
        return min_value

    return value