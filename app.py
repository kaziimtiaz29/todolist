#import re
from flask import Flask, config,url_for,redirect,render_template
from flask.globals import request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
app = Flask(__name__)



#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
#app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://mysql_user:mysql_password>@mysql_instance_ip>:3306/<mysql_db>'
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:1234@35.189.79.75:3306/TESTDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY']= '1234'
db = SQLAlchemy(app)


class todos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Task = db.Column(db.String(30), nullable=False)
    Completed = db.Column(db.Boolean,nullable=True, default= False)
    #country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=False)

class TodoForm(FlaskForm):
    task = StringField("Task")
    submit = SubmitField("Add Todo")

@app.route('/')
def index():
    _todos= todos.query.all()
    #todos_1= ""
    #for c in all_todos:
     #   todos_1+="<br>"+str(c.id)+" " +c.Task+" "+str(c.Completed)
    return  render_template("index.html", all_todos=_todos)
    
 
@app.route('/add',methods=['GET','POST'])
def to_do1():
    form = TodoForm()
    if form.validate_on_submit():
        Task_3 = todos(Task = form.task.data)
        db.session.add(Task_3)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("add.html", form=form)

@app.route('/complete/<int:n>')
def is_complete(n):
    task_4= todos.query.get(n)
    task_4.Completed = True
    db.session.commit()
    return redirect(url_for("index"))


@app.route('/incomplete/<int:n>')
def is_incomplete(n):
    task_5= todos.query.get(n)
    task_5.Completed = False
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/delete/<int:n>')
def is_delete(n):
    task_6 = todos.query.get(n)
    db.session.delete(task_6)
    db.session.commit()
    #return 'deleted'
    return  redirect (url_for("index"))
@app.route('/update/<int:n>',methods = ['GET','POST'])
def update(n):
    form = TodoForm()
    todo_update= todos.query.get(n)
    if form.validate_on_submit():
        todo_update.Task = form.task.data
        db.session.commit()
        return redirect(url_for("index"))
    if request.method == "GET":
        form.task.data= todo_update.Task
    return render_template("update.html",form=form)




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')