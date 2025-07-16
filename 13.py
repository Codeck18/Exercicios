"""13.	Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
•	Para homens: (72.7*h) - 58
•	Para mulheres: (62.1*h) - 44.7"""
sexo = input('Você é homem ou mulher?')
if sexo == 'mulher':
    altura= float(input('Qual sua altura?'))
    imcm= (62.1*altura) - 44.7
    print(f'Com base nos dados obtidos, seu peso ideal seria {imcm}')
elif sexo == 'homem':
    altura= float(input('Qual sua altura?'))
    imch= (72.2*altura) - 58
    print(f'Com base nos dados obtidos, seu peso ideal seria {imch}')
else:
    print('opção invávlida')
