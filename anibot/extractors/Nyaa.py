from .RSSExtractor import RSSExtractor

class Nyaa(RSSExtractor):
    name,url = "Nyaa", "https://nyaa.si/?page=rss"
    extid = "a9329e6c-30a6-471c-924c-cfb2ac93fe92"
    lastID, polling = 0, 60
    def filter(self, raw):
        output = []
        for entry in raw:
            entry['id'] = int(entry['guid'].replace('https://nyaa.si/view/',''))
            if entry['id'] > self.lastID:
                output.append(entry)
        if output:
            self.lastID = output[-1]['id']
            return output
        return []
    def poll(self):
        return self.filter(self.raw())
