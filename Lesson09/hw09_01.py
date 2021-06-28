"""Преобразовать все самописные классы-модели из прошлых ДЗ
(Заявки - Orders, Департаменты - Departments, Сотрудники - Employees)
в модели для использования в MongoDB. Предусмотреть необходимые связи, валидацию данных и ограничения.
Написать функции, которые будут:
создавать/изменять/удалять новую заявку/сотрудника/департамент

Подсказка: у вас должно получиться 3 модели и 9 функций =)"""

import mongoengine as me
from datetime import datetime

me.connect('orders')


class Departments(me.Document):
    department_id = me.IntField(required=True)
    department_name = me.StringField(required=True, min_length=4)

    def __str__(self):
        return f"Departments: {self.department_name}"

    def save(self, *args, **kwargs):
        return self.save(*args, **kwargs)

    def update(self, **kwargs):
        return self.update(**kwargs)

    def delete(self, **kwargs):
        super().delete(**kwargs)


class Employees(me.Document):
    employees_id = me.IntField(required=True)
    fio = me.StringField(required=True)
    position = me.StringField(required=True)
    departments = me.ReferenceField(Departments, reverse_delete_rule=me.CASCADE)

    def __str__(self):
        return f" Employees_id: {self.employees_id}  FIO: {self.fio}  Position: {self.position}"

    def save(self, *args, **kwargs):
        return self.save(*args, **kwargs)

    def update(self, **kwargs):
        return self.update(**kwargs)

    def delete(self, **kwargs):
        super().delete(**kwargs)


class Order(me.Document):
    created_dt = me.DateTimeField(required=True)
    updated_dt = me.DateTimeField(default=None)
    type_order = me.StringField(required=True, min_length=4)
    description = me.StringField(required=True, min_length=4)
    status = me.StringField(required=True)
    serial_number = me.IntField(required=True)
    creator_id = me.IntField(required=True)
    employees = me.ReferenceField(Employees, reverse_delete_rule=me.CASCADE)

    def __str__(self):
        return f"created_dt: {self.created_dt} "\
               f"updated_dt: {self.updated_dt} "\
               f"type_order: {self.type_order} "\
               f"description: {self.description} "\
               f"status: {self.status} "\
               f"serial_number: {self.serial_number} "\
               f"creator_id: {self.creator_id}"

    def save(self, *args, **kwargs):
        self.created_dt = datetime.now()
        return super().save(*args, **kwargs)

    def update(self, **kwargs):
        self.updated_dt = datetime.now()
        return super().update(**kwargs, updated_dt=self.updated_dt)

    def delete(self, **kwargs):
        super().delete(**kwargs)


departments_list = [
    {"department_id": 1,
     "department_name": "Тех. поддержка"
     },
    {"department_id": 2,
     "department_name": "Бухгалтерия"
     },
    {"department_id": 3,
     "department_name": "Администрация"
     },
    {"department_id": 4,
     "department_name": "Проектная"
     }
]

# for dept in departments_list:
#     my_id = dept['department_id']
#     dept_name = dept['department_name']
#     Departments(department_id=my_id, department_name=dept_name).save()
# d1 = Departments(department_id=1, department_name="fggg")
# d1.save()
#
obj = Departments.objects.get(id='60d38ce06d2f4e8f1a9bad03')
obj.delete()
# Departments.objects.all().delete()


# e1 = Employees(employees_id=1, fio='Иванов Иван Иванович', position='Инженер', departments=1)
# e1.my_save()

# o1 = Order(created_dt=datetime.now(), type_order='Support', description='Срочно',
#            status='new', serial_number='100001', creator_id='1')
# o1.my_save()
# print(o1)
