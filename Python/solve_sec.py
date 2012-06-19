from gauss_seidel import *
from os import system
from sys import platform

class ConditionMat(object):
	
	def __init__(self, cond, errMsg):
		super(ConditionMat, self).__init__()
		self.cond = cond
		self.errMsg = errMsg

	def check(self, Mat,dimension):
		return self.cond(Mat,dimension)
	def raiseError(self):
		raise Exception(self.errMsg)

def clearScreen():
	if platform is 'win32':
		system('cls')
	else:
		system("clear")

def getInputNumber(input_msg,errMsg):
	number = None

	while not number:
		try:
			number = int(raw_input(input_msg))
		except ValueError:
			print errMsg

	return number

def getInputMatrix(input_msg, dimension, conditions):
	while True:
		try:
			mat_str = raw_input(input_msg)
			Mat = matrix(mat_str)
			for cond in conditions:
				if cond.check(Mat, dimension):
					cond.raiseError()
			break
		except Exception, e:
			print e.message
	return Mat


if __name__ == '__main__':

	clearScreen()

	print"""
	  ______ _______ _                ______                   _                   
	 / _____|_______|_)              (_____ \                 | |                  
	( (____  _____   _                _____) )_____  ___  ___ | |_   _ _____  ____ 
	 \____ \|  ___) | |              |  __  /| ___ |/___)/ _ \| | | | | ___ |/ ___)
	 _____) ) |_____| |_____         | |  \ \| ____|___ | |_| | |\ V /| ____| |    
	(______/|_______)_______)        |_|   |_|_____|___/ \___/ \_)\_/ |_____)_|    
	                                                                                                                                                                          
	"""

	print "\t\t\tSEL Resolver 1.0 "
	print
	print "Programa de resolucion de ecuaciones lineales de sistemas cuadrados usando el metodo de Gauss Seidel matricial"
	print
	print "\t\tImplementado en Python 2.7 usando NumPy y SciPy"
	print 

	input_msgA = "#  Ingrese la matriz de coeficientes A \n Matriz A = "
	input_msgB = "#  Ingrese la matriz columna de terminos independients B \n Matriz B = "
	input_msgX0 = "# Ingrese la matriz columna de valores iniciales X0 \n Matriz X0 = "

	input_msgDim = "Ingrese la dimension del sistema: "
	errMsgDim = "La dimension ingresada no es un numero"

	input_msgEps = "#  Ingrese la precision X,(se computa como 10^-X, es el corte de control) del sistema: "
	errMsgEps = "La precision ingresada no es un numero"

	input_msgTrunc = "#  Ingrese cantidad maxima de digitos antes de truncar: "
	errMsgTrunc = "La cantidad ingresada no es un numero"

	condSquared = ConditionMat((lambda mat,d: mat.shape[0] is not mat.shape[1]),"La matriz ingresada no es cuadrada" )
	condDimRange = ConditionMat((lambda mat,dimension: mat.shape[0] is not dimension), "La matriz ingresada no es de la misma dimension que la dimension del sistema"  )
	condColumn = ConditionMat((lambda mat,dimension: mat.shape[1] is not 1), "La matriz ingresada no es una matriz columna")

	conditionsSquared = [condSquared,condDimRange]
	conditionsColumn = [condColumn,condDimRange]

	while True:

		print "Nota: El ingreso de valores de las matrices se realiza separando los elementos con un espacio y las filas con ;"
		print

		dimension = getInputNumber(input_msgDim,errMsgDim)

		A = getInputMatrix(input_msgA,dimension,conditionsSquared)
		B = getInputMatrix(input_msgB,dimension,conditionsColumn)
		X0 = getInputMatrix(input_msgX0,dimension,conditionsColumn)
	
		epsilon = 10**-getInputNumber(input_msgEps,errMsgEps)
		trunc_precision = getInputNumber(input_msgTrunc,errMsgTrunc)


		clearScreen()

		print "Empezando a resolver ! :D \n"

		try:
			Gauss_Seidel(A,B,trunc_precision).solve_precision(X0,epsilon)

		except NotDiagDomException, e:
			print e.message

		finally:
			answer  = raw_input("Desea ingresar otro sistema? (y/n) ")

		if answer.lower() == 'n':
			print
			print "Vuelva pronto :D" 
			print
			exit()

		clearScreen()

		

	







