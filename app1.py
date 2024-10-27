from flask import Flask, jsonify,request

app = Flask(__name__)

# Task data
tasks = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, Cheese, Pizza, Fruit',
        'done': False
    },
    {
        'id': 2,    
        'title': 'Learn Python',
        'description': 'Need to find a good Python tutorial on the web',
        'done': False
    },

]
#get task
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task is not None:
        return jsonify({'task': task})
    else:
        return jsonify({'error': 'Task not found'}), 404
    
# Create a New Task- post task
@app.route('/addtasks', methods=['POST'])
def add_task():
    tasks=request.json
    tasks.append(add_task)
    return jsonify({"task": add_task})

    
if __name__ == '__main__':
    app.run(debug=True)
