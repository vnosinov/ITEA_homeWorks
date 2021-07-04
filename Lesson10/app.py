from flask import Flask, render_template, request
from hw10_01 import *

app = Flask(__name__)


@app.route('/')
def welcome():
    return 'Welcome to CRM "ORDERS"'


@app.route('/dep/get_data/', methods=['GET'])
def get_departments():
    name = 'Отделы'
    dep_list = Department.get_data()
    return render_template('index.html', name=name, params=dep_list)


@app.route('/dep_del/', methods=['DELETE'])
def dep_del():
    id_ = request.args.get('id')
    try:
        Department.delete_data_by_id(id_)
    except Exception as e:
        print(e)
    return f"Удален отдел c id {id_}"


@app.route('/dep_new/', methods=['POST'])
def dep_new():
    name = request.args.get('name')
    try:
        d = Department(name)
        d.insert_new_data()
    except Exception as e:
        print(e)
    return f"Добавлен новый отдел{name}"


@app.route('/dep_update/', methods=['POST'])
def dep_update():
    id_ = request.args.get('id')
    name = request.args.get('name')
    try:
        Department.update_dep(name, id_)
    except Exception as e:
        print(e)
    return f'Новое название отдела "{name}"'


@app.route('/dep_get_by_id/', methods=['GET'])
def dep_get_by_id():
    id_ = request.args.get('id')
    name = 'Отдел'
    dep_name = Department.get_data_by_id(id_)
    return render_template('index1.html', name=name, param=dep_name)


@app.route('/employees/get_data/', methods=['GET'])
def get_employees():
    name = 'Сотрудники'
    emp_list = Employees.get_data()
    return render_template('index.html', name=name, params=emp_list)


@app.route('/employees/get_by_id/', methods=['GET'])
def emp_get_by_id():
    name = 'Сотрудник'
    id_ = request.args.get('id')
    emp = Employees.get_by_id(id_)
    return render_template('index1.html', name=name, param=emp)


@app.route('/employees/del_by_id/', methods=['DELETE'])
def emp_del_by_id():
    id_ = request.args.get('id')
    try:
        Employees.delete_data_by_id(id_)
    except Exception as e:
        print(e)
    return f"Удален сотрудник c id {id_}"


@app.route('/emp_new/', methods=['POST'])
def emp_new():
    fio = request.args.get('fio')
    position = request.args.get('position')
    department_id = request.args.get('department_id')
    try:
        emp = Employees(fio, position, department_id)
        emp.insert_new_data()
    except Exception as e:
        print(e)
    return f"Добавлен сотрудник {fio}"


@app.route('/order/get_data/', methods=['GET'])
def get_order():
    name = 'Заявки'
    order_list = Order.get_data()
    return render_template('index.html', name=name, params=order_list)


@app.route('/order/new/', methods=['POST'])
def ord_new():

    type_order = request.args.get('type_order')
    description = request.args.get('description')
    status = request.args.get('status')
    serial_number = request.args.get('serial_number')
    creator_id = request.args.get('creator_id')
    try:
        order = Order(type_order, description, status, serial_number,creator_id)
        order.insert_new_data()
    except Exception as e:
        print(e)
    return f"Новая заявка"


@app.route('/order/del/', methods=['DELETE'])
def ord_del():
    id_ = request.args.get('id')
    try:
        Order.delete_data_by_id(id_)
    except Exception as e:
        print(e)
    return f"Удалена заявка id {id_}"


@app.route('/order/find/param/', methods=['GET'])
def ord_find_by_param():
    name = 'Заявка'
    _id = request.args.get('id')
    order = Order.get_order_by_id(_id)
    return render_template('index1.html', name=name, param=order)


if __name__ == '__main__':
    app.run(debug=True)
