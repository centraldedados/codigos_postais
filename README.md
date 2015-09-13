Nesta datapackage encontra-se a lista completa de códigos postais em Portugal
(continente e regiões autónomas), com mais de 300000 entradas.


Fontes
------

Os dados foram convertidos a partir dos ficheiros de texto [disponibilizados no
site dos
CTT](https://www.ctt.pt/feapl_2/app/restricted/postalCodeSearch/postalCodeDownloadFiles.jspx).
O acesso requer o registo e o log-in antes de poder ver a página de download.


Pormenores
----------

O ficheiro de códigos postais contém 3 tipos de entradas:

* Clientes dos CTT com código postal próprio
* Localidades
* Arruamentos e troços de rua


Licença
-------

Presume-se que a informação aqui contida é de caráter público, e como tal ela é
aqui republicada de acordo com os termos da
[PDDL](http://opendatacommons.org/licenses/pddl/) (Licença de Base de Dados de
Domínio Público).


Edição
------

  * [Ricardo Lafuente](http://twitter.com/rlaf)


Detalhes técnicos
-----------------

O dataset original foi filtrado e simplificado para criar o CSV que se inclui nesta data package.
O comando para essa filtragem é:

    csvcut codigos_postais-orig.csv -c localidade,cod_arteria,tipo_arteria,prep1,titulo_arteria,prep2,nome_arteria,local_arteria,troco,porta,cliente,cod_postal,extensao_cod_postal,designacao_postal > codigos_postais.csv

(É necessário ter o [csvkit](https://csvkit.readthedocs.org) instalado para
poder executar esta operação.)


Agradecimentos
--------------

  * [João Antunes](http://twitter.com/joao), por ter [apontado o caminho
    certo](https://twitter.com/joao/status/572809514388471809) no Twitter

