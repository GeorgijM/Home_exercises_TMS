import json, csv
def create_json_file():

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


create_json_file()



def json_read_to_csv():
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
        print(all_data)

        #делаем разметку для будущего csv файла. добавляем разделитель "/", т.к. запятые уже есть во вложенных списках
        j = 1
        # while j < len(all_data):
        #     #print(j)
        #     all_data.insert(j, '/')
        #     j +=2
        # print(all_data)
        all_data_delimetr = []
        for i in all_data:
            all_data_delimetr.append([[x] + ['/'] for x in i])


        #
        # print(all_data)
        #print(a)
        print(all_data_delimetr)
json_read_to_csv()
