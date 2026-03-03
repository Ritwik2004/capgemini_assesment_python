from app_logger import logger
from abc import ABC, abstractmethod

class TrafficSignal():
    def __init__ (self, vechicle_count):
        self._vechicle_count = vechicle_count
        logger.info(f"Traffic signal created with vechicle count = {vechicle_count}")
    
    @abstractmethod
    def green_time(self):
        pass

    @abstractmethod
    def signal_type(self):
        pass