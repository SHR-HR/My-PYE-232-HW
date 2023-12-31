LESSON_13_06-07-08.12.2023__MY_HW_№12.py
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
''''
Дата: 06-07-08 ДЕКАБРЯ 2023
'''''
'''
Курс: Разработка Web-приложений на Python, с применением Фреймворка Django
Дисциплина: Основы программирования на Python
'''
'''
Урок №13 от 06.12.2023
Домашнее задание №12:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Выполните следующие задания:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Задание №1.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Дан текстовый файл. 
Необходимо создать новый файл убрав из него все неприемлемые слова. 
Список неприемлемых слов находится в другом файле.
'''
'''
Решение:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Код. ↓ 
'''
def filter_unacceptable_words(source_file, banned_words_file, output_file):
    # Загрузка неприемлемых слов из файла
    with open(banned_words_file, 'r', encoding='utf-8') as ban_file:
        banned_words = set(word.strip().lower() for word in ban_file)

    # Открываем исходный файл для чтения
    with open(source_file, 'r', encoding='utf-8') as input_file:
        # Читаем содержимое файла
        content = input_file.read()

        # Разбиваем текст на слова
        words = content.split()

        # Отфильтровываем слова, исключая неприемлемые
        filtered_words = [word for word in words if word.lower() not in banned_words]

    # Открываем новый файл для записи
    with open(output_file, 'w', encoding='utf-8') as output_file:
        # Записываем отфильтрованные слова в новый файл
        output_file.write(' '.join(filtered_words))

# Пример использования
filter_unacceptable_words('исходный_текст.txt', 'неприемлемые'
                                                '_слова.txt', 'очищенный_текст.txt')
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Шаг №1. Определение функции filter_unacceptable_words
'''
def filter_unacceptable_words(source_file, banned_words_file, output_file):
    # код функции
''''
Эта функция принимает три аргумента: 
source_file (путь к исходному файлу), banned_words_file (путь к файлу с неприемлемыми словами), 
и output_file (путь для записи отфильтрованного текста).
''''
'''
Шаг №2. Загрузка неприемлемых слов из файла
'''
with open(banned_words_file, 'r', encoding='utf-8') as ban_file:
    banned_words = set(word.strip().lower() for word in ban_file)
'''
Здесь открывается файл с неприемлемыми словами (banned_words_file), и каждое слово читается, убираются пробелы,
и они преобразуются в нижний регистр. Затем эти слова добавляются в множество banned_words.
'''
'''
Шаг №3. Открытие исходного файла для чтения
'''
with open(source_file, 'r', encoding='utf-8') as input_file:
    content = input_file.read()
'''
Открывается исходный файл (source_file) для чтения, и его содержимое читается в переменную content.
'''
'''
Шаг №4. Разбиение текста на слова
'''
words = content.split()
'''
Текст из переменной content разбивается на слова, и результат сохраняется в списке words.
'''
'''
Шаг №5. Фильтрация неприемлемых слов
'''
filtered_words = [word for word in words if word.lower() not in banned_words]
'''
Создается новый список filtered_words, в который включаются только те слова из списка words, 
которые не являются неприемлемыми (не находятся в множестве banned_words). Все слова сравниваются в нижнем регистре.
'''
'''
Шаг №6. Открытие нового файла для записи
'''
with open(output_file, 'w', encoding='utf-8') as output_file:
'''
Открывается новый файл (output_file) для записи отфильтрованных слов.
'''
'''
Шаг №7. Запись отфильтрованных слов в новый файл
'''
output_file.write(' '.join(filtered_words))
'''
Отфильтрованные слова объединяются в строку с использованием пробела в качестве разделителя, 
и эта строка записывается в открытый файл.
'''
'''
Пример использования
'''
# Пример использования функции
filter_unacceptable_words('исходный_текст.txt', 'неприемлемые_слова.txt',
                          'очищенный_текст.txt')
'''
В примере вызывается функция filter_unacceptable_words с указанными исходным файлом, файлом неприемлемых слов и 
файлом для вывода. Функция читает текст из исходного файла, фильтрует 
неприемлемые слова, и записывает результат в указанный файл.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Задание №2.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Написать программу транслитерации с русского на английский и наоборот. 
Данные для транслитерации берутся из файла и записываются в другой файл. 
Направление перевода определяется через меню пользователя.
'''
'''
Решение:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Код. ↓ 
'''
def transliterate(input_str, direction='ru-en'):
    translit_table = {
        'ru-en': {
            'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z',
            'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
            'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
            'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya',
        },
        'en-ru': {v: k for k, v in {
            'a': 'а', 'b': 'б', 'v': 'в', 'g': 'г', 'd': 'д', 'e': 'е', 'zh': 'ж', 'z': 'з',
            'i': 'и', 'y': 'й', 'k': 'к', 'l': 'л', 'm': 'м', 'n': 'н', 'o': 'о', 'p': 'п', 'r': 'р',
            's': 'с', 't': 'т', 'u': 'у', 'f': 'ф', 'kh': 'х', 'ts': 'ц', 'ch': 'ч', 'sh': 'ш', 'shch': 'щ',
            'y': 'ы', 'yu': 'ю', 'ya': 'я',
        }.items()}
    }

    result = ''
    for char in input_str:
        result += translit_table[direction].get(char.lower(), char)

    return result


def main():
    input_file = input("Введите имя файла для транслитерации: ")

    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Файл '{input_file}' не найден.")
        return

    direction = input("Выберите направление транслитерации ('ru-en' для русско-английского, 'en-ru' "
                      "для англо-русского): ")
    if direction not in ['ru-en', 'en-ru']:
        print("Неверное направление транслитерации.")
        return

    output_file = input("Введите имя файла для сохранения результата транслитерации: ")

    result = transliterate(content, direction)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(result)

    print(f"Транслитерация завершена. Результат сохранен в файл '{output_file}'.")


if __name__ == "__main__":
    main()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Шаг №1. Определение функции transliterate
'''
def transliterate(input_str, direction='ru-en'):
    # код функции
