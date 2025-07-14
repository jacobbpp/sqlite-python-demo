import sqlite3

def create_connection(db_file):
    """
    Create a connection to the SQLite database specified by db_file.
    If the database does not exist, it will be created.
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file}")
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    """
    Create a table named 'users' if it doesn't already exist.
    """
    sql_create_table = """
    CREATE TABLE IF NOT EXISTS users (
        id integer PRIMARY KEY,
        name text NOT NULL
    ); """
    cursor = conn.cursor()
    cursor.execute(sql_create_table)
    conn.commit()
    print("Table created.")

def insert_user(conn, name):
    """
    Insert a new user into the users table.
    Returns the ID of the newly inserted user.
    """
    sql = ''' INSERT INTO users(name) VALUES(?) '''
    cursor = conn.cursor()
    cursor.execute(sql, (name,))
    conn.commit()
    return cursor.lastrowid

if __name__ == "__main__":
    db_name = "sample.db"
    conn = create_connection(db_name)
    if conn:
        create_table(conn)
        user_id = insert_user(conn, "Sean")
        print(f"Inserted user with id: {user_id}")
        conn.close()