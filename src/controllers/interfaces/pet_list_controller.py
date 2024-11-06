from abc import ABC, abstractmethod
from typing import Dict


class PetListControllerInterface(ABC):

    @abstractmethod
    def list(self) -> Dict:
        pass
