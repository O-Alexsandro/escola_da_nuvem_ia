"""
1- Gerador de Senhas Seguras  
Crie um programa que gera senhas aleatórias com letras, números e caracteres especiais. Siga as instruções abaixo:

* Solicite ao usuário o tamanho da senha desejada (por exemplo: 8, 12, 16 caracteres).  
* A senha gerada deve conter letras maiúsculas, minúsculas, números e símbolos (ex: !@#$%&*).  
* Exiba a senha gerada ao final do programa.  

Dica: Use os módulos `random` e `string` para gerar os caracteres aleatórios.
"""

import random
import string

tamanho = int(input("Digite o tamanho da senha desejada: "))

maiusculas = string.ascii_uppercase
minusculas = string.ascii_lowercase
numeros = string.digits
simbolos = "!@#$%&*"

senha = [
    random.choice(maiusculas),
    random.choice(minusculas),
    random.choice(numeros),
    random.choice(simbolos)
]

todos = maiusculas + minusculas + numeros + simbolos
while len(senha) < tamanho:
    senha.append(random.choice(todos))

random.shuffle(senha)

senha_final = "".join(senha)

print("Senha gerada:", senha_final)
