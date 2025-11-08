from abc import ABC, abstractmethod
from driving_cli.entities.abstracts.abstract_vehicle import AVehicle
from logging import getLogger, Logger

log: Logger = getLogger(__name__)

class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: AVehicle) -> None:
        """
        Receive update from subject
        :param: Concrete subject class
        :return:
        """
        log.info("Received update from subject")
        pass