import os
import main

def test_database_created():
    db_file = "test.db"
    if os.path.exists(db_file):
        os.remove(db_file)

    conn = main.create_connection(db_file)
    assert conn is not None
    conn.close()
    assert os.path.exists(db_file)

def test_table_creation_and_insert():
    db_file = "test2.db"
    if os.path.exists(db_file):
        os.remove(db_file)

    conn = main.create_connection(db_file)
    main.create_table(conn)
    user_id = main.insert_user(conn, "Bob")

    cursor = conn.cursor()
    cursor.execute("SELECT name FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()

    assert row is not None
    assert row[0] == "Bob"

    conn.close()
