from .util import *

class AniBot:
    extractors = []
    telegram = dict(key='',interface=None)
    debug = False
    def __init__(self,key,extractors,debug=False):
        self.debug = debug

        # Setting the key
        self.telegram['key'] = key
        # Initialization
        #self.telegram['interface'] = Telegram()
        for ext in extractors:
            extractor = ext()
            self.registerExtractor(extractor)
    def run(self):
        setupLogging("test.log", self.debug)
        #self.telegram['interface'].run()
        for ext in self.extractors:
            ext.start()
    def event(self, event):
        if event.event == AnibotEvent.EXTRACTOR_INPUT:
            logging.getLogger(__name__).debug("{} [{}] -> {} entries".format(event.source.name, event.source.extid, len(event.data)))

    def registerExtractor(self, extractor):
        if extractor in self.extractors:
            raise SetupException("Could not register extractor [{}] ({}) , as it already exists.".format(extractor.extid, extractor.name))
        extractor.bot = self
        self.extractors.append(extractor)

