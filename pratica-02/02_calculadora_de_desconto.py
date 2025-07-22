"""
2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
"""

nomeProduto = "Camiseta"
precoOriginal = 50.00
porcentagemDesconto = 20

valor_desconto = precoOriginal * (porcentagemDesconto / 100)
preco_final = precoOriginal - valor_desconto

print("Produto:", nomeProduto)
print("Preço original: R$ {:.2f}".format(precoOriginal))
print("Desconto de {}%: R$ {:.2f}".format(porcentagemDesconto, valor_desconto))
print("Preço com desconto: R$ {:.2f}".format(preco_final))
