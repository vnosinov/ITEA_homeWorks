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


class Orders(BaseModel):
    INSERT_ORDERS = sql.SQL("""INSERT INTO orders (created_dt, updated_dt, order_type, description, 
                status, serial_no, creator_id) 
                VALUES (%s, %s, %s, %s, %s, %s) 
                RETURNING order_id
                """)

    def __init__(self, type_order, description, status, serial_number, creator_id, order_id=None):
        self.created_dt = datetime.now().strftime('%Y-%m-%d')
        self.type_order = type_order
        self.description = description
        self.status = status
        self.serial_number = serial_number
        self.creator_id = creator_id
        self.order_id = order_id

    def insert_new_data(self):
        with connect, connect.cursor() as cursor:
            cursor.execute(self.__class__.INSERT_ORDERS,
                           (datetime.now(), datetime.now(), self.type_order, self.description,
                            self.status, self.serial_number, self.creator_id))
            order_id = cursor.fetchone()[0]
            self.order_id = order_id
        return {'order_id': order_id}

    def delete_data_by_id(self, *args, **kwargs):
        pass


order1 = Orders('Support', 'Срочно', 'New', 10007, 5)
order1.insert_new_data()
