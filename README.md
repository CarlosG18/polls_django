# learn_django
estudando o tutorial de exemplo fornecido no site do django: 

**aplicação de enquetes**

- para criar um novo projeto em django use:

```bash
 $ django-admin startproject [nome_do_projeto]
```
- para rodar o servidor, esteja no mesmo diretorio do arquivo manage.py(interface para trabalhar com o terminal):

```bash
$ python manage.py runserver
```
- para criar uma aplicação:

```bash
$ python manage.py startapp [nome da aplicação]
```
- criando um super usuário para gerenciar a aplicação:

```bash
$ python manage.py createsuperuser
```

- para adicionar um model na pagina de administração:
cd polls/admin.py

```python
from .models import Question

admin.site.register(Question)
```
- atalho para carregar um template e retornar um HttpResponse com o resultado: ultilize o render(request, [url do template], context)

- quando você quiser ultilizar variaveis no html use {{}} já para colocar codigo python use: {% for i in range(5) %}

## parte 4 (trabalhando com forms)

- para adicionar estilos voce precisa definir arqyivos estaticos. para isso defina um diretorio 'static' e nele coloque os arquivos editaveis. no template faça:

> {% load static %} 

