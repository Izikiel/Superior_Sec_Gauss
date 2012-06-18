from numpy import matlib
from numpy import matrix, triu, tril, diag


class Gauss_Seidel(object):
	"""Objeto que resuelve un sistema A,B,X dado con precision E for Gauss_Seidel"""
	def __init__(self, A,B):
		super(Gauss_Seidel, self).__init__()
		D_L = tril(A)
		U = triu(A,k=1)
		self.Tgs = D_L.I * (-U)
		self.Cgs = D_L.I * B

	def solve(self, X):
		return (self.Tgs * X + self.Cgs)
	
	def solve_precision(self,X,precision):
		pass