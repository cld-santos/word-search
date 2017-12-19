import sys
import time
from word_search.searcher import WordSearch
from word_search.loader import WordLoader, FileSystemLoader

if __name__ == '__main__':

    if sys.argv[1] == 'pre-process':
        print('Aguarde alguns minutos...')
        word_loader = WordLoader()
        word_searcher = WordSearch(FileSystemLoader(word_loader), word_loader)
        word_searcher.pre_process()
        word_searcher.dump()
        print('Pré-processamento completado com sucesso.')
    else:
        word_loader = WordLoader()
        word_searcher = WordSearch(FileSystemLoader(word_loader), word_loader)
        original_term = sys.argv[1]
        word_searcher.load_cache()

        start = time.time()
        occurrences = word_searcher.search(original_term)
        elapsed = time.time() - start

        if occurrences:
            print('Foram encontradas em {2} segs, {0} ocorrências pelo termo "{1}".'.format(
                len(occurrences.split('\n'))-1,
                original_term,
                round(elapsed, 4)))
            print(occurrences)
        else:
            print('Não foram encontradas ocorrências do termo "{0}".'.format(original_term))