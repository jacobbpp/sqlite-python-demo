# SQLite Python Demo

This project demonstrates how to:

- Connect Python to an SQLite database
- Create a table and insert data
- Test that your database and table exist
- Automate tests with GitHub Actions

---

## Project Structure

```
sqlite-python-demo/
├── main.py
├── test_main.py
├── requirements.txt
└── .github/
    └── workflows/
        └── python-app.yml
```


---

## 1. Clone the Repository

Clone your repository:

```bash
git clone https://github.com/YOUR_USERNAME/sqlite-python-demo.git
cd sqlite-python-demo
```
---

## 2. Create requirements.txt

This file lists Python dependencies.

Save this text in requirements.txt:
```
pytest
```

## 3. Install Dependencies

* Install Python packages:
```
pip install -r requirements.txt
```

If you see:
```
Requirement already satisfied: pytest ...
```
you’re all set. Otherwise, pip will install pytest.

## 4. Run the Main Script

Run the Python script to create the SQLite database and insert data:

```bash
python main.py
```

Expected output:

```
Connected to sample.db
Table created.
Inserted user with id: 1
```

This creates a file called `sample.db` in your project folder.

---

## 5. Inspect the Database (Optional)

To check your database, you can use the `sqlite3` CLI tool:

```bash
sqlite3 sample.db
```

Inside the SQLite prompt, type:

```sql
.tables
SELECT * FROM users;
```

You should see:

```
users
1|Sean
```

Type `.exit` to quit SQLite.

---

## 6. Run the Tests

This project uses pytest to ensure everything works.

Run the tests:

```bash
python -m pytest
```

Expected output:

```
============================= test session starts =============================
collected 3 items

test_main.py ...                                                     [100%]

============================== 3 passed in 0.XXs ==============================
```

These tests check:

- that `sample.db` exists
- that the `users` table exists
- that Sean was inserted correctly

---

## 7. GitHub Actions

This project includes a GitHub Actions workflow to run tests automatically on each push or pull request.

**.github/workflows/python-app.yml**

```yaml
name: Python SQLite Demo

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: "3.10"

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run tests
      run: python -m pytest
```

---

## Project Structure

```
sqlite-python-demo/
├── main.py
├── test_main.py
├── requirements.txt
└── .github/
    └── workflows/
        └── python-app.yml
```

---

## requirements.txt

This file lists Python dependencies:

```
pytest
```

Install them with:

```bash
pip install -r requirements.txt
```

---

## How to Run Everything

Quick setup:

```bash
pip install -r requirements.txt
python main.py
python -m pytest
```

---

## Next Steps

- Add more fields to the `users` table
- Insert more data
- Write more tests for SELECT, UPDATE, and DELETE
- Try connecting SQLite from other languages (Java, C#, JavaScript)
