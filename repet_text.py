# Solicita o texto e o número ao usuário
texto = input("Digite um texto: ")
numero = int(input("Digite um número: "))

# Repete o texto a quantidade de vezes indicada pelo número, com espaços entre as repetições
resultado = ' '.join([texto] * numero)

# Exibe o resultado
print(resultado)
