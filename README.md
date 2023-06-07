# SISTEMA DE DELIVERY


## Tecnologias Utilizadas:

* ### Python
* ### Django
* ### Git
* ### PostgreSQL
* ### Docker


## Funcionalidades do Projeto
1. #### Página que apresenta todos os itens a venda e possibilitade de filtrar de acordo com a categoria
2. #### Página de vizualização dos detalhes de um produto específico
3. #### Vizualização de carrinho de compras que mostra os itens selecionados pelo usuário e suas respectivas quantidades bem como o total da compra em valores monetários
4. #### Formulário para iserção de endereço e forma de pagamento para conclusão da compra

## Instruções para instalação:

### Faça o clone do projeto:
```commandline
git clone git@github.com:JulianaRaquel/SISTEMA_DELIVERY.git
```
### Criar o ambiente virtual (venv):
```commandline
python3 -m venv venv
```
### Ativar o ambiente virtual no linux:
```commandline
source venv/bin/activate
```
### Ativar o ambiente virtual no windows:
```commandline
venv\Scripts\Activate
```
### Instalar Dependências:
```commandline
pip install -r requirements.txt
```
### Copiar as variáveis de ambiente:
```commandline
cp .env.example .env
```
### Aplicar as migrações:
```commandline
python3 manage.py migrate
```
### Rodar servidor do Django:
```commandline
python3 manage.py runserver
```