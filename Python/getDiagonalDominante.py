

from numpy import matrix
import numpy
from math import fabs
from numpy import matlib as mlib
import scipy


def factorial(a):
	if(a == 0):
		return 1
	else: 
		return (a*factorial(a-1))

def sumarfila(mat,row):
	return reduce(lambda x, y: fabs(x)+fabs(y), mat[row].tolist()[0])

def esDiagonalmenteDominante(mat):
	for row in range(mat.shape[0]):
		if(2*fabs((mat.diagonal().tolist()[0])[row]) < sumarfila(mat,row)):
			return False
	return True

def copiarFila(mat_origen,row_o,mat_destino,row_d):
	(mat_destino[row_d]) = (mat_origen[row_o]).copy()
	return mat_destino

def copiarMatriz(mat_origen,mat_destino):
	for row in range(mat_origen.shape[0]):
		copiarFila(mat_origen,row,mat_destino,row)

def getDiagDom(mat,permutar_columnas):
	n = mat.shape[0]
	mat_aux = mlib.rand(n,n)
	copiarMatriz(mat,mat_aux)
	row = 0
	cant_max_permutaciones = factorial(n)
	while(not esDiagonalmenteDominante(mat) and cant_max_permutaciones > 0):
		if(permutar_columnas):
			mat = mat.T
			copiarMatriz(mat,mat_aux)
		copiarFila(mat,row,mat_aux,row+1)
		copiarFila(mat,row+1,mat_aux,row)
		if(row+2 <= n-1):
			row = row + 1
		else: row = 0
		copiarMatriz(mat_aux,mat)
		if(permutar_columnas):
			mat = mat.T
		cant_max_permutaciones = cant_max_permutaciones - 1
	return mat;

def __get_Diag_Dom(mat):
	getDiagDom(mat,False)
	if(esDiagonalmenteDominante(mat)):
		return mat
	else:
		getDiagDom(mat,True)
	if(esDiagonalmenteDominante(mat)):
		return mat
	else: return None


mA = matrix('1 2 3;1 2 3 ;1 2 3')
mB = matrix('-1 -2 -3;-3 -2 -1; 2 3 1')
m = [1,2,3]
if __name__ == '__main__':
	#aca va tu codigo
	print mB
	mB = __get_Diag_Dom(mA)
	if(mB == None):
		print "no existe"
	else: print "existe"
