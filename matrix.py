from __future__ import division
import math

constMatrix = [
]

varMatrix = [
]

def multiplyMatrixes(a,b):
	if len(a) == 0 or len(b) == 0:
		return []

	result = [[0 for _ in xrange(len(b[0]))] for _ in xrange(len(a))]
	i = 0
	j = 0

	while j < len(b[0]):
		while i < len(a):
			for subIndex in xrange(len(a[i])):
				result[i][j] += a[i][subIndex] * b[subIndex][j]
			i += 1
		i = 0
		j += 1

	return result

# number of times to repeat
n = 5

for _ in xrange(n):
	varMatrix = multiplyMatrixes(constMatrix, varMatrix)

print varMatrix