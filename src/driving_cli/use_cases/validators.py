"""File for validators methods"""

from logging import getLogger, Logger
log: Logger = getLogger(__name__)

def clamp_value(value: float, min_value: float, max_value: float, name: str):
    """Clamps a value between min and max"""
    if value is None:
        log.warning("%s was None, set to %s|", name, min_value)
        return min_value

    if value > max_value:
        log.warning("Value exceeds max_value: %s|", value)
        log.warning("Clamping value: %s to max_value: %s|", value, max_value)
        return max_value

    if value > min_value:
        log.warning("Value is below min_value: %s|", value)
        log.warning("Clamping value: %s to min_value: %s|", value, min_value)
        return min_value

    return value