''''
Функция transliterate принимает строку input_str для транслитерации и необязательный параметр direction,
который указывает направление транслитерации. По умолчанию установлено значение 'ru-en'.
''''
'''
Шаг №2. Создание таблицы транслитерации
'''
translit_table = {
    # таблица транслитерации для ru-en
    'ru-en': {
        # русские буквы и их английские аналоги
    },
    # таблица транслитерации для en-ru
    'en-ru': {
        # английские буквы и их русские аналоги
    }
}
'''
translit_table - это словарь, содержащий таблицы транслитерации для русско-английского (ru-en) и
англо-русского (en-ru) направлений.
'''
'''
Шаг №3. Итерация по символам входной строки
'''
for char in input_str:
# код для каждого символа
'''
Цикл for проходит по каждому символу в строке input_str.
'''
'''
Шаг №4. Получение соответствующего символа из таблицы транслитерации
'''
result += translit_table[direction].get(char.lower(), char)
'''
Для каждого символа входной строки происходит поиск его транслитерированной версии в таблице translit_table в
соответствии с выбранным направлением direction. Если символ не найден, он остается неизменным.
'''
'''
Шаг №5. Возврат результата транслитерации
'''
return result
'''
Функция возвращает результирующую строку после завершения транслитерации.
'''
'''
Пример использования функции
'''
# Пример использования функции
transliterate('Привет, мир!', 'ru-en')
'''
Этот вызов функции транслитерирует строку 'Привет, мир!' с русского на английский с использованием
таблицы транслитерации ru-en.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Задание №3.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Пользователь с клавиатуры вводит названия файлов, до тех пор, пока он не введет слово quit.
После завершения ввода программа должна объединить содержимое всех перечисленных пользователем файлов в один.
'''
'''
Решение:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Код. ↓ 
'''
def merge_files(output_filename):
    # Открываем выходной файл для записи
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        while True:
            # Запрашиваем у пользователя ввод имени файла
            filename = input("Введите имя файла (или 'quit' для завершения): ")

            # Проверяем, если пользователь ввел 'quit', завершаем цикл
            if filename.lower() == 'quit':
                break

            try:
                # Открываем файл для чтения и читаем его содержимое
                with open(filename, 'r', encoding='utf-8') as input_file:
                    file_content = input_file.read()

                # Записываем содержимое файла в выходной файл
                output_file.write(file_content)

            except FileNotFoundError:
                print(f"Файл '{filename}' не найден. Попробуйте снова.")

    print(f"Объединение файлов завершено. Результат сохранен в файле '{output_filename}'.")


