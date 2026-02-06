from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, current_user, logout_user, login_required
from flask_limiter.util import get_remote_address
from models import db, User, Todo
from forms import RegistrationForm, LoginForm, TodoForm
from utils import sanitize_input

def init_routes(app, limiter):

    @app.errorhandler(404)
    def not_found(error):
        return render_template('error.html', msg="Page not found"), 404

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if current_user.is_authenticated:
            return redirect(url_for('home'))
        form = RegistrationForm()
        if form.validate_on_submit():
            existing_user = User.query.filter_by(email=form.email.data).first()
            if existing_user:
                flash('Email already registered.', 'danger')
                return redirect(url_for('register'))
            user = User(username=form.username.data, email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Account created successfully! You can now log in.', 'success')
            return redirect(url_for('login'))
        return render_template('register.html', form=form)

    @app.route('/login', methods=['GET', 'POST'])
    @limiter.limit("5 per minute", key_func=get_remote_address)
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('home'))
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and user.check_password(form.password.data):
                login_user(user, remember=True)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('home'))
            else:
                flash('Invalid email or password.', 'danger')
        return render_template('login.html', form=form)

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        flash('You have been logged out.', 'info')
        return redirect(url_for('login'))

    @app.route('/', methods=['GET', 'POST'])
    @login_required
    def home():
        form = TodoForm()
        if form.validate_on_submit():
            sanitized_content = sanitize_input(form.content.data)
            if not sanitized_content.strip():
                flash('Todo content cannot be empty.', 'warning')
                return redirect(url_for('home'))
            todo = Todo(content=sanitized_content, user_id=current_user.id)
            db.session.add(todo)
            db.session.commit()
            flash('Todo added successfully!', 'success')
            return redirect(url_for('home'))
        
        if current_user.role == 'admin':
            todos = Todo.query.order_by(Todo.created_at.desc()).all()
        else:
            todos = Todo.query.filter_by(user_id=current_user.id).order_by(Todo.created_at.desc()).all()
        
        return render_template('home.html', form=form, todos=todos)

    @app.route('/admin')
    @login_required
    def admin():
        if current_user.role != 'admin':
            flash('Access denied: Admins only.', 'danger')
            return redirect(url_for('home'))
        users = User.query.all()
        return render_template('admin.html', users=users)