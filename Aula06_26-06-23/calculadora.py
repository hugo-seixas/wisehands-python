def calculadora(num1, num2):
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    if num2 != 0:
        divisao = num1 / num2
    else:
        divisao = "Não é possível dividir por zero"
    
    print("SOMA:", soma)
    print("SUBTRAÇÃO:", subtracao)
    print("MULTIPLICAÇÃO:", multiplicacao)
    print("DIVISÃO:", divisao)

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

calculadora(num1, num2)
