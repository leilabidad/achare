import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "conversations.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            sender TEXT,
            message TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_message(user_id: str, sender: str, message: str):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO messages (user_id, sender, message) VALUES (?, ?, ?)",
              (user_id, sender, message))
    conn.commit()
    conn.close()
