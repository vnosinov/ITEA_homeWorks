"""1. Сделать шаблоны для отображения сотрудников, заявок и департаментов и прикрутить их к соответствующим методам.
Используйте 1 базовый шаблон, от которого унаследуете все остальные.

2.
- Написать ручку на flask, которая будет принимать в теле запроса список id пользователей.
- Дальше по каждому id нужно ОТДЕЛЬНО сделать запрос в БД на получение информации о пользователе.
- Реализовать механизм сбора данных о пользователе через процессы или потоки.
- Получив информацию по каждому пользователю вернуть её в составе json-объекта в ответе.
"""

import json
from flask import Flask, request
import psycopg2
from psycopg2 import sql
from multiprocessing import Process

conn = psycopg2.connect('postgres://postgres:dbpass@localhost:5432/order_service_db')


class Employees:
    SEARCH_EMPLOYEES_ID = sql.SQL('''SELECT fio, position FROM employees WHERE employee_id = %s''')

    def __init__(self, fio, position, department_id, employee_id=None):
        self.fio = fio
        self.position = position
        self.department_id = department_id
        self.employee_id = employee_id


app = Flask('__name__')


@app.route('/get_emp', methods=['GET'])
def get_emp():
    p = Process(target=get_emp)
    p.start()
    list_emp = {}
    list_id = json.loads(request.data)
    print(list_id)
    with conn, conn.cursor() as cursor:
        for key in list_id:
            cursor.execute(Employees.SEARCH_EMPLOYEES_ID, (list_id[key],))
            res = cursor.fetchall()
            list_emp[list_id[key]] = list(res[0])
        return json.dumps(list_emp)
    p.join()


if __name__ == "__main__":
    app.run(debug=True)
