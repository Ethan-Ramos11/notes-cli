import sqlite3


def get_connection():
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    return conn, cursor


def validate_connection(conn):
    if conn is None:
        return False
    try:
        conn.execute("SELECT 1")
        return True
    except sqlite3.Error:
        return False


def create_tables(conn, cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notes (
      id INTEGER PRIMARY KEY AUTOINCREMENT, 
      title TEXT NOT NULL, 
      content TEXT,  
      tags TEXT, 
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
      updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
""")

    conn.commit()


def main():
    conn, cursor = get_connection()
    if validate_connection(conn):
        create_tables(conn, cursor)
    conn.close()


if __name__ == "__main__":
    main()
