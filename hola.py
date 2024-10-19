try:
	name = input('Ingrese nombre: ')
	print(f'Hola {name}!')
	print('\nEdad: ', int(input('Ingrese edad: ')))
except:
	print('Dato incorrecto!')