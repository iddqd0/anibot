import logging, threading, time
from .. import AniBot
from ..util import AnibotEvent

class Extractor(threading.Thread):
    """
    :type bot: AniBot.AniBot
    """
    name = "Dummy Extractor"
    extid = "00000000-0000-0000-0000-000000000000"
    bot = None
    def run(self):
        pass
    def raw(self):
        return []
    def filter(self, raw):
        return []
    def matched(self, user):
        return []
    def poll(self):
        return []

