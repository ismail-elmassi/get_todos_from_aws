
""" This code is a flask app to get all todos and todo by id from aws """

from flask import Flask, jsonify
from get_data import get_all_todos,get_todo_by_id

app = Flask(__name__)

URL="https://0je8g9zvze.execute-api.eu-west-1.amazonaws.com/test/todos"


@app.route('/api/v1/todos',methods=['GET'])
def get_alltodos():
    """ This function return all todos in json format"""
    alltodos_list = get_all_todos(URL)
    return jsonify(alltodos_list)

@app.route('/api/v1/todos/<todo_id>',methods=['GET'])
def get_todobyid(todo_id):
    """ This function return todos by id in json format"""
    todo_by_id= get_todo_by_id(URL,todo_id)
    return jsonify(todo_by_id)

def main():
    """ This is the main function """
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    main()