if __name__ == "__main__":
    output_filename = input("Введите имя файла для сохранения объединенного содержимого: ")
    merge_files(output_filename)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Шаг №1. Определение функции merge_files
'''
def merge_files(output_filename):
    # код функции
''''
Эта функция принимает имя файла (output_filename), в который будет записан результат объединения.
''''
'''
Шаг №2. Открытие выходного файла
'''
with open(output_filename, 'w', encoding='utf-8') as output_file:
'''
Открываем выходной файл для записи объединенного содержимого.
'''
'''
Шаг №3. Цикл ввода имен файлов
'''
while True:
    filename = input("Введите имя файла (или 'quit' для завершения): ")
'''
Ввод имен файлов происходит в цикле. Если пользователь вводит 'quit', цикл завершается.
'''
'''
Шаг №4. Чтение и объединение файлов
'''
with open(filename, 'r', encoding='utf-8') as input_file:
    file_content = input_file.read()
'''
Открываем каждый файл, читаем его содержимое и добавляем к содержимому выходного файла.
'''
'''
Шаг №5. Обработка ошибок
'''
except FileNotFoundError:
    print(f"Файл '{filename}' не найден. Попробуйте снова.")
'''
Если файл не найден, выводится сообщение об ошибке.
'''
'''
Шаг №6. Завершение программы
'''
print(f"Объединение файлов завершено. Результат сохранен в файле '{output_filename}'.")
'''
По завершении ввода имен файлов выводится сообщение о завершении программы и сохранении результата в указанный файл.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Задание №4.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Пользователь с клавиатуры вводит названия файлов, до тех пор, пока он не введет слово quit. 
После завершения ввода программа должна записать в итоговый файл символы, которые есть во всех перечисленных файлах 
(символы должны быть в каждом файле).
'''
'''
Решение:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Код. ↓ 
'''
def get_common_characters(filenames):
    # Инициализируем переменную для хранения общих символов
    common_characters = set()

    # Проверка наличия файлов и получение уникальных символов
    for i, filename in enumerate(filenames, start=1):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                # Получаем символы из текущего файла
                characters = set(file.read())

                # Если common_characters пусто, добавляем все символы из первого файла
                if i == 1:
                    common_characters.update(characters)
                else:
                    # Обновляем common_characters, оставляя только общие символы
                    common_characters.intersection_update(characters)
        except FileNotFoundError:
            print(f"Файл '{filename}' не найден. Пропускаем.")

    return common_characters


def main():
    # Инициализируем список для хранения имен файлов
    filenames = []

    # Запрашиваем у пользователя ввод имен файлов
    while True:
        filename = input("Введите имя файла (или 'quit' для завершения): ")
        if filename.lower() == 'quit':
            break
        filenames.append(filename)

    # Получаем общие символы из всех файлов
    common_characters = get_common_characters(filenames)

    if common_characters:
        # Записываем общие символы в итоговый файл
        with open('итоговый_файл.txt', 'w', encoding='utf-8') as result_file:
            result_file.write(''.join(common_characters))

        print("Общие символы записаны в итоговый файл.")
    else:
        print("Нет общих символов в файлах.")


if __name__ == "__main__":
    main()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Шаг №1: Определение функции get_common_characters
'''
def get_common_characters(filenames):
''''
Производится определение функции get_common_characters, которая принимает аргумент filenames — список имен файлов.
''''
'''
Шаг №2: Инициализация переменной common_characters
'''
common_characters = set()
'''
Создается пустое множество common_characters, в котором будут храниться общие символы из всех файлов.
'''
'''
Шаг №3: Цикл для обработки каждого файла
'''
for i, filename in enumerate(filenames, start=1):
'''
Используется цикл for для обработки каждого файла в списке filenames. Функция enumerate позволяет получить итератор,
который возвращает пары индекса и значения из списка. Параметр start=1 указывает начальное значение индекса.
'''
'''
Шаг №4: Блок try-except для обработки исключений
'''
try:
'''
Этот блок используется для обработки исключений, таких как FileNotFoundError, 
которые могут возникнуть при работе с файлами.
'''
'''
Шаг №5: Открытие файла с явным указанием кодировки UTF-8
'''
with open(filename, 'r', encoding='utf-8') as file:
'''
Открывается файл для чтения ('r') с использованием кодировки UTF-8. 
Оператор with гарантирует, что файл будет закрыт после завершения блока кода, даже если возникнет исключение.
'''
'''
Шаг №6: Чтение файла и создание множества уникальных символов
'''
characters = set(file.read())
'''
Читается содержимое файла, и на его основе создается множество characters с уникальными символами из файла.
'''
'''
Шаг №7: Проверка, является ли текущий файл первым в списке
'''
if i == 1:
    common_characters.update(characters)
