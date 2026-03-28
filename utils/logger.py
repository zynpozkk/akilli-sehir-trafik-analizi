import logging

class TrafficLogger:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TrafficLogger, cls).__new__(cls)
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
            cls._instance.logger = logging.getLogger("TrafficApp")
        return cls._instance