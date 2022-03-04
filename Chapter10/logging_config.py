import logging
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename="log1.log",level=logging.DEBUG,format=LOG_FORMAT)

logging.log(logging.DEBUG,"I am a debug level log.")
logging.log(logging.INFO,"I am a info level log.")
logging.log(logging.WARNING,"I am a warning level log.")
logging.log(logging.ERROR,"I am a error level log.")
logging.log(logging.CRITICAL,"I am a critical level log.")