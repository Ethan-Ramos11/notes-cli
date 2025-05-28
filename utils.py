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
    if note.tags:
        params = [note.title, note.content, ", ".join(
            note.tags),
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ]
    else:
        params = [note.title, note.content, "",
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
        tags_list = result[3].split(", ") if result[3] else []
        new_note = Note(result[0], result[1], result[2],
                        tags_list, result[4], result[5])
    conn.close()
    return new_note


def update_note(note: Note):
    conn, cursor = get_connection()
    database_note = get_note(note.id)
    fields, params = [], []
    change = False
    for key in ["title", "content", "tags"]:
        if getattr(note, key) != getattr(database_note, key):
            change = True
            fields.append(f"{key} = ?")
            params.append(getattr(note, key))
    if not change:
        return
    query = f"UPDATE notes SET {", ".join(fields)} WHERE id = ?"
    params.append(note.id)
    cursor.execute(query, params)
    conn.commit()
    conn.close()


def delete_note(note_id: int):
    conn, cursor = get_connection()
    cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    conn.close()


def list_notes() -> List[Note]:
    conn, cursor = get_connection()
    cursor.execute("SELECT * FROM notes")
    results = cursor.fetchall()
    notes = [Note(*row) for row in results]
    conn.close()
    return notes
