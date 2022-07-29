from random import randint
from time import sleep
from os import system
import subprocess

import os
#n = int(input("Set matrix size: "))
n = 5
root_diagonal = 0
sub_diagonal = 0



# init the matrix with empty rows
matrix = [[] for matr_str in range(0, n)]
#print(matrix)

for matr_str in range(0, n):
    for matr_col in range(0, n):
        # set with the random numbers
        #matrix[matr_str].append(randint(0, 10))

        # set with zeros
        matrix[matr_str].append(0)

    # print by rows (beautiful)
    #matrix[0][1] = 1
    print(matrix[matr_str])
print('====================')
#subprocess.call("clear") # linux/mac

# for num in range(1,10):
#     print("\n")


#matrix2 = [e for ]
# change the definite elem
#print(matrix[0][1])
start_i = 2   #first index in matrix element
start_j = 2   #second index in matrix element
i = start_i     #a[i][j]
j = start_j     #a[i][j]
steps_in_circle_part = 1 #the way to go round the matrix start item is doing 1 step two times,
                        # than 2 steps two times, than 3 steps two times and so on..



matrix[i][j] = 'x'
count = 10

def up_step():
    global count
    global i
    global j
    global flag

    if i > 0:
        if matrix[i - 1][j] != 0:
            flag = 'stop'
        matrix[i-1][j] = count
        count +=1
        i -= 1


def left_step():
    global count
    global i
    global j
    global flag

    if j > 0:
        if matrix[i][j - 1] != 0:
            flag = 'stop'
        matrix[i][j-1] = count
        count += 1
        j -= 1



def down_step():
    global count
    global i
    global j
    global flag

    if i < n-1:
        if matrix[i + 1][j] != 0:
            flag = 'stop'
        matrix[i+1][j] = count
        count += 1
        i += 1
    # elif i == n-1:
    #     matrix[i][j] = count
    #     count += 1
    #     i += 1

def right_step():
    global count
    global i
    global j
    global flag


    if (j < n-1):
        if matrix[i][j + 1] != 0:
            flag = 'stop'
        matrix[i][j+1] = count
        count += 1
        j += 1

flag = 'process'
up_flag_left = 0
left_flag_left = 0
down_flag_left = 0
right_flag_left = 0

shift = 0
shift_up_left = 1
shift_down_right = 2
#while (shift <2 ):


# while a[i][j]
print(flag)

#flag = 'stop'
# while True:
#     if flag == 'stop':
#         break
#
#     for steps in range (10):
#         for step in range(shift_up_left):
#             if flag == 'stop':
#                 break
#             up_step()
#             up_flag_left = +1
#         for step in range(shift_up_left):
#             if flag == 'stop':
#                 break
#             left_step()
#             left_flag_left = +1
#         for step2 in range(shift_down_right):
#             if flag == 'stop':
#                 break
#             down_step()
#             down_flag_left = +1
#         for step2 in range(shift_down_right):
#             if flag == 'stop':
#                 break
#             right_step()
#             right_flag_left = +1
#
#         shift_up_left += 2
#         shift_down_right += 2
# print(flag)


shift +=1



for steps in range (10):
for step in range(shift_up_left):
    if flag == 'stop':
        break
    up_step()
    up_flag_left = +1
for step in range(shift_up_left):
    if flag == 'stop':
        break
    left_step()
    left_flag_left = +1
for step2 in range(shift_down_right):
    if flag == 'stop':
        break
    down_step()
    down_flag_left = +1
for step2 in range(shift_down_right):
    if flag == 'stop':
        break
    right_step()
    right_flag_left = +1

shift_up_left += 2
shift_down_right += 2
print(flag)












#print(matrix[i][j])
#high_border
# if i >= 0:
#     for i in range(i-1, -1, -1):
#         matrix[i][j] = 1



for matr_str in range(0, n):
    print(matrix[matr_str])

print(f'{i=}')
print(f'{j=}')
print(f'{n=}')
print(matrix[i][j])

print(flag)
