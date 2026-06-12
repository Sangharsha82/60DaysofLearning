from flask import Flask, render_template, request, jsonify
import sqlite3
import os

app = Flask(__name__)
DB_PATH = "sqlite_example.db"

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                quantity INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/items", methods=["GET"])
def get_items():
    with get_db() as conn:
        items = conn.execute("SELECT * FROM items ORDER BY id DESC").fetchall()
        return jsonify([dict(i) for i in items])

@app.route("/api/items", methods=["POST"])
def create_item():
    data = request.json
    with get_db() as conn:
        cursor = conn.execute(
            "INSERT INTO items (name, description, quantity) VALUES (?, ?, ?)",
            (data["name"], data.get("description", ""), data.get("quantity", 0))
        )
        conn.commit()
        item = conn.execute("SELECT * FROM items WHERE id = ?", (cursor.lastrowid,)).fetchone()
        return jsonify(dict(item)), 201

@app.route("/api/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    data = request.json
    with get_db() as conn:
        conn.execute(
            "UPDATE items SET name=?, description=?, quantity=? WHERE id=?",
            (data["name"], data.get("description", ""), data.get("quantity", 0), item_id)
        )
        conn.commit()
        item = conn.execute("SELECT * FROM items WHERE id = ?", (item_id,)).fetchone()
        if not item:
            return jsonify({"error": "Not found"}), 404
        return jsonify(dict(item))

@app.route("/api/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    with get_db() as conn:
        conn.execute("DELETE FROM items WHERE id = ?", (item_id,))
        conn.commit()
        return jsonify({"success": True})

if __name__ == "__main__":
    init_db()
    app.run(debug=True)