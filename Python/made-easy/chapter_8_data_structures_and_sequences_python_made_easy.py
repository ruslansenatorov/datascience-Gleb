# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: base
#     language: python
#     name: python3
# ---
"""Глава 8."""

import itertools as it

# В Python есть четыре встроенных структуры данных.
#
# ♦ списки;
#
# ♦ кортежи;
#
# ♦ множества;
#
# ♦ словари.
#
# # Строки и операции со строками
#
# Строки можно задать несколькими способами. Их можно заключать в одинарные('') или двойные кавычки ("") - результат будет одинаковый. Их также можно за­ключать в три кавычки. Использование трех кавычек дает возможность записывать строки более чем в одну строку. Примеры:
# 'строка' "строка" """строка"""
#
# Строки - это объекты, и, как у любых объектов, у них есть методы, которые мож­но применять
#
# **capitalize()**
#
# делает первую букву строки заглавной
#
# **upper()**
#
# Делавет все буквы заглавными
#
# **lower()**
#
# Делает все буквы малыми.
#
# **swapcase()**
#
# Меняет регистр на противоположный для каждой буквы
#
# Строки - это неизменяемые объекты, так что эти функции возвращают новую строку с требуемыми изменениями
#
# # Форматирование
#
# Для использования этого метода в строке должны быть заполнители, в которые по­мещаются аргументы метода format() при выполнении. Это позиционный метод, если не указано иное. Это означает, что аргументы в результирующей строке появ­ляются на тех же позициях, что и в format().
#
# # Методы split() и join()
#
# Разделить строку можно с помощью метода split(). Python находит в строке про­белы и символы переноса и возвращает список всех слов из строки.
#
# По умолчанию метод split ( ) делит строку по пробелам. Но мы можем изменить это поведение, передав в него нужный разделитель.
#
#
# words = ['Привет', 'мир', 'это', 'Python']
#
# Объединение списка в строку с пробелами между словами
#
# result = ' '.join(words)
#
# print(result)  # Вывод: Привет мир это Python
#
# # Списки
#
# У списков в Python есть 3 важные  свойства:
#
# ♦ упорядоченность;
#
# ♦ последовательность;
#
# ♦ итерируемость.
#
# **Индексы и срезы**
#

# https://drive.google.com/file/d/14GzvGE3HW1XBpDK7MEo7E50MqL87bVki/view?usp=share_link

# # Методы списков

# https://drive.google.com/file/d/1DOlC68cwbBcURng94pirE_t1u1uQ4fjp/view?usp=share_link

# # Списковые включения
#
# Списковые включения - это краткий и элегантный способ создания списков.
#
# результат = [выражение for элемент in список if условие]

# ![image.png](attachment:image.png)

# # Оператор del

# Если нужно удалить элемент из списка, указав его индекс, а не значение, вы можете использовать оператор del.
# Он отличается от метода рор(), который еще и возвращает значение элемента.
#
# Также del можно использовать для удаления переменных и функций
#
# # Кортежи
#
# Кортежи похожи на списки, но с двумя отличиями.
# ♦ Кортежи неизменяемы, а спискии зменяемы.
# ♦ Кортежи заключаются в круглые скобки, а списки - в квадратные.
# Возникает вопрос: зачем в Python есть две столь похожие встроенные структуры данных - кортежи и списки?
#
# ♦ Хотя кортежи и похожи на списки, они часто используются в разных ситуациях и для разных целей.
#
# ♦ Кортежи неизменяемы и обычно содержат неоднородную последовательность элементов, доступ к которым осуществляется посредством распаковки или индексации (или по имени атрибута в случае именованных кортежей).
#
# ♦ Списки изменяемы, их элементы обычно однородны, а доступ к ним осуществляется путем перебора списка
#
# Где и почему лучше использовать кортежи вместо списков?
# ♦ Когда важна скорость выполнения программы, предпочтительнее использовать кортежи. Программа с кортежами выполняется быстрее по сравнению с такой же программой, но на списках. Но при использовании небольших кортежей и списков разница не ощущается.
#
# ♦ Когда важна целостность данных и вы не хотите, чтобы ваши данные изменя­лись во время выполнения программы. Использование кортежа вместо списка защищает данные от случайного изменения во время выполнения.
# ♦ В Python есть еще один тип данных, называемый словарем. Ключи словаря должны быть неизменяемыми, поэтому для них можно использовать кортежи, а вот списки - нельзя.
#
# **Методы кортежей**
#
# Почти все методы списков также применимы и к кортежам. Вы уже знаете, что кортежи неизменяемы. Следовательно, методы и функции, которые изменяют спи­ски, для кортежей использоваться не могут.
#
# #  Множества
#
# Множество - это неупорядоченная коллекция неповторяющихся элементов. Они используются в основном для проверки вхождения элементов во множество и для устранения дубликатов. Множества также поддерживают математические операции, такие как объединение, пересечение, разность и симметричная разность.
#
# **Операции над множествами**
#
# Множества поддерживают те же операции, что и в работе с математическими мно­жеств
#

# https://drive.google.com/file/d/1osjIFYa0pWE8fMIdnMhF6PY7aGvET8xT/view?usp=share_link

# # Методы множеств

# https://drive.google.com/file/d/1NNN4pyJx5g2mTj27V5sXkFBYQBhQ6I-Z/view?usp=share_link
#
# https://drive.google.com/file/d/1t2wCWyyoHycda7MhtFo7IF-3dQjRYFyN/view?usp=share_link

