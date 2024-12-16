from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de tareas (en lugar de una base de datos)
tasks = []
students = [
    {"id": 1, "name": "Juan Pérez", "email": "juan@example.com"},
    {"id": 2, "name": "Ana Gómez", "email": "ana@example.com"},
    {"id": 3, "name": "Carlos López", "email": "carlos@example.com"}
]

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks, students=students)

# Ruta para agregar tareas
@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append({"task": task, "completed": False})
    return redirect(url_for('index'))

# Ruta para marcar tareas como completadas
@app.route('/complete_task/<int:index>')
def complete_task(index):
    tasks[index]['completed'] = True
    return redirect(url_for('index'))

# Ruta para eliminar tareas
@app.route('/delete_task/<int:index>')
def delete_task(index):
    tasks.pop(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

