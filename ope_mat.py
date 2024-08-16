num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

operacao = input("Digite a operação que deseja realizar (+, -, *, /): ")

if operacao == '+':
    print(num1 + num2)
elif operacao == '-':
    print(num1 - num2)
elif operacao == '*':
    print(num1 * num2)
elif operacao == '/':
    print(num1 / num2)