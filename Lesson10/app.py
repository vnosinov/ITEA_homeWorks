from flask import Flask, render_template
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
