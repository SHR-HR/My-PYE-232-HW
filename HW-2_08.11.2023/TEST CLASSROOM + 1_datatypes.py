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
list1 = ["Python", 2, 2.5, b"Python", [1, 2, 3]]  # список - коллекция элементов
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


print(list1)
list2.pop(0) #метод удаления по индексу
print(list1)


