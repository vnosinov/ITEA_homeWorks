"""
Продолжаем работу с таблицами из домашнего задания №5:

1. Создать тестовый набор данных по каждой из таблиц в модуле python (лучше всего использовать список списков или
список кортежей). Написать скрипт, который бы осуществлял подключение к существующей БД и последовательно запускал
сначала скрипты на создание таблиц (из прошлого ДЗ: departments, employees, orders), а затем последовательно загружал
туда данные.

2. По тестовым данным необходимо написать следующие запросы:
    - запрос для получения заявок в определенном статусе (можно выбрать любой) за конкретный день, созданных
    конкретным сотрудником;
    - запрос, возвращающий список сотрудников и департаментов, в которых они работают
    - запрос, позволяющий получить количество заявок в определенном статусе (можно выбрать любой) по дням;
"""
import psycopg2
from psycopg2 import sql
from psycopg2 import Error


def create_table(conn_name, table_name, sql_script):
    try:
        conn = conn_name
        cursor = conn.cursor()
        cursor.execute(sql_script)
        conn.commit()
        print(f'Таблица {table_name} создана ')
    except(Exception, Error) as error:
        print(error)


def insert_data_in_table(conn_name, sql_script, data_into):
    try:
        with conn_name, conn_name.cursor() as cursor:
            for data in data_into:
                cursor.execute(sql_script, (data,))
    except(Exception, Error) as error:
        print(error)


connect_db = psycopg2.connect(user="postgres", password="dbpass", host="127.0.0.1", port="5432",
                              database="order_service_db")

create_table_departments = sql.SQL("""
        CREATE TABLE IF NOT EXISTS departments (
        department_id SERIAL PRIMARY KEY,
        department_name TEXT NOT NULL,
        UNIQUE (department_name)
        );
""")

create_table_employees = sql.SQL("""
        CREATE TABLE IF NOT EXISTS employees (
        employee_id SERIAL PRIMARY KEY,
        fio TEXT NOT NULL,
        position TEXT NOT NULL,
        department_id INTEGER NOT NULL,
        FOREIGN KEY (department_id) REFERENCES departments (department_id)
        ON DELETE CASCADE);
""")

create_table_orders = sql.SQL("""
    CREATE TABLE IF NOT EXISTS orders (
    order_id SERIAL PRIMARY KEY NOT NULL,
    created_dt DATE NOT NULL,
    updated_dt DATE NOT NULL,
    type_order TEXT NOT NULL,
    description TEXT NOT NULL,
    status TEXT NOT NULL,
    serial_number INTEGER NOT NULL,
    creator_id INTEGER NOT NULL,
    FOREIGN KEY (creator_id) REFERENCES employees (employee_id)
);
""")

data_departments = ['Тех. поддержка',
                    'Бухгалтерия',
                    'Администрация',
                    'Продажа']

INSERT_QUERY_DEPARTMENTS = sql.SQL("""
    INSERT INTO departments (department_name) VALUES (%s)
""")


# create_table(connect_db, "departments", create_table_departments)
# create_table(connect_db, "employees", create_table_employees)
# create_table(connect_db, "orders", create_table_orders)
#
insert_data_in_table(connect_db, INSERT_QUERY_DEPARTMENTS, data_departments)


# try:
#     with connect_db:
#         with connect_db.cursor() as cursor:
#             for name in data_departments:
#                 print(name)
#                 cursor.execute(INSERT_QUERY_DEPARTMENTS, (name,))
# except(Exception, Error) as error:
#     print(error)
