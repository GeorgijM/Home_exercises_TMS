from random import randint
n = int(input("Set matrix size: "))
root_diagonal = 0
sub_diagonal = 0

# init the matrix with empty rows
matrix = [[] for matr_str in range(0, n)]
#print(matrix)

for matr_str in range(0, n):
    for matr_col in range(0, n):
        # set with the random numbers
        matrix[matr_str].append(randint(0, 10))

        # set with zeros
        #matrix[matr_str].append(1)

    # print by rows (beautiful)
    print(matrix[matr_str])

# change the definite elem
#matrix[0][1] = 6

#diagonal [0][0]-[n][n]
for i in range(1, n):
    for j in range(i):
        if matrix[i][j] != matrix[j][i]:
            print(f'matrix[{i}][{j}] = {matrix[i][j]} matrix[{j}][{i}] ={matrix[j][i]}  NONsymetrical')
            root_diagonal = 1
        else:
            print(f'matrix[{i}][{j}] = {matrix[i][j]} matrix[{j}][{i}] ={matrix[j][i]}  symetrical')

print('====================')
#diagonal [n][0]-[0][n]
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i] and (i + j) > n-1:
            print(f'matrix[{i}][{j}] = {matrix[i][j]} matrix[{j}][{i}] ={matrix[j][i]}  NONsymetrical')
            sub_diagonal = 1
        else:
            if (i + j) > n-1:
                print(f'matrix[{i}][{j}] = {matrix[i][j]} matrix[{j}][{i}] ={matrix[j][i]}  symetrical')

if root_diagonal == 1:
    print('Matrix NONsymetric by root diagonal ')
else:
    print('Matrix Symetric by root diagonal ')

if sub_diagonal == 1:
    print('Matrix NONsymetric by sub diagonal ')
else:
    print('Matrix Symetric by sub diagonal ')