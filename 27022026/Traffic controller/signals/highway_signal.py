from signals.base_signal import TrafficSignal
from app_logger import logger
from config import (
    HIGHWAY_HIGH_GREEN_TIME,
    HIGHWAY_LOW_GREEN_TIME,
    HIGHWAY_SIGNAL_TRAFFIC_LIMIT
)

class HighwaySignal(TrafficSignal):
    def green_time(self):
        logger.info(f"Calculating green time for highway signal")
        if self._vechicle_count <HIGHWAY_SIGNAL_TRAFFIC_LIMIT:
            return HIGHWAY_LOW_GREEN_TIME
        return HIGHWAY_HIGH_GREEN_TIME
    
    def signal_type(self):
        return "Highway Signal"
    
