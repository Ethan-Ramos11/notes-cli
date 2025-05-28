import pytest
from unittest.mock import patch, MagicMock
from models import Note
import utils
import notes


@pytest.fixture
def sample_note():
    return Note(id=1, title="Test", content="Test content", tags=["tag1", "tag2"], created_at=None, updated_at=None)

# --- utils.py tests ---


def test_create_note(sample_note):
    with patch("utils.get_connection") as mock_conn:
        conn = MagicMock()
        cursor = MagicMock()
        mock_conn.return_value = (conn, cursor)
        utils.create_note(sample_note)
        assert cursor.execute.called
        assert conn.commit.called
        assert conn.close.called


def test_get_note(sample_note):
    with patch("utils.get_connection") as mock_conn:
        conn = MagicMock()
        cursor = MagicMock()
        cursor.fetchone.return_value = (
            1, "Test", "Test content", "tag1, tag2", None, None)
        mock_conn.return_value = (conn, cursor)
        note = utils.get_note(1)
        assert note.title == "Test"
        assert note.tags == ["tag1", "tag2"]


def test_update_note(sample_note):
    db_note = Note(id=1, title="Old", content="Test content", tags=[
                   "tag1", "tag2"], created_at=None, updated_at=None)
    with patch("utils.get_connection") as mock_conn, \
            patch("utils.get_note", return_value=db_note):
        conn = MagicMock()
        cursor = MagicMock()
        mock_conn.return_value = (conn, cursor)
        sample_note.title = "Updated"
        utils.update_note(sample_note)
        assert cursor.execute.called
        assert conn.commit.called
        assert conn.close.called


def test_delete_note():
    with patch("utils.get_connection") as mock_conn:
        conn = MagicMock()
        cursor = MagicMock()
        mock_conn.return_value = (conn, cursor)
        utils.delete_note(1)
        assert cursor.execute.called
        assert conn.commit.called
        assert conn.close.called


def test_list_notes():
    with patch("utils.get_connection") as mock_conn:
        conn = MagicMock()
        cursor = MagicMock()
        cursor.fetchall.return_value = [
            (1, "Test", "Test content", "tag1, tag2", None, None)
        ]
        mock_conn.return_value = (conn, cursor)
        notes_list = utils.list_notes()
        assert len(notes_list) == 1
        assert notes_list[0].title == "Test"

# --- notes.py tests (CLI) ---


def test_add_note(monkeypatch):
    with patch("notes.create_note") as mock_create:
        monkeypatch.setattr("questionary.text", lambda *a,
                            **k: MagicMock(ask=lambda: "Test"))
        monkeypatch.setattr("notes.get_tags", lambda: ["tag1"])
        notes.add_note()
        assert mock_create.called


def test_view_note(monkeypatch, sample_note):
    with patch("notes.list_notes", return_value=[sample_note]), \
            patch("notes.get_note", return_value=sample_note):
        monkeypatch.setattr("questionary.select", lambda *a, **
                            k: MagicMock(ask=lambda: f"{sample_note.id}: {sample_note.title}"))
        notes.view_note()


def test_update_note_cli(monkeypatch, sample_note):
    with patch("notes.list_notes", return_value=[sample_note]), \
            patch("notes.get_note", return_value=sample_note), \
            patch("notes.update_note") as mock_update:
        monkeypatch.setattr("questionary.select", lambda *a, **
                            k: MagicMock(ask=lambda: f"{sample_note.id}: {sample_note.title}"))
        monkeypatch.setattr("notes.get_updated_changes",
                            lambda: {"title": "New Title"})
        notes.update_note_cli()
        assert mock_update.called


def test_delete_note_cli(monkeypatch, sample_note):
    with patch("notes.list_notes", return_value=[sample_note]), \
            patch("notes.delete_note") as mock_delete:
        monkeypatch.setattr("questionary.select", lambda *a, **
                            k: MagicMock(ask=lambda: f"{sample_note.id}: {sample_note.title}"))
        notes.delete_note_cli()
        assert mock_delete.called


def test_list_notes_cli(monkeypatch, sample_note):
    with patch("notes.list_notes", return_value=[sample_note]):
        notes.list_notes_cli()
