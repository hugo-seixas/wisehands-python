def divisao(num1, num2):
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Não é possível dividir por zero"
    
    return resultado

def velocidade(espaco, tempo):
    v = divisao(espaco, tempo)
    return v

espaco = float(input("Digite o espaço percorrido: "))
tempo = float(input("Digite o tempo decorrido: "))

resultado_velocidade = velocidade(espaco, tempo)
print("VELOCIDADE:", resultado_velocidade)