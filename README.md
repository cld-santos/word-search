# word-search

Este toy-project tem o objetivo de avaliar os mecanismos para executar uma pesquisa por palavras em uma grande quantidade de arquivos, então dada uma palavra o objetivo é encontra-la em menos de 0.01 segundos.

Para isso os usuário podem executar os commandos:

```
$ python3.5 search pre-process
$ python3.5 search.py "walt disney"

```

Recebendo a resposta:

```
Foram encontradas em 0.0091 segs, 53 ocorrências pelo termo "walt disney".
the-four-musicians-of-bremen.txt
perri.txt
how-to-have-an-accident-at-work.txt
the-jazz-fool.txt
mickey-s-elephant.txt
el-gaucho-goofy.txt
tugboat-mickey.txt
the-nifty-nineties.txt
tommy-tucker-s-tooth.txt
fathers-are-people.txt
donald-s-dream-voice.txt
dog-watch.txt
great-guns.txt
football-now-and-then.txt
self-control.txt
good-scouts.txt
funny-little-bunnies.txt
the-merry-dwarfs.txt
a-cowboy-needs-a-horse.txt
bootle-beetle.txt
canine-caddy.txt
alice-s-fishy-story.txt
how-to-be-a-sailor.txt
sky-scrappers.txt
the-hockey-champ.txt
alice-and-the-three-bears.txt
gallopin-gaucho.txt
billposters.txt
spare-the-rod.txt
on-ice.txt
donald-s-snow-fight.txt
cured-duck.txt
alpine-climbers.txt
bone-trouble.txt
father-noah-s-ark.txt
the-mail-pilot.txt
moochie-of-pop-warner-football.txt
the-little-house.txt
the-pet-store.txt
working-for-peanuts.txt
goofy-and-wilbur.txt
tall-timber.txt
fall-out-fall-in.txt
dude-duck.txt
pantry-pirate.txt
society-dog-show.txt
wide-open-spaces.txt
jiminy-cricket-s-christmas.txt
alice-helps-the-romance.txt
cock-o-the-walk.txt
undiscovered-walt-disney-world.txt
clown-of-the-jungle.txt
two-gun-mickey.txt

```

Este algoritmo utiliza os recursos nativos da biblioteca do Python versão 3.5 e simula um mecanismo de indexação, esta indexação ocorre no pré-processamento, neste momento os indices são criados na pasta _cache/_: 
 - words.txt a lista de todas as palavras encontradas;
 - files.txt eh a lista de todos os arquivos que foram lidos pelo pré-processamento;
 - words\_files.txt eh uma relação _de para_ onde a posição da linha de cada registro é igual a posição das palavras no arquivo words.txt, desta forma eh fácil obter a lista de arquivos em que aquela palavra foi encontrada;

Após o este processamento, podemos realizar nossa pesquisa em um bom desempenho. A pesquisa carrega o cache e acessa o _dict_ de palavras e usa uma função recursiva para encontrar os diferentes termos, então a partir do set de endereços que as palavras foram encontradas fazemos um _intersecction_ destes e o que resta são os arquivos com ocorrências das palavras.

Mais informações consulte o [kanban do projeto](https://trello.com/b/WpJg5TnO/word-search) e o [próprio desafio](https://gist.github.com/Bgouveia/f4ee3ffdae96255f79f1da57e45cc559)