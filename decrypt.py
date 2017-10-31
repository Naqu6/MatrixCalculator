from __future__ import division
import math
import copy

constMatrix = [
	[-.2, .2, .2],
	[.4, -.6, .2],
	[0, .4, -.2]
]

encryptedData = [
	[138, 81, 102],
	[101, 67, 109],
	[162, 123, 173],
	[210, 150, 165],
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
			result[i][j] = int(result[i][j])
			i += 1
		i = 0
		j += 1

	return result

def flatten(a):
	result = []

	for i in a:
		if type(i) == list:
			result += flatten(i)
		else:
			result.append(i)

	return result



decrypted = []

for data in encryptedData:
	fixedData = []

	for part in data:
		fixedData.append([part])

	decrypted.append(multiplyMatrixes(constMatrix, fixedData))

flattened = flatten(decrypted)

text = ""

for part in flattened:
	if part == 27: 
		text += " "
	else:
		text += chr(96 + part) 

print text

