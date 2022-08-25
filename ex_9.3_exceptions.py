class OperatorException(Exception):
    def __init__(self, operator):
        self.operator = operator

    def __str__(self):
        return f'The operator symbol "{operator}" is incorrect'




def calculator():
    try:
        print("Input operand X, than OPERATOR(+, -, /, *), than operand Y")
        x = float(input('X= '))
        operator = input('OPERATOR(+, -, /, *): ')
        # assert operator in ['+', '-', '/', '*'], 'Please change the operator'
        if operator not in ['+', '-', '/', '*']:
            raise OperatorException(operator)
        y = float(input('Y= '))

        if operator == '+':
            print(f'{x} {operator} {y} =', end=' ')
            print(addition(x, y))
        elif operator == '-':
            print(f'{x} {operator} {y} =', end=' ')
            print(subtraction(x, y))
        elif operator == '*':
            print(f'{x} {operator} {y} =', end=' ')
            print(multiplication(x, y))
        elif operator == '/':
            print(f'{x} {operator} {y} =', end=' ')
            print(division(x, y))

    except ZeroDivisionError:
        print('Error: division by zero. Change Y.')
    except ValueError:
        print('Value error. Insert numbers.')
    except OperatorException:
        print(f'Unknown operator')


def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b


calculator()
