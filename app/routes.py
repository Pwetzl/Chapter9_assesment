from app import app
from flask import render_template, flash, redirect
from app.forms import RegisterForm,AddProductForm



@app.route('/')
@app.route('/index')
def index():
    """shop URL"""
    return render_template("index.html" , title='index page')


@app.route('/add-product', methods = ['GET', 'POST'])
def add_product():
    """add product URL"""
    form = AddProductForm()
    return render_template('add_product.html', title='Add product page', form=form)


@app.route('/register', methods = ['GET', 'POST'])
def register():
    """register URL"""
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'you are requesting to register{form.username.data}')
    return render_template('register.html', title='Register page', form=form)

