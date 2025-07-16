"""11.	Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
•	o produto do dobro do primeiro com metade do segundo .
•	a soma do triplo do primeiro com o terceiro.
•	o terceiro elevado ao cubo."""
n1 = int(input('Forneça um numero inteiro'))
n2 = int(input('Forneça outro numero inteiro'))
n3 = float(input('Agora, forneça um numero decimal'))
p = (n1*2)*(n2/2)
s= n3+(n1*3)
c=n3**3
print(p, s, c)