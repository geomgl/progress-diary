import sqlite3

connection = sqlite3.connect("data.db")


def createTable():
    with connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS entries(entry_content TEXT, entry_date TEXT);")


def add_entry(entry_content, entry_date):
    with connection:
        connection.execute("INSERT INTO entries VALUES (?, ?)", (entry_content, entry_date))


def get_entries():
    return entries
