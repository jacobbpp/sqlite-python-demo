import os
import sqlite3

DB_FILE = "sample.db"

def test_database_file_exists():
    assert os.path.exists(DB_FILE)

def test_table_exists():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT name FROM sqlite_master
        WHERE type='table' AND name='users';
    """)
    table = cursor.fetchone()
    conn.close()
    assert table is not None

def test_user_inserted():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM users WHERE id = 1;")
    row = cursor.fetchone()
    conn.close()
    assert row is not None
    assert row[0] == "Sean"
