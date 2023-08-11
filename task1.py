# Задача 1
import argparse
# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# Обрабатывайте не числовые данные как исключения.

from log import get_logger


def get_digit():
    while True:
        num = input('Введите целое число: ')
        try:
            num = float(num)
            get_logger().info('Использовано значение ' + str(num))
            return num
        except:
            get_logger().error('Пользователем введено не целое или не вещественное число!')
            print('Введите целое или вещественное число!')