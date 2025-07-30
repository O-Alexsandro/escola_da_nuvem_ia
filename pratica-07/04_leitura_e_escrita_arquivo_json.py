"""
4- Leitura e Escrita de Arquivo JSON  
Desenvolva um programa que cria um dicionário com dados de uma pessoa e salva esses dados em um arquivo JSON. Em seguida, o programa deve ler o mesmo arquivo e exibir o conteúdo. Para isso:

* Crie um dicionário com pelo menos três campos (ex: nome, idade, cidade).  
* Solicite ao usuário o nome do arquivo JSON.  
* Salve os dados no arquivo usando o módulo `json`.  
* Após salvar, leia o mesmo arquivo e imprima os dados carregados.  
* Trate possíveis erros como ausência do arquivo ou problemas na escrita.

Dica: Use `json.dump()` para escrever e `json.load()` para ler o arquivo.
"""

import json

pessoa = {
    "nome": "Lucas",
    "idade": 30,
    "cidade": "Belo Horizonte"
}

nome_arquivo = input("Digite o nome do arquivo JSON (ex: dados.json): ")

try:
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(pessoa, arquivo, indent=4, ensure_ascii=False)
    print(f"\nDados salvos com sucesso no arquivo: {nome_arquivo}")
except Exception as e:
    print(f"\nErro ao salvar o arquivo: {e}")
    exit()

try:
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        dados_carregados = json.load(arquivo)
    print("\nDados lidos do arquivo:")
    for chave, valor in dados_carregados.items():
        print(f"{chave.capitalize()}: {valor}")
except FileNotFoundError:
    print(f"\nErro: o arquivo '{nome_arquivo}' não foi encontrado.")
except json.JSONDecodeError:
    print(f"\nErro: o conteúdo do arquivo '{nome_arquivo}' não é um JSON válido.")