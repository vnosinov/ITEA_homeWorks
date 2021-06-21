"""
2. На основе прошлых ДЗ необходимо создать модели представлений для классов ДЕПАРТАМЕНТЫ (Departments),
СОТРУДНИКИ (Employees), ЗАЯВКИ (Orders). Реализовать магические методы вывода информации на экран как для пользователя,
так и для "машинного" отображения.

Предусмотреть все необходимые ограничения и связи моделей между собой.

У каждой модели предусмотрите метод, который бы мог осуществлять запись хранимой в экземпляре информации в отдельный
json-файл с именем вида <id записи>.json. Если id не существует - выдавать ошибку.
"""

import psycopg2
from psycopg2 import sql
from psycopg2 import Error
from datetime import datetime
from envparse import Env
from abc import ABC, abstractmethod

env = Env()

DB_URL = env.str("MY_DB_URL", default="postgres://postgres:dbpass@127.0.0.1:5432/order_service_db")
print(DB_URL)

connect = psycopg2.connect(DB_URL)


class BaseModel(ABC):
    @abstractmethod
    def insert_new_data(self, *args, **kwargs):
        pass

    @abstractmethod
    def delete_data_by_id(self, *args, **kwargs):
        pass


class DataRequiredException(Exception):
    def __init__(self, message, *args, **kwargs):
        self.message = message
        self.args = args
        self.kwargs = kwargs


class Order(BaseModel):
    INSERT_ORDER = sql.SQL("""INSERT INTO orders (created_dt, updated_dt, type_order, description, status, 
    serial_number, creator_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING order_id""")

    def __init__(self, type_order, description, status, serial_number, creator_id, order_id=None):
        self.created_dt = datetime.now()
        self.updated_dt = datetime.now()
        self.type_order = type_order
        self.description = description
        self.status = status
        self.serial_number = serial_number
        self.creator_id = creator_id
        self.__order_id = order_id

    def __str__(self):
        return f'order_id: {self.__order_id}\n' \
               f'created_dt: {self.created_dt}\n' \
               f'updated_dt: {self.updated_dt}\n' \
               f'type_order: {self.type_order}\n' \
               f'description: {self.description}\n' \
               f'status: {self.status}\n' \
               f'serial_number: {self.serial_number}\n' \
               f'creator_id: {self.creator_id}\n'

    def insert_new_data(self):
        with connect, connect.cursor() as cursor:
            cursor.execute(self.__class__.INSERT_ORDER,
                           (datetime.now(), datetime.now(), self.type_order, self.description, self.status,
                            self.serial_number, self.creator_id))
            order_id = cursor.fetchone()[0]
            self.__order_id = order_id

        return {'order_id': order_id}

    def get_order_id(self):
        return self.__order_id

    @staticmethod
    def set_value(value, order_id, column):
        query = f"""UPDATE orders SET {column} = %s, updated_dt = %s WHERE order_id = %s"""
        with connect, connect.cursor() as cursor:
            cursor.execute(query, [value, datetime.now(), order_id])

    @staticmethod
    def update_creator(employee_id, order_id):
        queue = f"""UPDATE orders SET creator_id = %s, updated_dt = %s WHERE order_id = %s"""
        if Employees.check_id(employee_id):
            with connect, connect.cursor() as cursor:
                cursor.execute(queue, [employee_id, datetime.now(), order_id])
        else:
            raise DataRequiredException("the given id is missing in the database ")

    @staticmethod
    def check_order_id(id):
        queue = f"""SELECT order_id FROM orders WHERE order_id = %s"""
        with connect, connect.cursor() as cursor:
            cursor.execute(queue, [id])
            data = cursor.fetchone()
            if not data:
                return False
            else:
                return True

    @staticmethod
    def delete_data_by_id(id):
        queue = f"""DELETE FROM orders WHERE order_id = %s"""
        if Order.check_order_id(id):
            with connect, connect.cursor() as cursor:
                cursor.execute(queue, [id], )
        else:
            raise DataRequiredException("the given id is missing in the database ")


