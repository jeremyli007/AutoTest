import logging

class LogStudy:
    LOG_FORMAT="%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(filename='../result/my.log',level=logging.DEBUG,format=LOG_FORMAT)

    logging.debug("this is a bug!")
    logging.info("this is a bug!")
    logging.warning("2")
    logging.error("this is a bug!")
    logging.critical("4")

if __name__ == '__main__':
    LogStudy()