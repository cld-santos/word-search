import sys
from word_search.services import SearchLayer

if __name__ == '__main__':
    search_layer = SearchLayer()
    if sys.argv[1] == 'pre-process':
        print('Aguarde alguns minutos...')
        search_layer.pre_process()
        print('Pré-processamento completado com sucesso.')            
    else:
        search_term = sys.argv[1]
        try:
            ocurrences, time_elapsed = search_layer.search(search_term)
        except Exception as e:
            print(str(e))
            return

        if occurrences:
            print('Foram encontradas em {2} segs, {0} ocorrências pelo termo "{1}".'.format(
                len(ocurrences.split('\n'))-1, search_term, time_elapsed)
            print(occurrences)
        else:
            print('Não foram encontradas ocorrências do termo "{0}".'.format(search_term))
