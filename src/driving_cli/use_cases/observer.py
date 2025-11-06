from abc import ABC, abstractmethod
from vehicle import Vehicle
from logging import getLogger, Logger

log: Logger = getLogger(__name__)

class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: Vehicle) -> None:
        """
        Receive update from subject
        :param: Concrete subject class
        :return:
        """
        log.info("Received update from subject")
        pass