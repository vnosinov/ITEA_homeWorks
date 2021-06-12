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


def insert_in_department(conn_name, sql_script, data_into):
    try:
        with conn_name, conn_name.cursor() as cursor:
            for data in data_into:
                cursor.execute(sql_script, (data,))
    except(Exception, Error) as error:
        print(error)


def insert_in_tables(conn_name, sql_script, data_into):
    try:
        with conn_name, conn_name.cursor() as cursor:
            for data in data_into:
                cursor.execute(sql_script, data)
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

data_departments = ["Тех. поддержка",  # 1
                    "Бухгалтерия",     # 2
                    "Администрация",   # 3
                    "Продажа"]         # 4


data_employees = [
    ("Иванов Иван Иванович", "Инженер", 1),
    ("Сидоров Петр Иванович", "Админ", 1),
    ("Кирилова Мария Ивановка", "Бухгалтер", 2),
    ("Хараман Тая Федоровна", "Главный бухгалтер", 2),
    ("Крикунов Давид Янович", "Директор", 3),
    ("Красоткина Яна Ивановна", "Секретарь", 3),
    ("Янов Ян Янович", "Менеджер", 4),
    ("Зайцев Дмитрий Юрьевич", "Продавец", 4),
    ("Климова Ирина Петровна", "Кассир", 4),
    ("Крылов Владимир Андреевич", "Старший продавец", 4)]

data_orders = [
    ('2021-01-01', '2021-01-01', "support", "fsdf", "new", 10001, 3),
    ('2021-01-02', '2021-01-02', "support", "fsdапапf", "new", 10002, 3),
    ('2021-01-01', '2021-01-03', "sale", "fsпавпdf", "in progress", 10003, 4),
    ('2021-03-02', '2021-03-04', "support", "afadffsdf", "done", 10004, 5),
    ('2021-05-01', '2021-05-10', "sale", "ewrrfsdf", "done", 10005, 5),
    ('2021-06-01', '2021-06-07', "business", "frffsdf", "done", 10006, 10)]


INSERT_QUERY_DEPARTMENTS = sql.SQL("""
    INSERT INTO departments (department_name) VALUES (%s)
""")

INSERT_QUERY_EMPLOYEES = sql.SQL("""
    INSERT INTO employees (fio, position, department_id) VALUES (%s, %s, %s)
""")

INSERT_QUERY_ORDERS = sql.SQL("""
    INSERT INTO orders (created_dt, updated_dt, type_order, description, status,
                        serial_number, creator_id) VALUES (%s, %s, %s, %s, %s, %s, %s)
""")

# create_table(connect_db, "departments", create_table_departments)
# create_table(connect_db, "employees", create_table_employees)
# create_table(connect_db, "orders", create_table_orders)
# #
# insert_data_in_table(connect_db, INSERT_QUERY_DEPARTMENTS, data_departments)
# insert_in_tables(connect_db, INSERT_QUERY_EMPLOYEES, data_employees)
insert_in_tables(connect_db, INSERT_QUERY_ORDERS, data_orders)

