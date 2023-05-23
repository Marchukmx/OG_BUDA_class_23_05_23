import logging

logging.basicConfig(level=logging.DEBUG ,
                    filename = "logs.log" ,
                    filemode = "w" ,
                    format = '%(asctime)s - %(levelname)s - %(message)s')

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("Погано написав програму - ERROR")
logging.critical("critical")