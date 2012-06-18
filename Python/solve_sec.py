from gauss_seidel import *

if __name__ == '__main__':
	A = matrix('6 1 1 ; 1 6 2; 1 1 -6')
	B = matrix('15 ; -3 ; 9')
	X0 = matrix('1 ; 1 ; 1')
	epsilon = 10**-100
	trunc_precision = 102

	gs = Gauss_Seidel(A,B,trunc_precision)
	gs.solve_precision(X0,epsilon)