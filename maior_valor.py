print("vamos descobrir quem tem o maior valor")
num1 = input('digite um número: ')
num2 = input('digite outro número: ')

if num1 > num2:
    print(f'{num1} é maior')
    
elif num2 > num1:
    print(f'{num2} é maior')
    
elif num1 == num2:
    print('os valores são iguais')
    
else:
    print('não entendi sua resposta.')
