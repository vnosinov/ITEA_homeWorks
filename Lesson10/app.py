from flask import Flask
from hw10_01 import *
app = Flask(__name__)


@app.route('/')
def welcome():
    return 'Welcome to CRM "ORDERS"'


@app.route('/dep/get_data/', methods=['GET'])
def get_departments_list():
    dep = Department.get_data()
    return f"{dep}"


if __name__ == '__main__':
    app.run(debug=True)
