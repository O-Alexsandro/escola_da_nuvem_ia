"""
2- Verificador de Palíndromos
Crie um programa que verifica se uma palavra ou frase é um palíndromo, ou seja, se pode ser lida da mesma forma de trás para frente, desconsiderando espaços, acentos e pontuação. Para isso:

*Solicite ao usuário uma palavra ou frase.
*Desconsidere letras maiúsculas, espaços e sinais de pontuação.
*Verifique se a frase é um palíndromo.
*Exiba "Sim" se for palíndromo ou "Não" se não for.
"""

import unicodedata

frase = input("Digite uma palavra ou frase: ")

frase_sem_acentos = ''.join(
    c for c in unicodedata.normalize('NFD', frase)
    if unicodedata.category(c) != 'Mn'
)

frase_limpa = ''.join(
    c.lower() for c in frase_sem_acentos
    if c.isalnum()
)

if frase_limpa == frase_limpa[::-1]:
    print("Sim")
else:
    print("Não")
