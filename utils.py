import sqlite3
from database import get_connection
from models import Note
from typing import List, Optional
from datetime import datetime


def create_note(note: Note):
    conn, cursor = get_connection()
    query = """
INSERT INTO notes (title, content, tags, created_at, updated_at)
VALUES (?, ?, ?, ?, ?)
"""
    params = [note.title, note.content, ", ".join(
        note.tags),
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ]
    cursor.execute(query, params)
    conn.commit()
    conn.close()


def get_note(note_id: int) -> Optional[Note]:
    conn, cursor = get_connection()
    query = """
SELECT * FROM notes WHERE
id = ?
"""

    cursor.execute(query, (note_id,))
    result = cursor.fetchone()
    new_note = None
    if result:
        new_note = Note(result[0], result[1], result[2],
                        result[3], result[4], result[5])
    conn.close()
    return new_note


def update_note(note: Note):
    pass


def delete_note(note_id: int):
    pass


def list_notes() -> List[Note]:
    pass
