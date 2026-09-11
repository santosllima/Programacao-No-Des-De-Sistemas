import random

numero_secreto = random.randint(1, 10)
tentativas_restantes = 5
bonus_concedido = False  # Garante que o jogador receba o bônus apenas uma vez por "quase acerto"

print("=== JOGO DA ADIVINHAÇÃO ===")
print("Adivinhe o número secreto entre 1 e 10!")

while tentativas_restantes > 0:
    print(f"\nTentativas restantes: {tentativas_restantes}")
    
    try:
        chute = int(input("Digite o seu palpite: "))
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
        continue

    # Verifica se o jogador acertou
    if chute == numero_secreto:
        print(f"Parabéns! Você acertou o número secreto ({numero_secreto})!")
        break
    
    # Se errou, gasta uma tentativa
    tentativas_restantes -= 1
    diferenca = abs(chute - numero_secreto)

    # Regra do bônus: diferença de apenas 1 unidade
    if diferenca == 1 and not bonus_concedido:
        tentativas_restantes += 1
        bonus_concedido = True
        print("🔥 BÔNUS! Você ficou MUITO perto (diferença de 1)! Ganhou +1 tentativa extra.")
    elif chute < numero_secreto:
        print("O número secreto é MAIOR.")
    else:
        print("O número secreto é MENOR.")

if tentativas_restantes == 0:
    print(f"\nFim de jogo! Suas tentativas acabaram. O número secreto era {numero_secreto}.")
