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


@app.route('/dep_del/', methods=['POST'])
def dep_del():
    id = request.args.get('id')
    try:
        Department.delete_data_by_id(id)
    except Exception as e:
        print(e)
    return "Отдел удален"


@app.route('/dep_new/', methods=['POST'])
def dep_new():
    name = request.args.get('name')
    try:
        d = Department(name)
        d.insert_new_data()
    except Exception as e:
        print(e)
    return "Новый отдел добавлен"


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
