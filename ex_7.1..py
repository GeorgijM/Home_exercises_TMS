import json, csv, time
def create_json_file():
    global People
    People =   [
            {
                "name": "John Smith",
                "birthday": "02.10.1990",
                "height": 175,
                "weight": 76.5,
                "car": True,
                "languages": ["C++", "Python"]
            },
            {
                "name": "Alexey Alexeev",
                "birthday": "05.06.1986",
                "height": 197,
                "weight": 101.2,
                "car": False,
                "languages": ["Pascal", "Delphi"]
            },
            {
                "name": "Maria Ivanova",
                "birthday": "28.08.1998",
                "height": 165,
                "weight": 56.1,
                "car": True,
                "languages": ["C#", "C++", "C"]
            }
        ]



    with open('exercise_7.1.json', 'w') as file_json:
        json.dump(People, file_json, indent=1)


#create_json_file()



def json_read_to_csv():
    global all_data
    with open('exercise_7.1.json') as file_read_to_csv:
        data = json.load(file_read_to_csv)

        #print(data)
        #print(type(data))  #class 'list'
        data_columns_names = [list(data[0].keys())]  #получаем имена столбцов для таблицы, это ключи в словаре
        #print(data_columns_names)
        all_data = data_columns_names.copy()
        for i in data:
            #print(i.values())
            all_data.append(list(i.values())) #добавляем к шапке таблицы значения из словаря

        #print(type(all_data))
        #print(all_data)

        #делаем разметку для будущего csv файла. добавляем разделитель "/", т.к. запятые уже есть во вложенных списках
        #j = 1
        # while j < len(all_data):
        #     #print(j)
        #     all_data.insert(j, '/')
        #     j +=2
        # print(all_data)
        all_data_delimetr = []
        for i in all_data:
            all_data_delimetr.append([[x] + ['/'] for x in i])
        print(all_data_delimetr) #TODO:  как вывести это на печать без скобок


#json_read_to_csv()


def create_csv():
    with open('exercise_7.1.csv', 'w') as file_csv:
        #json_read_to_csv()
        file_writer = csv.writer(file_csv, delimiter='?')
        file_writer.writerows(all_data)

#create_csv()


def save_data_to_csv():
    with open('exercise_7.1.csv', 'a') as file_csv:
        #json_read_to_csv()
        file_writer = csv.writer(file_csv, delimiter='?')
        file_writer.writerows(all_data)



# print('==============')
# print(all_data)

def add_to_json():
    name = input('Name: ')
    birthday = input('Birthday: ')
    height = input('Height: ')
    weight = input('Weight: ')
    car = input('Car: ')
    languages = input('Languages: ').split()

    new_person = [
        {
            "name": name,
            "birthday":  birthday,
            "height": height,
            "weight": weight,
            "car": car,
            "languages": languages
        },
      ]


    with open('exercise_7.1.json', 'r+') as file_add_json:
        People_add = json.load(file_add_json)
        People_add.append(new_person)




        json.dump(People_add, file_add, indent=1)

    save_data_to_csv()
#add_to_json()



#print('=======================')

def add_to_csv():
    name = input('Name: ')
    birthday = input('Birthday: ')
    height = input('Height: ')
    weight = input('Weight: ')
    car = input('Car: ')
    languages = input('Languages: ').split()

    new_person = [

        name,
        birthday,
        height,
        weight,
        car,
        languages
    ]


    with open('exercise_7.1.csv', 'a') as file:


        file_writer = csv.writer(file, delimiter='?')
        file_writer.writerow(new_person)

#add_to_csv()

def person_search_by_name_json():
    with open('exercise_7.1.json') as file_json:
        data = json.load(file_json)
    print(data)
    print('=============')
    for i in data:
        print(i.get('name'))
    name = input('Which person would you like to choose? :')
    for i in data:
        if i.get('name') == name:
            print(i)
            for k in i:
                print(f'{k}:  {i[k]}')

#person_search_by_name_json()

def persons_by_language():
    with open('exercise_7.1.json') as file_json:
        data = json.load(file_json)
    print(data)
    print('=============')
    for i in data:
        print(i.get('languages'))
    language = input('Which language would you like to choose? :')
    for i in data:
        if language in i.get('languages'):
            print(i['name'])

#persons_by_language()

def average_height_till_birth():
    count = 0
    summ_person_higth = 0

    with open('exercise_7.1.json') as file_json:
        data = json.load(file_json)
    print(data)
    print('=============')
    for i in data:
        print(i.get('birthday'))
    birth_date = input('Which date would you like to choose? :')
    # Из модуля time используем метод strptime, который сообщает Питону в каком формате дата
    # для дальнейшего сравнения
    input_date_for_comparison = time.strptime(birth_date, "%d.%m.%Y")


    for i in data:
        person_bday = i.get('birthday')
        person_input_date_for_comparison = time.strptime(person_bday, "%d.%m.%Y")
        if input_date_for_comparison > person_input_date_for_comparison:
            print(i['birthday'])
            count += 1
            person_hight = i.get('height')
            summ_person_higth += person_hight
            print(person_hight)

    if count > 1:
        print(f'There are {count} younger persons. Their average height is'
              f' {summ_person_higth/count} cm.')
    elif count == 1:
        print(f'There is only  one younger person. His height is'
              f' {summ_person_higth / count} cm.')
    else:
        print('There are no younger persons in the database.')



#average_height_till_birth()