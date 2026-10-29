# Define função para calcular preço final
def calcular_preco_final(nome, preco, desconto=0):
    preco_final = preco - (preco * desconto / 100)
    print(f"Preço inicial de {nome}: R$ {preco:.2f}")
    print(f"Preço final de {nome}: R$ {preco_final:.2f}")

# Exemplo de uso (com desconto alterado de 15% para 20%)
calcular_preco_final("Fone de ouvido", 200, 20)
