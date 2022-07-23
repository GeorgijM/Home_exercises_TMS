'''
Задание 1. Фибоначи
'''

print(f'Задание 1')
def fib():
    n = 7
    a = 1
    b = 0
    for i in range(n):
        c = a + b       # искомый член последовательности
        a_next = b  #сохраняем текущее значение переменной b
        b = a + b       #меняем (сдвигаем) b для следующего цикла подсчета переменной с
        a = a_next  # сдвигаем позицию для переменной а на место переменной b
        print(c, end=' ')
    print()
'''
Задание 1. Фибоначи через красивый обмен переменных
'''
fib()

def fib2():
    a = b = 1
    n = 7
    print(a, b, end=' ')

    for i in range(2, n):
        a, b = b, a + b
        print(b, end=' ')
    print()
fib2()

'''Задание 1. Фибоначи через рекурсию'''

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


a = list(range(1, 10))
b = map(fibonacci, a)
c = list(b)
print(c)
print([fibonacci(i) for i in range(1,10)])

'''
Задание 2.Факториал через рекурсию. 
'''
print(f'\nЗадание 2')

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))


'''
Задание 2.Факториал через цикл.
'''

def factorial_for():
    n = 5
    counter = 1
    for i in range(2, n+1):
        counter *= i
    print(counter)

factorial_for()


