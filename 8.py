#8.	Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
hora = float(input("Quanto você ganha por hora trabalhar? "))
tempo = float(input('Quantas horas você trabalha por dia'))
salario = hora*(tempo*22) 
print(f'Seu salario, portanto, é {salario} reais')
