# learn_django
estudando o tutorial de exemplo fornecido no 
[site do django](https://docs.djangoproject.com/en/4.2/intro/tutorial01/): 

**aplicação de enquetes**

- para criar um novo projeto em django use:

```bash
 $ django-admin startproject [nome_do_projeto]
```
- para rodar o servidor, esteja no mesmo diretorio do arquivo `manage.py` _(interface para trabalhar com o terminal)_:

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
`cd polls/admin.py`

```python
from .models import Question

admin.site.register(Question)
```
- atalho para carregar um template e retornar um HttpResponse com o resultado: ultilize o render(request, [url do template], context)

- quando você quiser ultilizar variaveis no html use `{{}}` já para colocar codigo python use: `{% [codigo python] %}`

## parte 4

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

## parte 5

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

## parte 6
