"""
3- Consulta de CEP  
Desenvolva um programa que consulta dados de endereço a partir de um CEP brasileiro. Siga os passos abaixo:

* Solicite ao usuário que digite um CEP (apenas números, sem traço).  
* Acesse a API pública do ViaCEP: "https://viacep.com.br/ws/{cep}/json/".  
* Exiba as seguintes informações: logradouro, bairro, cidade, estado e o próprio CEP.  
* Caso o CEP não exista ou haja erro, informe isso de forma clara ao usuário.  

Dica: Use o módulo `requests` e trate exceções com `try/except`.
"""

import requests

cep = input("Digite o CEP (apenas números): ")

if len(cep) != 8:
    print("CEP inválido! Deve conter exatamente 8 números.")
else:
    try:
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url)
        data = response.json()

        if "erro" in data:
            print("CEP não encontrado.")
        else:
            print(f"CEP: {data['cep']}, Logradouro: {data['logradouro']}, Bairro: {data['bairro']}, Cidade: {data['localidade']}, Estado: {data['uf']}")

    except requests.exceptions.RequestException as e:
        print("Erro ao consultar o CEP. Verifique sua conexão e tente novamente.")
