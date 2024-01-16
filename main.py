from flask import Flask, render_template
from functions import *

main = Flask(__name__)


@main.route('/')
def index():
    return render_template('home.html')


@main.route('/about/')
def about():
    # code
    return render_template('about.html', data='Hello!')


@main.route('/contacts/')
def contact():
    return render_template('contacts.html')


@main.route('/catalog/')
def catalog():
    return render_template('catalog.html', data=get_products_data())


if __name__ == "__main__":
    main.run(debug=True)
