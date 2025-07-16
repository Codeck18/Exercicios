"""15.	Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
•	salário bruto.
•	quanto pagou ao INSS.
•	quanto pagou ao sindicato.
•	o salário líquido.
•	calcule os descontos e o salário líquido, conforme a tabela abaixo:
Salário Bruto : R$ IR (11%) : R$ INSS (8%) : R$ Sindicato ( 5%) : R$ Salário Liquido : R$ Obs.: Salário Bruto - Descontos = Salário Líquido."""
hora = float(input("Quanto você ganha por hora trabalhar? "))
tempo = float(input('Quantas horas você trabalha por dia? '))
salario = hora*(tempo*22) 
inss= salario*0.08
sindicato= salario*0.05
ir= salario*0.11
salarioreal=salario-inss-sindicato-ir 
print(f'Seu salario liquido, portanto, é {salarioreal} reais')