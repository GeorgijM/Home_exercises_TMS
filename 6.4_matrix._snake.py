import time

n = int(input("Set matrix size: "))
start_i = 0  # first index in matrix element
start_j = 0 # second index in matrix element


count = 1

flag = 'process'
shift_up_left = 1
shift_down_right = 2

# init the matrix with empty rows
matrix = [[] for matr_str in range(0, n)]

for matr_str in range(0, n):
    for matr_col in range(0, n):
        # set with the random numbers
        # matrix[matr_str].append(randint(0, 10))

        # set with zeros
        matrix[matr_str].append(0)

    # print by rows (beautiful)
    print(matrix[matr_str])
print('====================')

while start_i == 0:

    start_i = int(input("Set the start i-index for matrix element: "))
    if start_i == 0:
        print(f'Please insert start_i > 0')

start_j = int(input("Set the start j-index for matrix element: "))

i = start_i
j = start_j

matrix[i][j] = 'x'


def print_matrix():
    time.sleep(0.3)
    for num in range(1, 30):
        print("\n")
    for matr_str in range(0, n):
        print(matrix[matr_str])


def up_step():
    global count
    global i
    global j
    global flag

    if i > 0:
        if matrix[i - 1][j] != 0:
            flag = 'stop'
        else:
            matrix[i - 1][j] = count
            count += 1
            i -= 1


def left_step():
    global count
    global i
    global j
    global flag

    if j > 0:
        if matrix[i][j - 1] != 0:
            flag = 'stop'
        else:
            matrix[i][j - 1] = count
            count += 1
            j -= 1


def down_step():
    global count
    global i
    global j
    global flag

    if i < n - 1:
        if matrix[i + 1][j] != 0:
            flag = 'stop'
        else:
            matrix[i + 1][j] = count
            count += 1
            i += 1


def right_step():
    global count
    global i
    global j
    global flag

    if (j < n - 1):
        if matrix[i][j + 1] != 0:
            flag = 'stop'
        else:
            matrix[i][j + 1] = count
            count += 1
            j += 1




while True:
    if flag == 'stop':
        break
    for steps in range(n ** 2):
        for step in range(shift_up_left):
            if flag == 'stop':
                break
            up_step()
            print_matrix()
        for step in range(shift_up_left):
            if flag == 'stop':
                break
            left_step()
            print_matrix()
        for step2 in range(shift_down_right):
            if flag == 'stop':
                break
            down_step()
            print_matrix()
        for step2 in range(shift_down_right):
            if flag == 'stop':
                break
            right_step()
            print_matrix()
        # the way to go round the matrix "start item" is making 1 step two times,
        # than 2 steps two times, than 3 steps two times and so on..
        shift_up_left += 2
        shift_down_right += 2