'''
Проверяется, является ли текущий файл первым в списке. 
Если да, то все символы из этого файла добавляются в множество common_characters с помощью метода update.
'''
'''
Шаг №8: Обновление множества common_characters
'''
else:
common_characters.intersection_update(characters)
'''
Если текущий файл не первый в списке, множество common_characters обновляется, оставляя только те символы,
которые встречаются и в текущем файле, и в предыдущих файлах. В данном случае используется метод intersection_update.
'''
'''
Шаг №9: Обработка исключения FileNotFoundError
'''
except FileNotFoundError:
print(f"Файл '{filename}' не найден. Пропускаем.")
'''
Если файл не найден, выводится сообщение об ошибке.
'''
'''
Шаг №10: Возвращение множества common_characters
'''
return common_characters
'''
Функция возвращает множество common_characters, содержащее общие символы из всех файлов.
'''
'''
Это охватывает основные шаги внутри функции get_common_characters. Переходите ко второй части кода, функции main.
'''
def main():
''''
Это определение функции main, которая является основной точкой входа в программу.
'''''
'''
Шаг №11: Инициализация пустого списка filenames
'''
filenames = []
'''
Создается пустой список filenames для хранения имен файлов.
'''
'''
Шаг №12: Начало бесконечного цикла для ввода имен файлов
'''
    while True:
'''
Запускается бесконечный цикл для запроса у пользователя имен файлов.
'''
'''
Шаг №13: Запрос у пользователя имени файла
'''
        filename = input("Введите имя файла (или 'quit' для завершения): ")
'''
Пользователю предлагается ввести имя файла.
'''
'''
Шаг №14: Проверка условия выхода из цикла
'''
        if filename.lower() == 'quit':
            break
'''
Если пользователь ввел 'quit', цикл завершается.
'''
'''
Шаг №15: Добавление имени файла в список filenames
'''
filenames.append(filename)
'''
Имя файла, введенное пользователем, добавляется в список filenames.
'''
'''
Шаг №16: Вызов функции get_common_characters для получения общих символов
'''
common_characters = get_common_characters(filenames)
'''
Вызывается функция get_common_characters для получения множества общих символов из всех файлов, 
находящихся в списке filenames.
'''
'''
Шаг №17: Проверка наличия общих символов
'''
if common_characters:
'''
Проверяется, есть ли общие символы.
'''
'''
Шаг №18: Открытие файла для записи общих символов
'''
with open('итоговый_файл.txt', 'w', encoding='utf-8') as result_file:
'''
Открывается файл 'итоговый_файл.txt' для записи общих символов с явным указанием кодировки UTF-8.
'''
'''
Шаг №19: Запись общих символов в файл
'''
result_file.write(''.join(common_characters))
'''
Общие символы записываются в файл с использованием метода write.
'''
'''
Шаг №20: Вывод сообщения об успешной записи
'''
print("Общие символы записаны в итоговый файл.")
'''
Выводится сообщение об успешной записи общих символов в файл.
'''
'''
Шаг №21: Иначе (если общих символов нет)
'''
else:
print("Нет общих символов в файлах.")
'''
Если общих символов нет, выводится сообщение об этом.
'''
'''
Шаг №22: Проверка условия if __name__ == "__main__":
'''
if __name__ == "__main__":
'''
Это проверка, выполняется ли скрипт напрямую (а не импортируется как модуль). Если да, то вызывается функция main.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Работа с файлами и каталогами
'''
'''
Выполните следующее задание:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Задание №1
В текущей папке лежат две другие папки: video и sub. Создайте новую папку watch_me и переложите туда содержимое
указанных папок (сами папки класть не надо).

Задание №2
В текущей папке лежат файлы типа Nina_Stoletova.jpg, Misha_Perelman.jpg и т.п. 
Переименуйте их переставив имя и фамилию местами.

Задание №3
В текущей папке лежит файл list.tsv, в котором с новой строки написаны имена некоторых других файлов этой папки.
Создайте папку list и переложите в неё данные файлы.

Задание №4
Дан текстовый файл. Удалить из него последнюю строку. Результат записать в другой файл.
'''
'''
Решение:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Код - Задания №1. ↓ 
'''
import os
import shutil

