import random

def obter_nivel_dificuldade():
    print("Escolha o nível de dificuldade:")
    print("1 - Fácil (10 tentativas)")
    print("2 - Médio (7 tentativas)")
    print("3 - Difícil (5 tentativas)")
    
    while True:
        nivel = int(input("Digite o número correspondente ao nível desejado: "))
        
        if nivel in [1, 2, 3]:
            return nivel
        else:
            print("Nível inválido. Escolha novamente.")

def adivinhar_numero(numero_secreto, max_tentativas):
    for tentativas in range(1, max_tentativas + 1):
        print("Tentativa {} de {}".format(tentativas, max_tentativas))
        
        try:
            palpite = int(input("Digite o seu palpite: "))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
            continue
        
        if palpite == numero_secreto:
            print("Parabéns! Você acertou o número em", tentativas, "tentativas!")
            return True
        
        print("Tente um número", "maior!" if palpite < numero_secreto else "menor!")
    
    print("Você excedeu o número máximo de tentativas. O número secreto era", numero_secreto)
    return False

def jogar_adivinhacao():
    numero_secreto = random.randint(1, 100)
    nivel = obter_nivel_dificuldade()
    
    if nivel == 1:
        max_tentativas = 10
    elif nivel == 2:
        max_tentativas = 7
    elif nivel == 3:
        max_tentativas = 5
    
    print("Adivinhe o número entre 1 e 100!")
    
    if not adivinhar_numero(numero_secreto, max_tentativas):
        print("FIM DE JOGO")

jogar_adivinhacao()
