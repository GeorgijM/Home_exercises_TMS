def arithmetic_progression(first_element, elements_amount, multiplier):
    for i in range(1, elements_amount+1):
        yield first_element * multiplier ** (i-1)

for item in arithmetic_progression(2, 10, 2):
    print(item)


def fibonachi (n):
    a = b = 1
    for i in range (1, n+1):
        a, b = b, a + b
        yield a

for item in fibonachi(10):
    print(item)