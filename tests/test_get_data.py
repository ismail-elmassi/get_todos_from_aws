""" This code is to test the two function get_all_todos and get_todo_by_id using pytest framework"""
from src.get_data import get_all_todos,get_todo_by_id

URL="https://0je8g9zvze.execute-api.eu-west-1.amazonaws.com/test/todos"

def test_get_todo_by_id():
    """This function to test the function get_todo_by_id """
    todos_by_id=get_todo_by_id(URL,1)
    assert todos_by_id=={"completed": False,"id": 1,"title": "delectus aut autem","userId": 1}

def test_get_all_todos():
    """This function to test the function get_all_todos """
    list_alltodos=get_all_todos(URL)
    assert len(list_alltodos)==100
