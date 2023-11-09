bool1 = True  # булевы значения в формате Правда/Ложь
bool2 = False

int1 = 12  # целочисленные значения integer
int2 = -12

float1 = 12.0555555555555554  # значения с плавающей точкой float
float2 = -12.0

str1 = 'Python'
str2 = "Python"
str3 = "i'm student"
str4 = '"Harry Potter" is book'
str5 = """ i'm student "Harry Potter" """

str6 = str1 + str2  # конкатенация (сложение строк)
str7 = 'Python' + " " + "i'm student"

# print(str7)

age = 50
age1 = 25
age2 = 35
str8 = f"Мне {age} лет. Руслану {age1} лет. Роману {age2} лет"  # интерполяция (вставка разных переменных в строку)
# print(str8)


bytes1 = b"Python"  # байты - коллекция символьных элементов в виде байтов
bytes2 = b"\x01\x02\x03\x04\x05"

# print(bytes2)
#           0      1   2      3           4
#            -5      -4    -3   -2        -1
list1 = ["Python", 2, "Python", 2.5, b"Python", [1, 2, 3]]  # список - коллекция элементов
list2 = []
tmp1 = 'Python'
tmp2 = 2
# print(list1[4][1])
# print(list1[-1])


# print(list2)
# list2.append(123)  # добавить в конец
# list2.append(2)  # добавить в конец
# list2.append(222)  # добавить в конец
# print(list2)
# print(list1)
# list1.pop(0)  # удалил по индексу
# print(list1)
# print(list1)
# list1.remove("Python")  # удалил первый элемент
# print(list1)

#         0     1
tuple1 = (12, False)  # кортеж - коллекция неизменяемых элементов
tuple2 = (12,)  # кортеж с одним элементом

set1 = {12, False, 12, 12, 12}  # множество - коллекция уникальных элементов
# print(set1)
# set1.add(12)
# print(set1)
# set1.add(111)
# print(set1)

dict1 = {
    "Имя": "Python",
}  # словарь - коллекция уникальных элементов в формате ключ-значение

#         0  1  2  3
list12 = [1, 2, 3, 4]
# list12[0]
dict_list = {
    0: 1,
    1: 2,
    2: 3,
    3: 4,
}

people = {
    "age": 25,
    "name": "Bogdan",
    "arr": [10, True, []],
    "dict1": {
        "name": "Bogdan",
        "age": 25,
        "arr": [10, True, []],
    },
}

# print(dict1['Имя'])

dict3 = dict(Age=24, Name="Ally")  # создание словаря
# print(dict3)

dict4 = {
    "Age": 24,
    "Name": "Ally"
}  # создание словаря
# print(dict4)

int12 = 12

# Camel Case nameOfFirstPerson
# Snake Case name_of_first_person

INT_CONSTANT = 12  # условно-неизменяемая КОНСТАНТЫ
PI = 3.14
# print(INT_CONSTANT)
# INT_CONSTANT = 12 + 20
# print(INT_CONSTANT)
is_commit = False  # можно изменить
IS_COMMIT = False  # можно изменить, но не желательно

HOST_PASSWORD = "password"

################################################################
# TODO действия с переменными

bool11 = False
int11 = 123
# вывод значение переменной в консоль
# print(bool11, 12, 13, True)

# вывод значение типа переменной в консоль
type_bool11 = type(int11)
# print(type_bool11)
# print(type(bool11))  # type_bool1 = type(bool1)

# проверка принадлежности типа данных
# print(isinstance(bool1, str))  # False
# print(isinstance(bool1, bool))  # True
# print(isinstance(12, int))  # True

# конвертация типов данных:
# print(int11)
# print(type(int11))
# str11 = str(int11)
# print(str11)
# print(type(str11))

float_to_int1 = int(10.5)  # int()
int_to_float1 = float(10)  # float()
str_to_float1 = float("10.2")  # float()
int_to_str1 = str(10.4)  # str()
int_to_bool1 = bool(0)  # bool()  если bool(0) = False, bool("") = False
set_to_list1 = list({1, 2, 2, 5})  # list()
# list_to_set1 = set([1, 2, 2, 5])  # set()
list_to_set1 = set(set_to_list1)  # set()

# получение ввода от пользователя
# str_from_user1 = input("Введите Ваше имя: ")
# print(str_from_user1)

#        012345
str12 = "Python"
# print(str12[-1])
