"""
1- Calculadora de Gorjeta
Crie um programa que calcula o valor da gorjeta a partir do total da conta e da porcentagem escolhida. Use as instruções abaixo:

* Defina o valor da conta (ex: R$ 100,00).  
* Informe a porcentagem da gorjeta (ex: 10%, 15%, 20%).  
* O programa deve calcular o valor correspondente e exibir o resultado com duas casas decimais.
"""

valor_conta = float(input("Digite o valor da conta (em R$): "))
porcentagem = float(input("Digite a porcentagem da gorjeta (ex: 10, 15, 20): "))

valor_gorjeta = valor_conta * (porcentagem / 100)

print(f"Gorjeta de {porcentagem}%: R$ {valor_gorjeta:.2f}")