#12.	Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
altura = float(input('Qual sua altura atualmente? '))
imc = (72.2*altura)-58
print(f'Segundo sua altura, seu peso ideal segundo o IMC é {imc}')