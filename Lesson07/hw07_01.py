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
from datetime import date
from envparse import Env
from abc import ABC, abstractmethod

env = Env()

DB_URL = env.str("MY_DB_URL", default="postgres://postgres:dbpass@127.0.0.1:5432/order_service_db")
print(DB_URL)

connect = psycopg2.connect(DB_URL)


class BaseModel(ABC):
    @abstractmethod
    def create_new_data(self, *args, **kwargs):
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
    def __init__(self, created_dt, updated_dt, type_order, description, status, serial_number, creator_id):
      pass
