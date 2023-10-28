volume = 1.44 # объем дискеты, Мб
num_of_pages = 100 # количество страниц в книге, шт
strings_on_the_page = 50 # число строк на странице, шт
num_of_symbols = 25 # количество символов в строке, шт
volume_for_symbol = 4 # объем памяти для одного символа, байт
volume_of_book = num_of_pages * strings_on_the_page * num_of_symbols * volume_for_symbol / 1024**2 # объем книги, Мб
number_of_books = volume / volume_of_book # количество книг, которые можно поместить на дискету
print("Количество книг, помещающихся на дискету:", round(number_of_books))