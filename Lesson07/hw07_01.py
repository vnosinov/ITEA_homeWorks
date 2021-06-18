"""
Продолжаем работу с таблицами из домашнего задания №5 и классом Заяка из домашнего задания №2:

Расширить поведение класса Заявка. Теперь заявка должна иметь следующие методы, которые будут взаимодействовать
с БД (получать данные, изменять данные, удалять данные и т.д.):
создание новой заявки;
изменение статуса;
изменение описания;
изменение id создателя;
При изменении данных заявки в БД необходимо изменять поле updated_dt.

Аналогичные классы создать для департаментов и сотрудников. Во время выполнения задания постарайтесь максимально
использовать концепции ООП (инкапсуляцию, наследование, полиморфизм).
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
    UPDATE_ORDER_STATUS = sql.SQL("""SELECT * FROM orders WHERE 
    """)

    def __init__(self, type_order, description, status, serial_number, creator_id, order_id=None, updated_dt=None):
        self.created_dt = datetime.now()
        self.updated_dt = updated_dt
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

    def delete_data_by_id(self, *args, **kwargs):
        pass

    def get_order_id(self):
        return self.__order_id

    @staticmethod
    def set_value(value, order_id, column):
        query = f"""UPDATE orders SET {column} = %s, updated_dt = %s WHERE order_id = %s"""
        with connect, connect.cursor() as cursor:
            cursor.execute(query, [value, datetime.now(), order_id])

    @staticmethod
    def get_id(order_id):
        queue = f"""SELECT order_id FROM orders WHERE order_id = %s"""
        with connect, connect.cursor() as cursor:
            i = cursor.execute(queue, [order_id])
            print(i)

    @staticmethod
    def del_order_by_id(order_id):
        queue = f"""DELETE FROM orders WHERE order_id = %s"""

        with connect, connect.cursor() as cursor:
            if not order_id:
                raise DataRequiredException("Order_id param is required for deleting!")
            else:
                cursor.execute(queue, [order_id], )


# order1 = Order()
# order1.insert_new_data()
# Order.set_value('in_progress', 16, 'status')
# Order.del_order_by_id(1)
f1 = Order.get_id(1)
f2 = Order.get_id(8)

print(f1, f2)