class Employees(BaseModel):
    INSERT_EMPLOYEES = sql.SQL("""INSERT INTO employees (fio, position, department_id) 
        VALUES (%s, %s, %s) RETURNING employee_id""")

    def __init__(self, fio, position, department_id, employee_id=None):
        self.fio = fio
        self.position = position
        self.department_id = department_id
        self.employee_id = employee_id

    def insert_new_data(self):
        with connect, connect.cursor() as cursor:
            cursor.execute(self.__class__.INSERT_EMPLOYEES,
                           (self.fio, self.position, self.department_id))
            employee_id = cursor.fetchone()[0]
            self.employee_id = employee_id

        return {'employee_id': employee_id}

    @staticmethod
    def check_id(id):
        queue = f"""SELECT employee_id FROM employees WHERE employee_id = %s"""
        with connect, connect.cursor() as cursor:
            cursor.execute(queue, [id])
            data = cursor.fetchone()
            if not data:
                return False
            else:
                return True

    @staticmethod
    def delete_data_by_id(id):
        """
        функция работает, но должна быть проверка на наличие заявок от удаленных пользователей
        и либо реализовывать каскадное удаление заявок вместе с пользователем, либо менять структуру данных
        ???
        :param id:
        :return:
        """
        # queue = f"""DELETE FROM employees WHERE employee_id = %s"""
        # if Employees.check_id(id):
        #     with connect, connect.cursor() as cursor:
        #         cursor.execute(queue, [id], )
        # else:
        #     raise DataRequiredException("the given id is missing in the database ")
        pass


class Department(BaseModel):
    INSERT_DEPARTMENT = sql.SQL("""INSERT INTO departments (department_name) 
            VALUES (%s) RETURNING department_id""")

    def __init__(self, department_name, department_id=None):
        self.department_name = department_name
        self.department_id = department_id

    def insert_new_data(self):
        with connect, connect.cursor() as cursor:
            cursor.execute(self.__class__.INSERT_DEPARTMENT, (self.department_name,))
            department_id = cursor.fetchone()[0]
            self.department_id = department_id

        return {'department_id': department_id}

    def delete_data_by_id(id):
        """тот же вопрос что и по пользователям"""
        pass

    @staticmethod
    def show_data():
        data = Department.get_data()
        for x, y in data:
            print(f"ID: {x} NAME: {y}")

    @classmethod
    def get_data(cls):
        queue = f"""SELECT department_id, department_name FROM departments"""
        with connect, connect.cursor() as cursor:
            cursor.execute(queue)
            data = cursor.fetchall()
        return data

    @staticmethod
    def check_id(id):
        queue = f"""SELECT department_id FROM departments WHERE department_id = %s"""
        with connect, connect.cursor() as cursor:
            cursor.execute(queue, [id])
            data = cursor.fetchone()
            if not data:
                return False
            else:
                return True

    @staticmethod
    def update_dep(name, id):
        queue = f"""UPDATE departments SET department_name = %s WHERE department_id = %s"""
        if Department.check_id(id):
            with connect, connect.cursor() as cursor:
                cursor.execute(queue, [name, id])
        else:
            raise DataRequiredException("the given id is missing in the database ")


order1 = Order('business', 'Срочно', 'new', 10021, 7)
# order1.insert_new_data()
# Order.set_value('in_progress', 16, 'status')
# Order.set_value('согласовано шефом', 16, 'description')
# Order.delete_data_by_id(14)
# Order.update_creator(12, 13)

e1 = Employees('Петров Петр Петрович', 'Слесарь', 4)
# e1.insert_new_data()
# e1.delete_data_by_id(11)

d1 = Department('Проектная')
# d1.insert_new_data()
# Department.update_dep('Магазин', 4)
# Department.get_data()

# print(Department.get_data())
Department.show_data()