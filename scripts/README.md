Scraper dos códigos postais
===========================

Este scraper acede gentilmente ao site dos CTT e vai buscar o ficheiro de texto com os códigos postais.

Instalar
--------

Antes de correr, é preciso tratar das dependências:

    make install
    
Este scraper usa o [splinter](http://splinter.readthedocs.io) para correr o Chromium. Também é necessária a package `chromedriver`, que deve estar disponível no package manager do sistema operativo. Caso ele dê o erro

    'chromedriver' executable needs to be in PATH. Please see https://sites.google.com/a/chromium.org/chromedriver/home

é preciso apontar o executável dentro do nosso `$PATH`.

    sudo ln -s /usr/lib/chromium/chromedriver /usr/local/bin/

Depois de tratar da instalação, precisamos de editar as credenciais para acrescentar o nosso username e password no CTT.pt. É só copiar o `credenciais.ini.sample` para `credenciais.ini` e editar o ficheiro.

Usar
----

Agora é só

    make scrape

E está sacado. Se quisermos fazer um commit automático e um push, só temos de

    make deploy
