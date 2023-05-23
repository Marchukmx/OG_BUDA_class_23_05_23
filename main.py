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

try:
    print(10/0)
except Exception:
    logging.exception("помилка(")


def factorial(n):
    logging.info(f"Розпочато обчислення факторіалу {n}")
    result = 1
    for i in range(1,n+1):
        result *= i
    logging.info(f"Завершено обчислення факторіалу {n}"
                 f"Результат виконання :{result}")
    return result
logging.basicConfig(level=logging.INFO)
factorial(5)