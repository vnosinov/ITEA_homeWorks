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


@app.route('/employees/get_data', method=['GET'])
def get_employees():
    name = 'Сотрудники'


if __name__ == '__main__':
    app.run(debug=True)
