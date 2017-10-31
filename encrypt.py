from __future__ import division
import math
import copy

constMatrix = [
	[1,3,4],
	[2,1,3],
	[4,2,1]
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

dataSets = []
buf = []

for letter in "all is fair in love and war":
	val = ord(letter) - 96
	if letter == " ": val = 27

	buf.append(val)

	if len(buf) % 3 == 0:
		dataSets.append([[buf[0]], [buf[1]], [buf[2]]])
		buf = []

for dataSet in dataSets:
	print multiplyMatrixes(constMatrix, dataSet)