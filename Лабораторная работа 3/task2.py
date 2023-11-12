def find_common_participants(str1,str2,default_arg=','):
    a=[] # создаем пустой список а
    str1_edited=str1.split('|') # разделяем строку str1 по разделителю
    str2_edited=str2.split('|') # разделяем строку str2 по разделителю
    a = list(set(str1_edited).intersection(set(str2_edited))) # находим пересечение
    return a


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = sorted(find_common_participants(participants_first_group,participants_second_group)) # сортируем полученный список с помощью встроенной функции sorted
print(result)