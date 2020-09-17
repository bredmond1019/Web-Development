from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import sys
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://brandon:flask@localhost:5432/todoapp'

db = SQLAlchemy(app)

migrate = Migrate(app, db)

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column (db.Boolean, nullable=False, default = False)
    list_id = db.Column(db.Integer, db.ForeignKey('todolists.id'), nullable = False)

    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'



class TodoList(db.Model):
    __tablename__ = 'todolists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    todos = db.relationship('Todo', backref='list', lazy=True)

"""
NOTE: I initially made a migration after creating this class and we had an error. 
The error was that the values already in the list now contain null values
under the column "list_id". 
This goes against the NO NULL constraint that we set.

Therefore we should modify the migrations file before we upgrade. 
We can change: op.add_column('todos', sa.Column('list_id', sa.Integer(), nullable=True))
so nullable is True (for now) instead of False. Until we can update all the existing records.

Also, set nullable = True for now in the Todo class

Then we will run another migration once they are all updated or edit them in psql. 
In PSQL we can create a list called "Uncategorized" and add all of our todo items to that list

SQL Commands:
    insert into todolists (name) values ('Uncategorized');
    UPDATE todos SET list_id = 1 WHERE list_id IS NULL;


Now all of the todo items have a list_id. So we can set Todo's list_id of nullable=True
back to False
Save the file. Run 'flask db migrate' again. Then 'flask db upgrade'. 

Now we are good!
"""


@app.route('/todos/create', methods=['POST'])
def create():
    error = False
    body = {}
    try:
        description = request.get_json()['description']
        todo = Todo(description = description, completed = False)
        db.session.add(todo)
        db.session.commit()
        body['description'] = todo.description
        body['id'] = todo.id
        body['completed'] = todo.completed
    except:
        error = True
        db.session.rollback()
        print(sys.exec_info())
    finally:
        db.session.close()
    if not error:
        return jsonify(body)


@app.route('/todos/<todo_id>/set-completed', methods=['POST'])
def set_completed_todo(todo_id):
    try:
        completed = request.get_json()['completed']
        todo = Todo.query.get(todo_id)
        todo.completed = completed
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
    return redirect(url_for('index'))


@app.route('/todos/<todo_id>/delete', methods=['DELETE'])
def delete_todo(todo_id):
    try:
      Todo.query.filter_by(id=todo_id).delete()
      db.session.commit()
    except:
      db.session.rollback()
    finally:
      db.session.close()
    
    return jsonify({ 'success' : True})


@app.route('/lists/<list_id>')
def get_list_todos(list_id):
    return render_template('index.html', 
    lists = TodoList.query.all(),
    active_list = TodoList.query.get(list_id),
    todos=Todo.query.filter_by(list_id=list_id).order_by('id').all())


@app.route('/')
def index():
    return redirect(url_for('get_list_todos', list_id=1))