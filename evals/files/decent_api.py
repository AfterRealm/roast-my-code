"""Simple REST API for a todo app."""
from flask import Flask, request, jsonify
from datetime import datetime
import sqlite3
import os

app = Flask(__name__)
DB_PATH = os.environ.get('DB_PATH', 'todos.db')


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    return conn


def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            completed INTEGER DEFAULT 0,
            priority TEXT DEFAULT 'medium',
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


@app.route('/todos', methods=['GET'])
def list_todos():
    conn = get_db()
    status = request.args.get('status')
    if status == 'completed':
        rows = conn.execute("SELECT * FROM todos WHERE completed = 1 ORDER BY updated_at DESC").fetchall()
    elif status == 'active':
        rows = conn.execute("SELECT * FROM todos WHERE completed = 0 ORDER BY priority, created_at").fetchall()
    else:
        rows = conn.execute("SELECT * FROM todos ORDER BY completed, priority, created_at").fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])


@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    if not data or not data.get('title'):
        return jsonify({'error': 'Title required'}), 400

    now = datetime.utcnow().isoformat()
    conn = get_db()
    conn.execute(
        "INSERT INTO todos (title, description, priority, created_at, updated_at) VALUES (?, ?, ?, ?, ?)",
        (data['title'], data.get('description', ''), data.get('priority', 'medium'), now, now)
    )
    conn.commit()
    todo_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
    conn.close()
    return jsonify({'id': todo_id, 'created': True}), 201


@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    now = datetime.utcnow().isoformat()
    conn = get_db()

    existing = conn.execute("SELECT * FROM todos WHERE id = ?", (todo_id,)).fetchone()
    if not existing:
        conn.close()
        return jsonify({'error': 'Not found'}), 404

    title = data.get('title', existing['title'])
    description = data.get('description', existing['description'])
    completed = data.get('completed', existing['completed'])
    priority = data.get('priority', existing['priority'])

    conn.execute(
        "UPDATE todos SET title=?, description=?, completed=?, priority=?, updated_at=? WHERE id=?",
        (title, description, completed, priority, now, todo_id)
    )
    conn.commit()
    conn.close()
    return jsonify({'updated': True})


@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    conn = get_db()
    conn.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
    conn.commit()
    conn.close()
    return jsonify({'deleted': True})


@app.route('/todos/search', methods=['GET'])
def search_todos():
    q = request.args.get('q', '')
    conn = get_db()
    rows = conn.execute(
        "SELECT * FROM todos WHERE title LIKE ? OR description LIKE ?",
        (f'%{q}%', f'%{q}%')
    ).fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])


if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)
