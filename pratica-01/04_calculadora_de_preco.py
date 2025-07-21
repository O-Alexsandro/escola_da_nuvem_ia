"""
*O programa deve calcular o volume e exibir o resultado em cm³.

4- Calculadora de Preço Total
* Desenvolva um programa que calcula o preço total de uma compra. 
* Use as seguintes informações:

* Nome do produto: "Cadeira Infantil"
* Preço unitário: R$ 12.40
* Quantidade: 3

* O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.
"""

nomeProduto = "Cadeira Infantil"
preco = 12.40
quantidade = 3

precoTotal = preco * quantidade

print(f"Produto: {nomeProduto}")
print(f"Preço unitário: R$ {preco:.2f}")
print(f"Quantidade: {quantidade}")
print(f"Preço total: R$ {precoTotal:.2f}")