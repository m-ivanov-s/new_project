# Задача 1
import argparse
# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# Обрабатывайте не числовые данные как исключения.

import logging

logging.basicConfig(filename="my_log.log", filemode='w', encoding='utf-8', level=logging.ERROR)
logger = logging.getLogger(__name__)


def get_digit():
    while True:
        num = input('Введите целое число: ')
        try:
            num = float(num)
            return num
        except:
            logger.error('Пользователем введено не целое или не вещественное число!')
            print('Введите целое или вещественное число!')


print(get_digit())


# Задача 2

# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.

def myGet(dict, key, defaultValue):
    try:
        value = dict[key]
    except:
        value = defaultValue
        logger.error('Использовано значение по умолчанию')
    return value


dict1 = {1: 7, 5: 4, 8: 1}

print(myGet(dict1, 5, 0))
print(myGet(dict1, 15, 0))

