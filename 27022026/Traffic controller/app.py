from signals.city_signal import CitySignal
from signals.highway_signal import HighwaySignal
from Controller.controller import SignalController
from app_logger import logger

logger.info(f"Traffinc Simulation Started...")

controller = SignalController()

no_vechicle = int(input("Enter number of vechicle : "))

city_signal = CitySignal(no_vechicle)
Highway_signal = HighwaySignal(no_vechicle)
controller.operate(city_signal)
controller.operate(Highway_signal)

logger.info(f"Simulation complited")