from __future__ import division
import math
import numpy as np

epsilon = pow(10,-12)

f = lambda x,a: np.exp(x) - x - a

def bissectionalRootSearch(a, b, param):

	if np.sign(f(a, param)) == np.sign(f(b, param)):
		raise Exception("a and b do not bound a root")

	m = (a + b) / 2

	if abs(f(m, param)) <= epsilon:
		return m
	elif np.abs(a - b) < epsilon:
		return a
	elif np.sign(f(m, param)) != np.sign(f(b, param)) :
		return bissectionalRootSearch(m, b, param)
	elif np.sign(f(m, param)) != np.sign(f(a, param)) :
		return bissectionalRootSearch(a, m, param)

def solveEq(a):
	if a == 1 :
		print("equation has one root: x = 0")

	if a > 1:
		delta = 1
		leftBound = 0
		rightBound = 1

		while np.sign(f(leftBound, param)) == np.sign(f(rightBound, param)):
			leftBound += 1
			rightBound += 1

		print("equation has two roots: x_1 = ", bissectionalRootSearch(-a, 0, a),
			" x_2 = ", bissectionalRootSearch(leftBound, rightBound, a))

	elif a < 1 :
		print("equation has no roots")

param = float(input("enter a = "))
solveEq(param)
