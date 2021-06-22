"""
1. Напишите декоратор для класса, который бы при создании экземпляра этого класса осуществлял бы запись информации об
этом в текстовый файл. Пример записи: 2012-01-01 15:04 Создан экземпляр класса TestClass по адресу памяти x01223342


"""


from datetime import datetime


def deco_class_info(cls):
    def inner():
        with open("class_info.txt", "a", encoding="utf-8") as f:
            info = f"{datetime.now()} Создан экземпляр класса {cls} по адресу памяти {hex(id(cls))}\n"
            f.write(info)

        return cls
    return inner


@deco_class_info
class Class1:
    pass


@deco_class_info
class Class2:
    pass


c1 = Class1()
c2 = Class1()