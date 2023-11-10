
# - ЗАДАНИЕ №1

# ВАРИАНТ 1

# # ВВОД НЕОБХОДИМЫХ ДАННЫХ
#
# name = input("Введите имя: ")  # РОМАН
# surname = input("Введите фамилию: ")  # ШАУНИН
# patronymic = input("Введите отчество: ")  # ВЛАДИМИРОВИЧ
# age = int(input("Введите возраст: "))  # 18
#
# # ПРЕОБРАЗОВАНИЕ РЕЗЮМЕ
# resume = f"Здравствуйте! Меня зовут {name} {surname} {patronymic}. Мне {age} и я хочу у Вас работать."
#
# # ИТОГОВЫЙ РЕЗУЛЬТАТ
#
# print(resume)




# ВАРИАНТ 2


#Hello = 'Здравствуйте!'
# My_name_is = 'Меня зовут'
#
# Last_name = 'Шаунин'
# First_name = 'Роман'
# Sur_name = 'Владимирович,'
#
# My_age = 'Мне более 9000 лет'
#
# Mee_need_work = 'и я хочу у Вас работать.'
#
# print(Hello, My_name_is, Last_name, First_name, Sur_name, My_age, Mee_need_work)


# ВАРИАНТ 3

# Hello = 'Здравствуйте!'
# My_name_is = 'Меня зовут'
#
# Last_name = 'Шаунин'
# First_name = 'Роман'
# Sur_name = 'Владимирович'
#
# My_age = 'Мне более 9000 лет'
#
# I_need_work_in_your_company = 'и я хочу у Вас работать.'
#
# Dialog_name = 'Возможно, вы скажите, что: Я слишком стар.'
# Dialog_name2 = 'Но, Я Вам отвечу, что: Я обладаю высочайшими компетенциями в галактике!'
#
# print("Здравствуйте! Меня зовут", Last_name, First_name, Sur_name, My_age,
# "и я мечтаю у Вас работать.", Dialog_name, Dialog_name2)


# ВАРИАНТ 4 (КАК ВАРИАНТ 1 (только чуть-чуть по другому))

# hello = input('Приветствие!') # Здравствуйте! #str0
# what_is_your_name = input('Как Вас зовут?') # Меня зовут #str1
# last_name = input('Фамилия') # Шаунин #str2
# first_name = input('Имя') # Роман #str3
# sur_name = input('Отчество') # Владимирович #str4
# age = 18
# my_age = f". Мне {age} лет и" #str5
# work = input('Какова Ваша цель?') # я хочу у Вас работать. #str6

# resume = [hello + what_is_your_name + last_name + first_name + sur_name + my_age + work]  # так или
# #str7 = str0 + # str1 + str2 + str3 + str4 + str5 + str6 # конкатенация строк (сложение строк)
# print(resume)


# ВАРИАНТ 5

# age = 18
# list0 = 'Здравствуйте''!' ' ' 'Меня зовут'
# list1 = ' ' 'Шаунин' ' ' 'Роман' ' ' 'Владимирович' '.'
# list2 = ' ' 'Мне' ' ' f'{age} лет' ','
# list3 = ' ' 'и' ' ' 'я бы очень' ' ' 'хотел' ' ' 'у Вас работать.'
#
#                     # ??? # tmp0 = list0[0][0][1][2][3]
#                     # ??? # tmp1 = list1[0][1][2][3][4][5][6]
#                     # ??? # tmp2 = list2[0][1][2][3][4]
#                     # ??? # tmp3 = list3[0][1][2][3][4][5][6][7]
#
# tmp0 = list0
# tmp1 = list1
# tmp2 = list2
# tmp3 = list3
#
# tmp4 = tmp0 + tmp1 + tmp2 + tmp3
#
# print(tmp4)


# - ЗАДАНИЕ № 2

# L = 7
# X = 5
# N = L // X  # N = 1
# M = L % X  # M = 2
# print(N, M)


# - ЗАДАНИЕ № 3

# ВАРИАНТ 1

# o = "Hello!"
#
# print(o.isdigit())  # строка состоит только из цифр?
# # False
# print(o.isalpha())  # строка состоит только из букв?
# # False
# print(o.isalnum())  # строка состоит только из цифр и букв?
# # False

# ВАРИАНТ 2

# print(2 * 2 == 4)
# #True
#
# print(1.57*3/1.5 == 3.14)
# # True
#
# print(3 ** 3 - 3 * (6 * 3 - 4.5 * 2) == 1)
# #False


# - ЗАДАНИЕ № 3

# MULTIPLE_VAL = 55.07
#
# def process_input(M):
#     result = M * MULTIPLE_VAL
#     result_int = int(result)
#     result_str = str(result)
#     return result, result_int, result_str
#
# # Ввод числа M
# M = float(input("Введите число M: "))
#
# # Обработка введенного числа
# result, result_int, result_str = process_input(M)
#
# # Вывод результатов
# print("Результат в виде числа с плавающей точкой:", result)
# print("Результат в виде целого числа:", result_int)
# print("Результат в виде строки:", result_str)

# Совсем не то что нужно

# INT_CONSTANT = 35 * 30
# print(INT_CONSTANT)  #string
# INT_CONSTANT = 1050
# print(INT_CONSTANT)  #string
# INT_CONSTANT = 1050 / 2.01
# print(INT_CONSTANT)  #float
# INT_CONSTANT = 522.3880597014926 * 2.01
# print(INT_CONSTANT)  #float
#
# number1 = "1050"
# number2 = "522.3880597014926"
# number3 = "1050.0"
#
# print(number1.isdigit())  # строка состоит только из цифр?
# # True
#
# print(number2.isalpha())  # строка состоит только из букв?
# # False
#
# print(number3.isafloat())  # строка состоит только из цифр?
# True

