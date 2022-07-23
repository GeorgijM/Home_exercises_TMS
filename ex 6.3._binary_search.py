
'''
Задание 3. Дихотомия (бинарный поиск).
'''

def bin_search():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    value_for_search = 8
    search_point_index = len(a) // 2
    left_border = 0
    right_border = len(a) - 1

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