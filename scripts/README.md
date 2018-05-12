Scraper dos códigos postais
===========================

Este scraper acede gentilmente ao site dos CTT e vai buscar o ficheiro de texto com os códigos postais.

Antes de correr, é preciso tratar das dependências:

    make install
    
Este scraper usa o [splinter](http://splinter.readthedocs.io) para correr o Chromium. À partida todas as dependências devem estar resolvidas com o `make install`.

Depois de tratar da instalação, precisamos de editar as credenciais para acrescentar o nosso username e password no CTT.pt. É só copiar o `credenciais.ini.sample` para `credenciais.ini` e editar o ficheiro.

Agora é só

    make scrape

E está sacado. Se quisermos fazer um commit automático e um push, só temos de

    make deploy
