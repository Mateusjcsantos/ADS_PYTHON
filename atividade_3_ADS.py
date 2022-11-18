#CALCULO IMC

nome = input('Qual seu nome? ')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = round(peso / altura**2, 1)
if imc < 18.5:
    print(nome, 'eu IMC é:',imc, ', você está abaixo do peso')
if imc > 18.5 and imc < 24.9:
    print(nome, 'seu IMC é:', imc, ', você está com seu peso ideal')
if imc > 25 and imc < 29.9:
    print(nome, 'seu IMC é:', imc, ', você está com sobrepeso')
if imc > 30 and imc < 34.9:
    print(nome, 'seu IMC é:', imc, ', você está com obesidade grau I')
if imc > 35 and imc < 39.9:
    print(nome, 'seu IMC é:', imc, ', você está com obesidade grau II')
if imc > 40:
    print(nome, 'seu IMC é:', imc, ', você está com obesidade grau III')


