# word-search

Este toy-project tem o objetivo de avaliar os mecanismos para executar uma pesquisa por palavras em uma grande quantidade de arquivos, então dada uma palavra o objetivo é encontra-la em menos de 0.01 segundos.

Para isso os usuário podem executar os commandos:

```
$ python3.5 word-search load_files
$ python3.5 word-search o'reilly books

```

Recebendo a resposta:

```
$ word search took 0.009534
	meu-arquivo-um.txt          100%
	meu-arquivo-dois.txt         75%
	meu-arquivo-dois.txt         65%
```

O processo de pontuação determina os percentuais pela ordem e sequência das palavras pesquisadas, desta forma se encontrarmos o termo como ele foi pesquisado a busca recebe sua pontuação maxima, se o termo de pesquisa for encontrado na mesma sequencia recebe uma pontuação de 85% e caso os termos sejam encontrados em sequencia distinta sua pontuação é de 65% indicando que esta busca pode ter pouca relevância, poderíamos utilizar as seguintes pontuações para encontrar o termo em forma quebrada, encontrando cada palavra isoladamente, porém este não é o foco deste projeto.
