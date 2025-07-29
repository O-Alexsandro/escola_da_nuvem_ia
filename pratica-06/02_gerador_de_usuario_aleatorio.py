"""
2- Gerador de Usuário Aleatório  
Crie um programa que acessa uma API pública e exibe informações de um usuário fictício. Para isso:

* Use a API pública "https://randomuser.me/api/" para obter dados aleatórios.  
* Mostre na tela: nome completo, e-mail e país do usuário.  
* O programa deve tratar possíveis erros de conexão ou falha na API.  

Dica: Utilize o módulo `requests` para fazer a requisição e o método `.json()` para acessar os dados.
"""

import requests

try:
    response = requests.get('https://randomuser.me/api/')

    if response.status_code == 200:
        dados = response.json()['results'][0]

        nome = dados['name']['first'] + ' ' + dados['name']['last']
        sexo = dados['gender']
        rua = dados['location']['street']['name']
        pais = dados['location']['country']
        email = dados['email']
        username = dados['login']['username']

        print(f"Nome: {nome}\nEmail: {email}\nPaís: {pais}\nSexo: {sexo}\nRua: {rua}\nUsername: {username}")
    else:
        print("Erro ao acessar a API.")

except:
    print("Ocorreu um erro na requisição.")

