## main.py — What It Does

Let’s break down how this file works so there’s no mystery.

---

### 1. Import sqlite3

First, we import Python’s built-in SQLite library:

```python
import sqlite3
```

Nothing extra to install. SQLite comes with Python.

---

### 2. Create a Connection

This function opens (or creates) a database file:

```python
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file}")
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn
```

- If the file doesn’t exist, SQLite makes it for you.
- If there’s an error, it prints the error and returns `None`.

---

### 3. Create a Table

This function creates a table called `users` if it doesn’t exist yet:

```python
def create_table(conn):
    sql_create_table = """
    CREATE TABLE IF NOT EXISTS users (
        id integer PRIMARY KEY,
        name text NOT NULL
    ); """
    cursor = conn.cursor()
    cursor.execute(sql_create_table)
    conn.commit()
    print("Table created.")
```

- We define an SQL command to make a `users` table.
- `id` is an integer primary key.
- `name` is a text column that can’t be null.
- We execute the SQL and commit the changes.

---

### 4. Insert Data

Here’s a function to insert a new user into the table:

```python
def insert_user(conn, name):
    sql = ''' INSERT INTO users(name) VALUES(?) '''
    cursor = conn.cursor()
    cursor.execute(sql, (name,))
    conn.commit()
    return cursor.lastrowid
```

- The question mark `?` is a placeholder to prevent SQL injection.
- We pass a tuple `(name,)` as the parameter.
- The function returns the newly inserted row’s ID.

---

### 5. Run Everything

At the bottom of the file:

```python
if __name__ == "__main__":
    db_name = "sample.db"
    conn = create_connection(db_name)
    if conn:
        create_table(conn)
        user_id = insert_user(conn, "Sean")
        print(f"Inserted user with id: {user_id}")
        conn.close()
```

- If you run this file directly, it:
  - connects to `sample.db`
  - creates the `users` table if it doesn’t exist
  - inserts a user called **Sean**
  - prints out the new user’s ID
  - closes the connection

After running, you’ll have a file called `sample.db` in your folder with a table and some data inside.

---

## Summary

So, in plain terms:

- [x] Connects Python to an SQLite database  
- [x] Creates a table called `users`  
- [x] Inserts Sean into it  
- [x] Prints what it’s doing

Nothing fancy. No dependencies beyond Python itself. Perfect for getting started.