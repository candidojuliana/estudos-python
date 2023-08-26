#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math

raio = int(input('Digite o raio do círculo: '))


print(f"A area do círculo é: {round(math.pi, 2) * raio ** 2}" )

# round(pi, casas) para definir a quantidade de cadas depois da vírgula a serem usadas ou mostradas 
# Area de um círculo = π . r²

