
'''
Задание 3. Дихотомия (бинарный поиск) в сдвинутом массиве.
'''

def bin_search():
    a = [5, 6, 7, 8, 1, 2, 3, 4]
    value_for_search = 7
    search_point_index = len(a) // 2
    left_border = 0
    right_border = len(a) - 1

    point = 0
    target = 'none'

    # Поиск индекса (point), после которого массив сдвинут. У нас будет два отсортированных подмассива.
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            #print(a[i])
            point = i
            #print(point)

    #Найдем в каком из вновь образованных подмассивов искомое значение.
    if a[point] == value_for_search:  #нашли
        search_point_index = point

        #target = 'done'
        #print(f'Value Id: {point}')
    elif a[point] > value_for_search and a[0] > value_for_search:
        target = 'right'           #будем искать в правом
    else:
        target = 'left'          #будем искать в левом


    #print(target)

    # Задаем значения для переменных-границ и середины для поиска в левом или правом подмассиве
    if target == 'left':
        search_point_index = point // 2
        left_border = 0
        right_border = point - 1
    elif target == 'right':
        search_point_index = point + (len(a) - point) // 2
        left_border = point + 1
        right_border =  len(a) - 1



    while a[search_point_index] != value_for_search and left_border <= right_border:
        if a[search_point_index] < value_for_search:
            left_border = search_point_index + 1
        else:
            right_border = search_point_index - 1
        search_point_index = (left_border + right_border) // 2

    if value_for_search == a[search_point_index]:
        print(f'Value Id: {search_point_index}')
    else:
        print(f'No Value in list')


bin_search()

