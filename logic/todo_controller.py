import eel
from data.todo import Todo

todo_app = Todo()

@eel.expose
def add(task):
    todo_app.add(task)

@eel.expose
def delete(task):
    todo_app.delete(task)

@eel.expose
def get_tasks():
    return todo_app.get_tasks()

@eel.expose
def get_bet_list():
    return todo_app.get_bet_list()

@eel.expose
def float_henkan(budget):
    gousei_odds = todo_app.float_henkan(budget)
    print(gousei_odds)
    return gousei_odds

@eel.expose
def reset():
    return todo_app.reset()