# # Словари
#
# Словарь - это еще один встроенный тип данных Python. Это неупорядоченный набор единиц данных.
# В обычных словарях, как правило, есть ключ, т. е. слово или элемент, значение ко­торого объясняется в словаре. Это объяснение и есть значение ключа. В Python то же самое.
#
# Лучше всего рассматривать словарь как пары ключ : значение с требованием о том, чтобы ключи в пределах одного словаря были уникальными. Пустой словарь созда­ется с помощью фигурных скобок {}, а наполняется через запятую при помощи пар ключ: значение.
#
# Словарь также можно создать с помощью встроенной функции dict ( )
# Ключ в словаре - это уникальный и неизменяемый тип данных, такой как строка, число или кортеж. Другими словами, в качестве ключей можно использовать только простые типы данных
#
#

# **Методы словарей**

# https://drive.google.com/file/d/1-3Zl5-G0ddrOYWX0sba30vM10EHdCLJe/view?usp=share_link

# # Перебор последовательностей в цикле
#
# При циклическом просмотре словаря ключ и соответствующее значение можно получить одновременно с помощью метода items().
# При переборе последовательности индекс позиции и соответствующее значение можно получить одновременно с помощью функции enumerate()

# # Практическая часть

# ![image.png](attachment:image.png)

# # a)

a_list: list[str] = [letter for letter in "COUNTRY"]
a_list

# # б)

b_list: list[str] = [sml * times for sml in "CAT" for times in range(1, 4)]
b_list

# # в)

c_list: list[list[int]] = [[int(smb)] for smb in [2, 3, 4, 3, 4, 5, 4, 5, 6]]
c_list

# # г)

nums: list[int] = [2, 3, 4, 5, 3, 4, 5, 6, 4, 5, 6, 7, 5, 6, 7, 8]
num5: int = 4
d_list: list[list[int]] = [
    nums[num1 : num1 + num5] for num1 in range(0, len(nums), num5)
]
d_list

# # д)

# +
e_list: list[tuple[int, ...]] = list(
    sorted(it.product([1, 2, 3], repeat=2), key=lambda atb: atb[1]),
)

e_list
# -

# # е)

f_list: list[int] = [item**2 for item in range(10)]
f_list

# 2. Создайте пустой список my_list. Заполните его 50 числами от 1 до 25 (числа могут повторяться)

my_list: list[int] = [num2 for num2 in (list(range(1, 26))) * 2]
my_list

# 3. В списке my_list выполните поиск и узнайте, есть ли в нем числа 11, 18 и 20. Напишите код для поиска этих чисел. Кроме того, узнайте, сколько раз встречаются эти числа в списке

are_in_list = 11 in my_list, 18 in my_list, 20 in my_list
are_in_list

counts = my_list.count(11), my_list.count(18), my_list.count(20)
counts

# 4. Выведите информацию о количестве четных и нечетных чисел в my_list.

even: int = 0
odd: int = 0
for num in my_list:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
even, odd

# 5. Напишите код для создания из my_list другого списка, в котором числа равны квадрату чисел в my_list, но в обратном порядке.

power2_list: list[int] = [obj**2 for obj in my_list][::-1]
power2_list


# 6. Напишите функцию sorted_list(), которая принимает в качестве параметра список и возвращает True, если список отсортирован в порядке возрастания, и False в противном случае. В качестве дополнительного условия вы можете считать, что элементы списка можно сравнивать с помощью операторов отношения «, > и т. д.


def is_sorted_list(sequence: list[int]) -> bool:
    """_summary_.

    Args:
        sequence (list[int]): _description_

    Returns:
        bool: _description_
    """
    for indx in range(len(sequence) - 1):
        if sequence[indx] < sequence[indx + 1]:
            is_or_not: bool = True
        else:
            is_or_not = False
    return is_or_not


is_sorted_list([5, 4, 6, 2])

# 7. Напишите программу Python для ввода имен и номеров телефонов 10 ваших друзей, сохранения их в словаре и вывода номера телефона по заданному имени.

names: list[str] = []
phones: list[str] = []
for thing in range(1, 11):
    name: str = input("Enter a contact name: ")
    phone: str = "+1" + (input("Enter the phone number: +1 "))
    names.append(name)
    phones.append(phone)
contacts: dict[str, str] = dict(zip(names, phones))
contacts


# 8. Напишите функцию remove_duplicates(), которая принимает в качестве параметра список и возвращает новый список, содержащий только уникальные элементы из первого списка. Подсказка: они не обязательно должны сохранять порядок.


def remove_duplicates(your_list: list[int]) -> list[int]:
    """_summary_.

    Args:
        your_list (list[int]): _description_

    Returns:
        list[int]: _description_
    """
    list_set: set[int] = set(your_list)
    return list(list_set)


remove_duplicates([1, 23, 23, 54, 54, 3, 6, 4, 7, 23, 3, 3])


# 9. Напишите функцию для вычисления произведения элементов списка. Что произойдет, если в функцию передать список строк?


def multilist(list_a: list[int]) -> int:
    """_summary_.

    Args:
        list_a (list[int]): _description_

    Returns:
        int: _description_
    """
    score: int = 1
    for mult in list_a:
        score = score * mult
    return score


multilist([1, 2, 3, 4, 5])

# ![image.png](attachment:image.png)
