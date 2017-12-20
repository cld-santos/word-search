import time
from .searcher import WordSearch
from .loader import WordLoader, FileSystemLoader


class SearchLayer():

    def pre_process(self):

        word_loader = WordLoader()
        word_searcher = WordSearch(FileSystemLoader(word_loader), word_loader)
        word_searcher.pre_process()
        word_searcher.dump()

    def search(self, search_term):
        word_loader = WordLoader()
        word_searcher = WordSearch(FileSystemLoader(word_loader), word_loader)
        original_term = search_term

        # Este processo foi removido intencionalmente da contabilidade de tempo 
        # levado para pesquisa, por se tratar de uma tarefa simples de leitura,
        # o que varia bastante entre os diferentes tipos de hardwares.  
        word_searcher.load_cache()

        start = time.time()
        occurrences = word_searcher.search(original_term)
        elapsed = time.time() - start

        return (occurrences.split('\n'), round(elapsed, 4))