# Создаем новую папку 'watch_me'
new_folder = 'watch_me'
os.makedirs(new_folder, exist_ok=True)

# Список папок для копирования
folders_to_copy = ['video', 'sub']

# Копируем содержимое указанных папок в новую папку 'watch_me'
for folder in folders_to_copy:
    source_path = os.path.join(os.getcwd(), folder)
    destination_path = os.path.join(os.getcwd(), new_folder)
    shutil.copytree(source_path, os.path.join(destination_path, folder))

print("Задание №1 выполнено.")
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Шаг №1: Создание новой папки
'''
import os
import shutil
# Создаем новую папку 'watch_me'
new_folder = 'watch_me'
os.makedirs(new_folder, exist_ok=True)
'''
На этом шаге используются модули os и shutil для создания новой папки с именем 'watch_me'. Функция os.makedirs()
используется для создания папки, и exist_ok=True гарантирует, что, если папка уже существует, не возникнет ошибок.
'''
'''
Шаг №2: Подготовка копирования
'''
# Список папок для копирования
folders_to_copy = ['video', 'sub']
'''
На этом шаге создается список folders_to_copy, содержащий имена папок, которые нужно скопировать.
'''
'''
Шаг №3: Копирование содержимого указанных папок
'''
# Копируем содержимое указанных папок в новую папку 'watch_me'
for folder in folders_to_copy:
    source_path = os.path.join(os.getcwd(), folder)
    destination_path = os.path.join(os.getcwd(), new_folder)
    shutil.copytree(source_path, os.path.join(destination_path, folder))
'''
На этом шаге используется цикл for, чтобы пройти по каждой папке в списке folders_to_copy.
Для каждой папки формируются пути и используется shutil.copytree() для рекурсивного копирования содержимого папки
из source_path в destination_path. Таким образом, содержимое каждой из указанных папок копируется в 
новую папку 'watch_me'.
'''
'''
Шаг №4: Вывод сообщения о завершении задания
'''
print("Задание №1 выполнено.")
'''
На последнем шаге выводится простое сообщение, уведомляющее о том, что задание выполнено.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Код - Задания №2. ↓ 
'''
import os

# Получаем список файлов в текущей папке
files = [file for file in os.listdir() if os.path.isfile(file) and file.endswith('.jpg')]

# Переименовываем файлы, переставляя имя и фамилию местами
for file in files:
    file_name, extension = os.path.splitext(file)
    parts = file_name.split('_')
    if len(parts) == 2:
        new_name = f"{parts[1]}_{parts[0]}{extension}"
        os.rename(file, new_name)

print("Задание №2 выполнено.")
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Шаг №1: Получение списка файлов
'''
'''
На этом шаге используется модуль os для получения списка файлов в текущей рабочей папке, которые являются файлами 
(а не папками) и имеют расширение '.jpg'. Список файлов сохраняется в переменной files.

Пример кода:
'''
files = [file for file in os.listdir() if os.path.isfile(file) and file.endswith('.jpg')]
'''
Шаг №2: Переименование файлов
'''
'''
На этом шаге используется цикл for, чтобы пройти по каждому файлу в списке files. 
Для каждого файла выполняется следующее:

os.path.splitext(file) используется для разделения имени файла и его расширения.
file_name.split('_') разделяет имя файла на части с использованием символа подчеркивания.
Если результат разделения содержит две части (ожидается, что это имя и фамилия), то происходит переименование файла,
меняя местами имя и фамилию.
os.rename(file, new_name) выполняет фактическое переименование файла.

Пример кода:
'''
for file in files:
    file_name, extension = os.path.splitext(file)
    parts = file_name.split('_')
    if len(parts) == 2:
        new_name = f"{parts[1]}_{parts[0]}{extension}"
        os.rename(file, new_name)
