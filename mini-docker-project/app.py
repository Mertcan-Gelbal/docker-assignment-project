from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key')

# Database configuration
DB_CONFIG = {
    'host': os.environ.get('DB_HOST', 'localhost'),
    'database': os.environ.get('DB_NAME', 'taskdb'),
    'user': os.environ.get('DB_USER', 'postgres'),
    'password': os.environ.get('DB_PASSWORD', 'password'),
    'port': os.environ.get('DB_PORT', '5432')
}

def get_db_connection():
    """Database connection helper"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except psycopg2.Error as e:
        print(f"Database connection error: {e}")
        return None

def init_db():
    """Initialize database tables"""
    conn = get_db_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute('''
                CREATE TABLE IF NOT EXISTS tasks (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(200) NOT NULL,
                    description TEXT,
                    completed BOOLEAN DEFAULT FALSE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()
            cur.close()
            conn.close()
            print("Database initialized successfully")
        except psycopg2.Error as e:
            print(f"Database initialization error: {e}")

@app.route('/')
def index():
    """Home page - list all tasks"""
    conn = get_db_connection()
    if not conn:
        flash('Database connection failed', 'error')
        return render_template('index.html', tasks=[])
    
    try:
        cur = conn.cursor()
        cur.execute('SELECT id, title, description, completed, created_at FROM tasks ORDER BY created_at DESC')
        tasks = cur.fetchall()
        cur.close()
        conn.close()
        return render_template('index.html', tasks=tasks)
    except psycopg2.Error as e:
        flash(f'Database error: {e}', 'error')
        return render_template('index.html', tasks=[])

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    """Add new task"""
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        
        if not title:
            flash('Görev başlığı gereklidir!', 'error')
            return render_template('add_task.html')
        
        conn = get_db_connection()
        if not conn:
            flash('Database connection failed', 'error')
            return render_template('add_task.html')
        
        try:
            cur = conn.cursor()
            cur.execute(
                'INSERT INTO tasks (title, description) VALUES (%s, %s)',
                (title, description)
            )
            conn.commit()
            cur.close()
            conn.close()
            flash('Görev başarıyla eklendi!', 'success')
            return redirect(url_for('index'))
        except psycopg2.Error as e:
            flash(f'Database error: {e}', 'error')
            return render_template('add_task.html')
    
    return render_template('add_task.html')

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    """Mark task as completed"""
    conn = get_db_connection()
    if not conn:
        flash('Database connection failed', 'error')
        return redirect(url_for('index'))
    
    try:
        cur = conn.cursor()
        cur.execute('UPDATE tasks SET completed = TRUE WHERE id = %s', (task_id,))
        conn.commit()
        cur.close()
        conn.close()
        flash('Görev tamamlandı!', 'success')
    except psycopg2.Error as e:
        flash(f'Database error: {e}', 'error')
    
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    """Delete task"""
    conn = get_db_connection()
    if not conn:
        flash('Database connection failed', 'error')
        return redirect(url_for('index'))
    
    try:
        cur = conn.cursor()
        cur.execute('DELETE FROM tasks WHERE id = %s', (task_id,))
        conn.commit()
        cur.close()
        conn.close()
        flash('Görev silindi!', 'success')
    except psycopg2.Error as e:
        flash(f'Database error: {e}', 'error')
    
    return redirect(url_for('index'))

@app.route('/health')
def health_check():
    """Health check endpoint"""
    conn = get_db_connection()
    if conn:
        conn.close()
        return {'status': 'healthy', 'database': 'connected'}, 200
    else:
        return {'status': 'unhealthy', 'database': 'disconnected'}, 500

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True) 