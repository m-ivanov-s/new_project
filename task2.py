# Задача 2

# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.

from log import get_logger

def myGet(dict, key, defaultValue):
    try:
        value = dict[key]
        get_logger().info('Использовано значение ' + str(value))
    except:
        value = defaultValue
        get_logger().error('Использовано значение по умолчанию')
    return value


