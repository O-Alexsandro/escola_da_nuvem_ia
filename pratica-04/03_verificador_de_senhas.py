"""
3- Verificador de Senhas Fortes
Crie um programa que avalia a força de uma senha informada pelo usuário. O programa deve:

* Solicitar a senha até que o usuário digite "sair".  
* Verificar se a senha possui pelo menos 8 caracteres.  
* Verificar se contém pelo menos um número.  
* Informar se a senha é fraca ou forte.  
* Encerrar o programa apenas quando a senha for forte ou se o usuário digitar "sair".  
"""

def contem_numero(senha):
    for caractere in senha:
        if caractere.isdigit():
            return True
    return False

while True:
    senha = input("Digite uma senha ou 'sair' para encerrar: ")

    if senha.lower() == "sair":
        print("Encerrando o programa.")
        break

    if len(senha) < 8:
        print("Senha fraca: deve conter pelo menos 8 caracteres.")
    elif not contem_numero(senha):
        print("Senha fraca: deve conter pelo menos um número.")
    else:
        print("Senha forte!")
        break
