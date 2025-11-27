from abc import ABC, abstractmethod


class OSHandler(ABC):

    @property
    @abstractmethod
    def home_dir(self) -> str:
        pass
    
    @property
    @abstractmethod
    def scan_hidden(self) -> bool:
        pass



"""
    @abstractmethod
    def get_home_dir(self) -> str:
        pass
"""