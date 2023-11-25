# TODO решите задачу
import json

INPUT_FILE="input.json"
def task() -> float:
    with open(INPUT_FILE, "r") as f: # открываем для чтения файл JSON
        json_data=json.load(f) # десереализация JSON в объект Python
        score_list=[i["score"] for i in json_data] # с помощью list comprehension создаем список, содержащий значения по ключу "score"
        weight_list=[i["weight"] for i in json_data] # с помощью list comprehension создаем список, содержащий значения по ключу "weight"
        products=[score_list[i]*weight_list[i] for i in range(0, len(score_list))] # с помощью list comprehension создаем список, содержащий произведения элементов первых двух списков
        return sum(products)


print(f"{task():.3f}")
