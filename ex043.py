nome = str(input('Digite seu nome: '))
peso = float(input('Peso: '))
altura = float(input('Altura: '))

imc = peso / (altura**2)
print(f'Sua IMC é de {imc:.2f}')

if imc <= 18.5:
    print(f'{nome}, você está ABAIXO DO PESO.')
elif imc >=18.5 and imc <= 25:
    print(f'{nome}, você está com o PESO IDEAL.')
elif imc >= 25 and imc <= 30:
    print(f'{nome}, você está com SOBREPESO.')
elif imc >= 30 and imc <= 40:
    print(f'{nome}, você está com OBESIDADE.')
elif imc >= 40:
    print(f'{nome}, você está com OBESIDADE MÓRBIDA.')

