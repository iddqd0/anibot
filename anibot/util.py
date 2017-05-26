import logging
import logging.handlers
import sys


def setupLogging(filename,debug=False):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    rootLogger = logging.getLogger()
    fileHandler = logging.handlers.RotatingFileHandler(filename, maxBytes=(1048576 * 5), backupCount=7)
    rootLogger.addHandler(fileHandler)

    if debug:
        consoleHandler = logging.StreamHandler(sys.stdout)
        #rootLogger.addHandler(consoleHandler)
        rootLogger.setLevel(logging.DEBUG)

def AnibotExceptionHook(extype, value, traceback):
    if issubclass(extype, AnibotException):
        logging.getLogger(__name__).error("Error! ----> {}".format(value))
        logging.getLogger(__name__).debug("Start traceback ->\n{}\n<- End traceback".format(traceback))
    else:
        sys.__excepthook__(extype, value, traceback)

class AnibotException(Exception):
    pass

class TelegramException(AnibotException):
    pass

class DatabaseException(AnibotException):
    pass

class RSSException(AnibotException):
    pass

class SetupException(AnibotException):
    pass

class UIException(AnibotException):
    pass

class AnibotEvent:
    EXTRACTOR_INPUT = 0
    TELEGRAM_MSG = 1
    def __init__(self, event, data, source):
        self.event = event
        self.data = data
        self.source = source
