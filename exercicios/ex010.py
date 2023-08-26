# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.


tempC = float(input('Digite a temperatura em Celcius: '))

tempF = (tempC * 9/5) + 32 

print(f"A temperatura é de {round(tempF, 2)} graus Fahrenheit")


