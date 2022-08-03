class SuperStr:
    def __init__(self, string):
        self.string = string

    def is_repeatance(self, string_part):
        count = 0
        if type(string_part) != str or self.string == '':
            return False
        string_part_length = len(string_part)
        list_string = [self.string[i:i + len(string_part)]
                       for i in range(0, len(self.string), len(string_part))]

        for i in list_string:
            if i == string_part:
                count += 1

        if count == len(list_string):
            return True
        else:
            return False

    def is_palindrom(self):
        if self.string == '' \
                or self.string == self.string[::-1]:
            return True
        else:
            return False


string_1 = SuperStr('asdfasdfasdfasdf')
print(string_1.is_repeatance('asdf'))

string_2 = SuperStr('')
print(string_2.is_repeatance('asdf'))

string_3 = SuperStr('akas')
string_4 = SuperStr('aka')
print(string_3.is_palindrom())
print(string_4.is_palindrom())
print(string_2.is_palindrom())
