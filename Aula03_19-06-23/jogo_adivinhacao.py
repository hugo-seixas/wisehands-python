import random

def adivinhar_numero():
    numero_secreto = random.randint(1, 50)
    tentativas = 1
    max_tentativas = 5
    
    print("Adivinhe o número entre 1 e 50!")
    
    while tentativas <= max_tentativas:
        print("Tentativa {} de {}".format(tentativas, max_tentativas))
       
        try:
           palpite = int(input("Digite o seu palpite: "))
        except ValueError:
           print("Entrada inválida. Digite um número inteiro.")
           continue
       
        if palpite == numero_secreto:
            print("Parabéns! Você acertou o número em", tentativas, "tentativas!")
            break
        
        print("Tente um número", "maior!" if palpite < numero_secreto else "menor!")
        
        tentativas += 1
    
    print("FIM DE JOGO")
    
adivinhar_numero()