'''
Шаг №3: Вывод сообщения о завершении задания
'''
'''
На последнем шаге выводится простое сообщение, уведомляющее о том, что задание выполнено.

Пример кода:
'''
print("Задание №2 выполнено.")
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Код - Задания №3. ↓ 
'''
import os
import shutil

# Читаем имена файлов из файла list.tsv
with open('list.tsv', 'r', encoding='utf-8') as file:
    file_names = [line.strip() for line in file]

# Создаем папку 'list'
list_folder = 'list'
os.makedirs(list_folder, exist_ok=True)

# Копируем файлы в новую папку 'list'
for file_name in file_names:
    source_path = os.path.join(os.getcwd(), file_name)
    destination_path = os.path.join(os.getcwd(), list_folder)
    shutil.copy(source_path, destination_path)

print("Задание №3 выполнено.")
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Шаг №1: Чтение имен файлов из файла list.tsv
'''
'''
На этом шаге используется оператор with, чтобы открыть файл 'list.tsv' в режиме 
чтения ('r') с указанием кодировки utf-8. Затем для каждой строки файла удаляются лишние пробелы и 
символы новой строки, и результат сохраняется в списке file_names.

Пример кода:
'''
with open('list.tsv', 'r', encoding='utf-8') as file:
    file_names = [line.strip() for line in file]
'''
Шаг №2: Создание новой папки 'list'
'''
'''
На этом шаге используется модуль os для создания новой папки с именем 'list'. 
Функция os.makedirs() используется для создания папки, и exist_ok=True гарантирует, что, если папка 
уже существует, не возникнет ошибок.

Пример кода:
'''
list_folder = 'list'
os.makedirs(list_folder, exist_ok=True)
'''
Шаг №3: Копирование файлов в новую папку 'list'
'''
'''
На этом шаге используется цикл for, чтобы пройти по каждому имени файла в списке file_names.
Для каждого файла формируются пути и используется shutil.copy() для копирования файла из
source_path в destination_path.

Пример кода:
'''
for file_name in file_names:
    source_path = os.path.join(os.getcwd(), file_name)
    destination_path = os.path.join(os.getcwd(), list_folder)
    shutil.copy(source_path, destination_path)
'''
Шаг №4: Вывод сообщения о завершении задания
'''
'''
На последнем шаге выводится простое сообщение, уведомляющее о том, что задание выполнено.

Пример кода:
'''
print("Задание №3 выполнено.")
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Код - Задания №4. ↓ 
'''
with open('intput.txt') as file:
    lines = file.readlines()

# Если файл не пустой и есть хотя бы одна строка, удаляем последнюю строку
if lines:
    lines.pop()

# Записываем оставшиеся строки в другой файл
with open('output.txt', 'w', encoding='utf-8') as output_file:
    output_file.writelines(lines)

print("Задание №4 выполнено.")
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Шаг №1: Чтение содержимого файла
'''
'''
На этом шаге используется оператор with, чтобы открыть файл 'PR.txt' в режиме чтения ('r') с указанием 
кодировки utf-8. Затем функция readlines() используется для чтения всех строк из файла и сохранения 
их в переменной lines.

Пример кода:
'''
with open('intput.txt') as file:
    lines = file.readlines()
'''
Шаг №2: Удаление последней строки, если файл не пустой
'''
'''
На этом шаге проверяется, не пуст ли файл (содержит ли он хотя бы одну строку). Если файл не пуст, 
то с использованием метода pop() удаляется последняя строка из списка lines.

Пример кода:
'''
if lines:
    lines.pop()
'''
Шаг №3: Запись оставшихся строк в другой файл
'''
'''
На этом шаге создается новый файл 'output.txt' в режиме записи ('w') с указанием кодировки utf-8. 
Затем метод writelines() используется для записи оставшихся строк из списка lines в этот новый файл.

Пример кода:
'''
with open('output.txt', 'w', encoding='utf-8') as output_file:
    output_file.writelines(lines)
'''
Шаг №4: Вывод сообщения о завершении задания
'''
'''
На последнем шаге выводится простое сообщение, уведомляющее о том, что задание выполнено.

Пример кода:
'''
print("Задание №4 выполнено.")

