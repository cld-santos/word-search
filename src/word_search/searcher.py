import linecache


class WordSearch():

    def __init__(self, source_loader, item_loader):
        self.source_loader = source_loader
        self.item_loader = item_loader

    def pre_process(self):
        self.source_loader.load()

    def dump(self):
        self.source_loader.dump()

    def load_cache(self):
        self.source_loader.load_cached_words()

    def search(self, words):
        search_term = words.split(' ')
        search_term = [search_term] if isinstance(search_term, str) else search_term
        search_term = [word.lower() for word in search_term]
        
        files = self._search_words(search_term)
        occurrences = ""
        for file in files:
            occurrences += linecache.getline(self.source_loader.cache_dir + 'files.txt', int(file)+1)
        return occurrences

    def _search_words(self, words):
        try:
            word_index = self.source_loader.cached_words.index(words.pop(0) + '\n')
        except:
            return ()

        word_files_indexs = linecache.getline(self.source_loader.cache_dir + 'words_files.txt', int(word_index)+1)
        intersection = frozenset(word_files_indexs[:-1].split(','))
        if words:
            return intersection & self._search_words(words)
        else:
            return intersection
