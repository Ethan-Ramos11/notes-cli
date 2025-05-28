import sqlite3
from database import get_connection
from models import Note
from typing import List, Optional


def create_note(note: Note):
    conn, cursor = get_connection()
    


def get_note(note_id: int) -> Optional[Note]:
    pass


def update_note(note: Note):
    pass


def delete_note(note_id: int):
    pass


def list_notes() -> List[Note]:
    pass
