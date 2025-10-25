# Reference

- https://www.w3schools.com/python/python_mysql_getstarted.asp

# Project Structure

```
mysql_cli_app/
│
├── main.py                  # Entry point (menu / action handler)
├── sample/                  # Sample Simple Program
├── db/
│   ├── __init__.py
│   ├── connection.py        # Handles DB connection setup
│   └── operations.py        # CRUD and schema operations
│
├── scripts/
│   └── initial_table.sql    # Optional predefined SQL file(s)
│
├── config.py                # Configuration (host, port, user, password)
└── requirements.txt
```

# Database

- Assumed to be existing, may setup by docker by command below

```
docker run --name my-local-mysql -v my-local-mysql-data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=password -d -p 3306:3306 mysql:lts
```

# Environment Setup

## Mac

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Windows

```
python -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
```