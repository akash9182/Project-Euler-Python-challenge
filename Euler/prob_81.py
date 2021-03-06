with open("p081_matrix.txt") as f:
	matrix = [[]]
	matrix = [map(int,row.split(',')) for row in f.readlines()]

print(matrix)
n, m = len(matrix), len(matrix[0])

for i in xrange(n):
    for j in xrange(m):
        matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1]) if i*j > 0 else (matrix[i-1][j] if i else (matrix[i][j-1] if j else 0))

print "Minimal path sum in", n, "by", m, "matrix =", matrix[-1][-1]