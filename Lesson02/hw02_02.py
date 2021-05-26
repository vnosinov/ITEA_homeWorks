"""Давайте представим, что мы занимаемся проектированием CRM для сервисного центра по обслуживанию и ремонту техники.
Реализуйте класс Заявка. Каждая заявка должна иметь следующие поля:  -уникальный идентификатор (присваивается в момент)
создания заявки автоматически, дата и время создания заявки (автоматически), имя пользователя, серийный номер
оборудования, статус (активная заявка или закрытая например, статусов может быть больше). Id заявки сделать приватным
полем.
поля:
    - уникальный идентификатор (присваивается в момент)
    - дата и время создания заявки
    - имя пользователя
    - серийный номер оборудования
    - статус (активная заявка или закрытая например, статусов может быть больше)
У заявки должны быть следующие методы:
- метод, возвращающий, сколько заявка находится в активном статусе (если она в нём)
- метод, изменяющий статус заявки
- метод, возвращающий id заявки"""

import uuid
from datetime import datetime
import time


class CRMRequest:

    def __init__(self, user_name, serial_number, status='None'):
        self.change_time_status = datetime.now()
        self.creation_time = datetime.now()
        self.status = status
        self.__id = uuid.uuid4()
        self.user_name = user_name
        self.serial_number = serial_number

    def get_id(self):
        return self.__id

    def get_creations(self):
        return self.creation_time

    def set_status(self, new_status):
        self.status = new_status
        if self.status == 'Active':
            # time.sleep(5)
            self.change_time_status = datetime.now()

    def get_time_in_active(self):
        if self.status == 'Active':
            time_in_active = datetime.now() - self.change_time_status
            return time_in_active
        else:
            print('Заявка не в работе')


r1 = CRMRequest("loh1", "df123fr4")

print(f'Id заявки : {r1.get_id()}\nВремя создания: {r1.get_creations()}\nСтатус {r1.status}')

r1.set_status('Active')

print(f'Id заявки : {r1.get_id()}\nСтатус {r1.status}\nВремя в активном статусе: {r1.get_time_in_active()}')
