# learn_django
estudando o tutorial de exemplo fornecido no 
[site do django](https://docs.djangoproject.com/en/4.2/intro/tutorial01/): 

**aplicação de enquetes**

## check-list para inicia um projeto em django

- ao iniciar um projeto use o seguinte comando:
```bash
$ django-admin startproject [nome_do_projeto]
```

- para criar uma aplicação, entre dentro da pasta do projeto criada anteriormente `cd [nome_do_projeto]`. nela use o seguinte comando para criar um app:
```bash
$ python manage.py startapp [nome_do_app]
```

- você precisará colocar os apps criados no arquivo de configuração do seu projeto `nome_do_projeto/settings.py`. nesse arquivo na parte `INSTALLED_APPS` e colocar da seguinte maneira:

```python
INSTALLED_APPS = [
  '[nome_do_app].apps.[Nome_do_app]Config',
  '[nome_do_app1].apps.[Nome_do_app1]Config',
  '[nome_do_app2].apps.[Nome_do_app2]Config',
  ...
]
```

apos colocar todos os apps criados no arquivo de configuração do seu projeto, nos podemos rodar o comando:

```bash
$ python manage.py migrate
```

este comando criará todas as tabelas necessárias para seu projeto no seu banco de dados.

## ajustando as configurações de url

Em cada app criado, você terá que criar um novo arquivo chamado `urls.py`. nele você terá que colocar as urls do determinado app. um exemplo do arquivo `polls/urls.py`:

```python
from django.urls import path

app_name = "polls"
urlpatterns = [
  path("", <view>, name="[nome_do_url]"),
]
```

no diretorio de seu projeto, no arquivo `urls.py`, importe o metodo include e coloque no path. veja um exemplo com o app polls:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
]
```

## criando um model 

- quando você tiver criado seus models, para que as tabelas sejam criadas você deve executar os seguintes comandos: 

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

- para rodar o servidor, esteja no mesmo diretorio do arquivo `manage.py` _(interface para trabalhar com o terminal)_:

```bash
$ python manage.py runserver
```

- criando um super usuário para gerenciar a aplicação:

```bash
$ python manage.py createsuperuser
```

- para adicionar um model na pagina de administração:
`cd polls/admin.py`

```python
from .models import Question

admin.site.register(Question)
```
- atalho para carregar um template e retornar um HttpResponse com o resultado: ultilize o render(request, [url do template], context)

- quando você quiser ultilizar variaveis no html use `{{}}` já para colocar codigo python use: `{% [codigo python] %}`

## parte 4 - generic views

### usando views genéricas:

para realizar a mudança de uma view padrão para uma genérica é preciso analisar se essa view se encaixa como uma `generic view`.

para realizar a mudança de uma view comum para uma view genérica basta fazer o seguinte:
- modificar a urlconfig
- deletar algumas views desnecessárias
- aplicar novas views baseado nas generics views: as view antigas que eram definidas por funções agora deveram ser classes.

***cada view generica deve saber qual modelo ela vai agir, por isso é usado o atributo `model`****

***para mudar o nome do template use `template_name`***

1. **generic.ListView**: view genérica para listagem de elementos. alguns detalhes:
  1. para alterar o nome do context use `context_object_name`, e aplique a funcao:
```python 
  def get_queryset(self):
    return [retorne algo]
```
2. **generic.DetailView**: view genérica para mostrar detalhes sobre algo. 

## parte 5 - testes

escrever testes é uma boa pratica. `test-driven development` é uma disciplina que realiza a parte dos testes antes ds escrever os codigos da sua aplicação.

- seus testes devem ser criados no arquivo: `tests.py`.
- crie uma subclasse de django.test.Testcase com essa base:
```python
class [Nomedomodel]ModelTest(TestCase):
```
- nesta subclasse, crie uma função de teste que comece com a palavra `test`, logo em seguida com o nome da função a ser testada e juntamente com o tipo de teste.
***testando a função soma***

```python
def test_soma_com_numeros_negativos(self):
  a = -5
  b = -7
  assertIs(soma(a,b), -12)
```

- use o metodo .assertIs():
```python
self.assertIs([funcao a ser testada], [valor correto que deveria retornar])
```

- execute o teste com este comando:
```bash
$ python manage.py test polls
```

## parte 6 - arquivos estáticos

para usar arquivos estaticos (css, js) faça:
- crie uma pasta `static` no diretorio de sua aplicação;
- dentro dela crie uma subpasta `nome_da_aplicaçao`;
- nessa subpasta adicione os arquivos estáticos: `style.css`, `main.js`;
- nos seus templates faça:
  - no topo coloque `{% load static %}`;
  - no link do css por exemplo coloque: `{% static 'nome_da_aplicacao/style.css' %}`

## parte 7 - modificando a parte de admin

## parte 8 - ferramenta de depuração
