
from numpy import matrix, triu, tril, vectorize, diag
from math  import fabs

class Gauss_Seidel(object):
	"""Objeto que resuelve un sistema A,B,X dado con precision E for Gauss_Seidel"""
	def __init__(self, A,B, trunc_precision):
		"""A y B tienen que ser matrices!, A debe ser cuadrada, B una matriz columna. trunc_precision es la cantidad de digitos deseados"""
		super(Gauss_Seidel, self).__init__()

		if self.__is_Squared(A) is False:
			raise Exception("La matriz A no es cuadrada")

		if A.shape[0] is not B.shape[0] or B.shape[1] is not 1:
			raise Exception("La matriz B no es columna de la dimension de A")

		if self.__check_Diag_Dom(A) is False:
			A = self.__get_Diag_Dom(A)
			if A is None:
				raise Exception("No se pudo conseguir una matriz diagonalmente dominante a partir de A")

		D_L = tril(A)
		U = -triu(A,k=1)
		self.Tgs = D_L.I * U
		self.Cgs = D_L.I * B
		self.trunc_precision = trunc_precision

	def __is_Squared(self,A):
		return A.shape[0] is A.shape[1]


	def __solve(self, X):
		return (self.Tgs * self.__trunc(X) + self.Cgs)

	def __get_Diag_Dom(self,A):
		""" Transforma A en una matriz diagonalmente dominante """
		return True # TODO Hacer metodo para permutar! 

	def __trunc(self, X):
		""" Trunca todos los elementos de la matriz a la precision deseada"""
		def trunc(number, precision):
			int_number = int(number)
			decimals = int((number - int_number) * 10**precision)
			return int_number + (float(decimals)/(10**precision))

		trunc_matrix = vectorize(trunc) #esta funcion es como un map pero para matrices.
		return trunc_matrix(X,self.trunc_precision)


	def __check_Diag_Dom(self,A):
		""" Chequea si A es diagonalmente dominante """
		rows = A.tolist()
		D = diag(A)
		true_rows = []
		for x in xrange(0,len(D)):
			res  = fabs(D[x]) >= reduce(lambda x,y: fabs(x)+fabs(y),rows[x]) - fabs(D[x]) 
			true_rows.append(res)
		return all(true_rows)

	
	def solve_precision(self,X0,epsilon):
		""" Resuelve para un X0 dado el sistema con el epsilon dado """
		iterations = 1

		while True:
			X1 = self.__solve(X0)

			print "Iteracion numero:", iterations, "valores:", [str(x[0]) for x in X1.tolist()]

			if self.__norm2(X1-X0) < epsilon:
				print "Se necesitaron", iterations, "iteraciones para llegar a la precision deseada"
				print "Valores obtenidos:", [str(x[0]) for x in X1.tolist()]
				return X1

			X0 = X1
			iterations +=1



	def __norm2(self, X):
		""" Calcula la norma 2 del vector dado """
		vectorX = [x for row in X.tolist() for x in row]
		squared_norm = sum(map(lambda x: x**2, vectorX))
		return squared_norm**0.5


