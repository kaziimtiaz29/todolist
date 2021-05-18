from app import db, todos
db.drop_all()
db.create_all() 

Task_3 = todos(Task = 'new todo', Completed = True)
#completed_task1 = todos(name= "True")
db.session.add(Task_3)
db.session.commit()
