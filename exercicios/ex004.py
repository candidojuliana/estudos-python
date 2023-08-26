# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

m1 = float(input('Digite a méidia do 1º bimestre: '))
# O método integrado float() recebe um objeto string e a transforma em inteiro

m2 = float(input('Digite a méidia do 2º bimestre: '))

m3 = float(input('Digite a méidia do 3º bimestre: '))

m4 = float(input('Digite a méidia do 4º bimestre: '))


print(f"A média final é {(m1 + m2 + m3 + m4) / 4}")