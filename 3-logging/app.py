import logging 

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s- %(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger=logging.getLogger("ArithematicApp")

def add(a,b):
    result=a+b
    logger.debug(f"adding {a}+{b}={result}")
    return result

def multiply(a,b):
    result=a+b
    logger.debug(f"multiply {a}*{b}={result}")
    return result

def subtract(a,b):
    result=a-b
    logger.debug(f"subtracting {a}-{b}={result}")
    return result


def division(a,b):
    try:
        result=a/b
        logger.debug(f"division {a}/{b}={result}")
        return result
    except ZeroDivisionError:
        logger.error("division by zero error")
        return None

add(10,15)
subtract(15,9)
multiply(23,67)
division(20,0)
