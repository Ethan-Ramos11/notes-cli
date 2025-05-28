import sqlite3
from database import get_connection


def create_note(title, content="", tags=[]):
    conn, cursor = get_connection()
    