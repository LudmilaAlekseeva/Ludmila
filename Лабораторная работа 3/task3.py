# TODO  Напишите функцию count_letters
import string # вводим модуль string для дальнейшего быстрого удаления знаков препинания
def count_letters(text):
    text_low=text.lower() # понижаем регистр символов
    words=text_low.split() # разделяем строку на отдельные слова
    words_str="".join(words) # склеиваем слова в единую строку
    for punctuation in string.punctuation:
        words_str=words_str.replace(punctuation,'') # с помощью метода .replace избавляемся от знаков пунктуации (, ; :)
    a=words_str.replace('—', '').replace('…', '') # в переменную а помещаем склеенную строку с убранными - и многоточием
    dict_ = {} # вводим пустой словарь
    for i in a: # i - элемент в строке
        if i in dict_:
            dict_[i]+=1
        else:
            dict_[i]=1
    return dict_


# TODO Напишите функцию calculate_frequency
def calculate_frequency(dict_):
    dict_frequency={} # вводим пустой словарь для частот
    for letter, number in dict_.items(): # letter - ключ (буква), number - значение (кол-во упоминаний символа)
        frequency=number/sum(dict_.values())
        dict_frequency[letter]=frequency
    return dict_frequency

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
result_letters=count_letters(main_str)
result_frequency=calculate_frequency(result_letters)
for letter, frequency in result_frequency.items():
    print(f"{letter}: {frequency:.2f}")