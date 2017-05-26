import time, feedparser
from ..util import AnibotEvent
from .Extractor import Extractor

class RSSExtractor(Extractor):
    name, url = "Dummy RSS Extractor", ""
    polling = 600
    def raw(self):
        if self.url:
            feed = feedparser.parse(self.url)
            return feed.entries
    def run(self):
        while True:
            data = self.poll()
            if data:
                self.bot.event(event=AnibotEvent(event=AnibotEvent.EXTRACTOR_INPUT, data=data, source=self))
            time.sleep(self.polling)

