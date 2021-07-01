"""
Продолжаем работу над нашей CRM. Теперь нужно реализовать несколько web-ручек для управления нашей системой:

    создание департамента, заявки, сотрудника
    редактирование информации о департаменте, заявке сотруднике
    удаление данных о заявке, департаменте и сотруднике
    поиск по id/дате/любому другому параметру (на ваш выбор) департамента, сотрудника, зявки



Для выполнения ДЗ можно использовать интеграцию с любой изученной БД (sqlite, Postgresql, Mongo)
"""
import psycopg2
from psycopg2 import sql
from datetime import datetime
from envparse import Env
from abc import ABC, abstractmethod
from os import path
import json

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
    def get_data():
        queue = f"""SELECT created_dt, updated_dt, type_order, description, status,
                serial_number, creator_id 
                FROM orders"""
        with connect, connect.cursor() as cursor:
            cursor.execute(queue)
            data = cursor.fetchall()
        return data

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

    def show(self):
        return {"ID": self.__order_id, "created_dt": str(self.created_dt), "updated_dt": str(self.updated_dt),
                "type_order": self.type_order, "description": self.description, "status": self.status,
                "serial_number": self.serial_number, "creator_id": self.creator_id}

    def __str__(self):
        return f'order_id: {self.__order_id}\n' \
               f'created_dt: {self.created_dt}\n' \
               f'updated_dt: {self.updated_dt}\n' \
               f'type_order: {self.type_order}\n' \
               f'description: {self.description}\n' \
               f'status: {self.status}\n' \
               f'serial_number: {self.serial_number}\n' \
               f'creator_id: {self.creator_id}'

    def save_in_json(self):
        if self.__order_id is None:
            print("ID не может быть None")
        else:
            if not path.exists(f"Order_ID_{self.__order_id}.json"):
                with open(f"Order_ID_{self.__order_id}.json", "x", encoding="utf-8") as f:
                    f.write("{}")

            with open(f"Order_ID_{self.__order_id}.json", "w") as f:
                data = self.show()
                data["Time of creation"] = f"{datetime.now()}"
                f.write(json.dumps(data, indent=4))


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
    def get_data():
        queue = f"""SELECT fio, position, department_id FROM employees"""
        with connect, connect.cursor() as cursor:
            cursor.execute(queue)
            data = cursor.fetchall()
        return data

    @staticmethod
    def get_by_id(id_):
        queue = f"""SELECT fio, position, department_id FROM employees WHERE employee_id = %s"""
        with connect, connect.cursor() as cursor:
            cursor.execute(queue, [id_])
            data = cursor.fetchone()
        return data

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
        queue = f"""DELETE FROM employees WHERE employee_id = %s"""
        if Employees.check_id(id):
            with connect, connect.cursor() as cursor:
                cursor.execute(queue, [id],)
        else:
            raise DataRequiredException("the given id is missing in the database ")

    def show(self):
        return {"ID": self.employee_id, "FIO": self.fio, "POSITION": self.position, "DEP_ID": self.department_id}

    def __str__(self):
        return f"ID: {self.employee_id} FIO: {self.fio} POSITION: {self.position} DEP_ID: {self.department_id}"

    # def __repr__(self):
    #     return f"ID('{self.department_id}') NAME('{self.department_name}')"

    def save_in_json(self):
        if self.employee_id is None:
            print("ID не может быть None")
        else:
            if not path.exists(f"Emp_ID_{self.employee_id}.json"):
                with open(f"Emp_ID_{self.employee_id}.json", "x", encoding="utf-8") as f:
                    f.write("{}")

            with open(f"Emp_ID_{self.employee_id}.json", "w") as f:
                data = self.show()
                data["Time of creation"] = f"{datetime.now()}"
                f.write(json.dumps(data, indent=4))


class Department(BaseModel):
    INSERT_DEPARTMENT = sql.SQL("""INSERT INTO departments (department_name) 
            VALUES (%s) RETURNING department_id""")

    def __init__(self, department_name, department_id=None) -> object:
        self.department_name = department_name
        self.department_id = department_id

    def insert_new_data(self):
        with connect, connect.cursor() as cursor:
            cursor.execute(self.__class__.INSERT_DEPARTMENT, (self.department_name,))
            department_id = cursor.fetchone()[0]
            self.department_id = department_id
        return {'department_id': department_id}

    @staticmethod
    def delete_data_by_id(id):
        queue = f"""DELETE FROM departments WHERE department_id = %s"""
        with connect, connect.cursor() as cursor:
            cursor.execute(queue, [id])

    @staticmethod
    def show_all_data():
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
    def get_data_by_id(id_):
        queue = f"""SELECT department_name FROM departments WHERE department_id = %s"""
        with connect, connect.cursor() as cursor:
            cursor.execute(queue, [id_])
            data = cursor.fetchone()
        return data

    @staticmethod
    def check_id(id_):
        queue = f"""SELECT department_id FROM departments WHERE department_id = %s"""
        with connect, connect.cursor() as cursor:
            cursor.execute(queue, [id_])
            data = cursor.fetchone()
            if not data:
                return False
            else:
                return True

    @staticmethod
    def update_dep(name, id_):
        queue = f"""UPDATE departments SET department_name = %s WHERE department_id = %s"""
        if Department.check_id(id_):
            with connect, connect.cursor() as cursor:
                cursor.execute(queue, [name, id_])
        else:
            raise DataRequiredException("the given id is missing in the database ")

    def show(self):
        return {"ID": self.department_id, "NAME": self.department_name}

    def __str__(self):
        return f"ID: {self.department_id} NAME: {self.department_name}"

    def __repr__(self):
        return f"ID('{self.department_id}') NAME('{self.department_name}')"

    def save_in_json(self):
        if self.department_id is None:
            print("ID не может быть None")
        else:
            if not path.exists(f"dept_ID_{self.department_id}.json"):
                with open(f"dept_ID_{self.department_id}.json", "x", encoding="utf-8") as f:
                    f.write("{}")

            with open(f"dept_ID_{self.department_id}.json", "w") as f:
                data = self.show()
                data["Time of creation"] = f"{datetime.now()}"
                f.write(json.dumps(data, indent=4))





