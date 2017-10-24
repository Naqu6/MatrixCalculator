from __future__ import division
import math

constArray = [
	[0., 0., .33],
	[.4, 0., 0.],
	[0., .71, .94]
]

x = [
	[900],
	[500],
	[2600]
]

def multiplyMatrixes(a,b):
	result = [[0 for _ in xrange(len(b[0]))] for _ in xrange(len(a))]
	i = 0
	j = 0

	while j < len(b[0]):
		while i < len(a):
			for subIndex in xrange(len(a[i])):
				result[i][j] += a[i][subIndex] * b[subIndex][j]
				print a[i][subIndex], b[subIndex][j]
			i += 1
		i = 0
		j += 1

	return result

# number of times to repeat
n = 5

for _ in xrange(n):
	x = multiplyMatrixes(constArray, x)

print x