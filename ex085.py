numeros = [[],[]]

print('PROGRAMA PARA VERIFICAR NÚMEROS PARES E ÍMPARES')
print('-=' * 20)

for numbers in range(1, 8):
    num = int(input(f'Digite o {numbers}ª valor: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
print(f'Os valores pares são {sorted(numeros[0])}')
print(f'Os valores impares são {sorted(numeros[1])}')


    
