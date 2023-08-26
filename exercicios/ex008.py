# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.


valorHora = float(input('Diga quanto ganha por hora trabalhada: '))

horasTrabalhadas = int(input("Quantas horas trabalha: "))

salario = valorHora * horasTrabalhadas

print(f"Seu salario é de {round(salario, 2)} reais ao mês" )


