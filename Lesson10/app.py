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


@app.route('/order/get_data/', methods=['GET'])
def get_order():
    name = 'Заявки'
    order_list = Order.get_data()
    return render_template('index.html', name=name, params=order_list)


if __name__ == '__main__':
    app.run(debug=True)
