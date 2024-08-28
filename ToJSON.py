import json


def convert_to_json(name, series, number, code, signature):
    data = {
        'Фамилия': name.split()[0],
        'Имя': name.split()[1],
        'Отчество': name.split()[2],
        'Серия': series,
        'Номер': number,
        'Код подразделения': code,
        'Подпись оператора': signature[0],
        'Подпись абонента': signature[1]
    }
    with open('Files/png_folder/data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
