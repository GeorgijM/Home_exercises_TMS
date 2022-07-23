from random import randint
def guess_number():
    menu = 'Y'
    while menu == "Y":
        for i in range (10, 0, -1):
            random_number = randint(1, 10)
            print(f'Guess the number from 1 to 10. Tryings left {i}')
            number = int(input('Your number is '))
            print(f'The randomizer number is {random_number}')
            if random_number == number:
                print('Your won. Congratulations!!')
                return

        print('Once more time? Y/N')
        menu = input()
        if menu == 'N':
            print('Bye.')
            return
guess_number()