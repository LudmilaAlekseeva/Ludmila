# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r') as input_file: # открываем файл csv для чтения
        rows=[row for row in csv.DictReader(input_file)] # с помощью list comprehension и DictReader получаем список словарей
        with open(OUTPUT_FILENAME, 'w') as output_file: # открываем для записи файл json
            json_data=json.dump(rows, output_file, indent=4) # с помощью метода dump сериализуем данные в json
        return json_data







if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")