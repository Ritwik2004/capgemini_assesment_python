from app_logger import logger

class SignalController:
    def operate(self, signal):
        logger.info(f"Signal Controller started for {signal.signal_type()}")
        time = signal.green_time()
        logger.info(f"{signal.signal_type()}--> Green for {time} second..")
        logger.info(f"Signal Controller operation Completed")