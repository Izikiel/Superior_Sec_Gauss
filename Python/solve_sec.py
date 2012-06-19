from gauss_seidel import *
from os import system
from sys import platform

def clearScreen():
	if platform is 'win32':
		system('cls')
	else:
		system("clear")

if __name__ == '__main__':

	clearScreen()

	print "SEL Resolver 1.0 "
	print "Programa de resolucion de ecuaciones lineales de sistemas cuadrados usando el metodo de Gauss Seidel matricial"
	print "Implementado en Python 2.7 usando NumPy y SciPy"
	print 

	while True:

		print "Nota: El ingreso de valores de las matrices se realiza separando los elementos con un espacio y las filas con ;"
		print

		dimension = None

		while not dimension:
			try:
				dimension = int(raw_input("Ingrese la dimension del sistema: "))
			except ValueError:
				print "La dimension ingresada no es un numero"



		while True:
			try:
				a = raw_input("#  Ingrese la matriz de coeficientes A \n Matriz A = ")

				if len(a.split(';')) is dimension: 

					A = matrix(a)

					if A.shape[0] is not A.shape[1]:
						raise Exception("La matriz ingresada no es cuadrada")
					if A.shape[0] is not dimension:
						raise Exception("La matriz ingresada no es de la misma dimension que la dimension del sistema")
					else:
						break

			except Exception, e:
				print e.message
			
		while True:
			try:
				b = raw_input("#  Ingrese la matriz columna de terminos independients B \n Matriz B = ")

				if len(b.split(';')) is dimension:  

					B = matrix(b)

					if B.shape[0] is not dimension:
						raise Exception("La matriz ingresada no es de la misma dimension que la dimension del sistema ")
					if B.shape[1] is not 1:
						raise Exception("La matriz ingresada no es una matriz columna")
					else:
						break
						
			except Exception, e:
				print e.message

		while True:
			try:
				x0 = raw_input("# Ingrese la matriz columna de valores iniciales X0 \n Matriz X0 = ")

				if len(x0.split(';')) is dimension:  
					
					X0 = matrix(x0)

					if X0.shape[0] is not dimension:
						raise Exception("La matriz ingresada no es de la misma dimension que la dimension del sistema ")
					if X0.shape[1] is not 1:
						raise Exception("La matriz ingresada no es una matriz columna")
					else:
						break
						
			except Exception, e:
				print e.message


		epsilon = None
		while not epsilon:
			try:
				epsilon = int(raw_input("#  Ingrese la precision X,(se computa como 10^-X, es el corte de control) del sistema: "))
				epsilon = 10**-epsilon
			except ValueError:
				print "La precision ingresada no es un numero"

		trunc_precision = None
		while not trunc_precision:
			try:
				trunc_precision = int(raw_input("#  Ingrese cantidad maxima de digitos antes de truncar: "))
			except ValueError:
				print "La cantidad ingresada no es un numero"

		clearScreen()

		print "Empezando a resolver ! :D \n"

		Gauss_Seidel(A,B,trunc_precision).solve_precision(X0,epsilon)


		answer  = raw_input("Desea ingresar otro sistema? (y/n) ")
		

		if answer.lower() == 'n':
			print "Vuelva pronto :D" 
			exit()

		clearScreen()

		

	







