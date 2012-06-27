from numpy import matrix, triu, tril, vectorize, diag
from math  import fabs, factorial, trunc


class NotDiagDomException(Exception):
	"""NotDiagDomException es una excepcion que ocurre cuando la matriz no se pudo diagonalizar dominantemente"""
	def __init__(self):
		Exception.__init__(self, "No se pudo conseguir una matriz diagonalmente dominante a partir de la matriz \nde coeficientes dada ")

class Gauss_Seidel(object):
	"""Objeto que resuelve un sistema A,B,X dado con precision E for Gauss_Seidel"""
	def __init__(self, A,B, trunc_precision):
		"""A y B tienen que ser matrices!, A debe ser cuadrada, B una matriz columna. trunc_precision es la cantidad de digitos deseados"""
		super(Gauss_Seidel, self).__init__()

		if  not self.__is_Squared(A):
			raise Exception("La matriz A no es cuadrada")

		if A.shape[0] != B.shape[0] or B.shape[1] != 1:
			raise Exception("La matriz B no es columna de la dimension de A")

		if  not self.__check_Diag_Dom(A):
			A = self.__transform_into_DiagDom(A)

		D_L = tril(A)
		U = -triu(A,k=1)
		self.Tgs = D_L.I * U
		self.Cgs = D_L.I * B
		self.trunc_precision = trunc_precision

	def __is_Squared(self,A):
		return A.shape[0] == A.shape[1]


	def __solve(self, X):
		return (self.Tgs * self.__trunc(X) + self.Cgs)

	def __transform_into_DiagDom(self,mat):
		"""Transforma mat en una matriz diagonalmente dominante, si no lo logra, lanza NotDiagDomException"""
		max_indexes = []

		for row in mat.tolist():
			index = self.__get_Max_Index_In_Row(row)
			if index not in max_indexes:
				max_indexes.append(index)
			else:
				raise NotDiagDomException

		diag_mat = mat.copy()
		for pos,index in enumerate(max_indexes):
			diag_mat[index] = mat[pos].tolist()

		return diag_mat



	def __get_Max_Index_In_Row(self,row):
		abs_row = map(fabs,row)

		try:
			max_element_index = [(2*x >= sum(y for y in abs_row)) for x in abs_row].index(True)
		except ValueError:
			raise NotDiagDomException

		return max_element_index

	def __trunc(self, X):
		""" Trunca todos los elementos de la matriz a la precision deseada"""
		def trunc_to_precision(number, precision):
			return (1.0/10**precision)*trunc((number * 10**precision))

		trunc_matrix = vectorize(trunc_to_precision) #esta funcion es como un map pero para matrices.
		return trunc_matrix(X,self.trunc_precision)


	def __check_Diag_Dom(self,A):
         """ Chequea si A es diagonalmente dominante """
         rows = A.tolist()
         for x, Dx in enumerate(diag(A)):
             if not 2*fabs(Dx) >= sum(fabs(y) for y in rows[x]):
                return False 
         return True

	
	def solve_precision(self,X0,epsilon):
		""" Resuelve para un X0 dado el sistema con el epsilon dado """
		iterations = 1

		while True:
			X1 = self.__solve(X0)

			print "Iteracion numero:", iterations, "valores:", [str(x[0]) for x in X1.tolist()]

			if self.__norm2(X1-X0) < epsilon:
				return (X1, iterations)

			X0 = X1
			iterations +=1



	def __norm2(self, X):
         """ Calcula la norma 2 del vector dado """
         squared_norm = sum([x**2 for row in X.tolist() for x in row] )
         return squared_norm**0.5



