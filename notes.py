import questionary
from rich.console import Console
from rich.table import Table
from utils import create_note, get_note, update_note, delete_note, list_notes
from models import Note
from datetime import datetime
console = Console()


def main_menu():
    return questionary.select(
        "What would you like to do?",
        choices=[
            "add a note",
            "view a note",
            "update a note",
            "delete a note",
            "update all notes"
        ]
    ).ask()


def get_tags():
    tags = []
    while True:
        tag = questionary.text(
            "Enter a tag (or type 'con' to continue):").ask()
        if tag == "con":
            break
        else:
            tags.append(tag)
    return tags


def add_note():
    title = questionary.text("What is the title of your note?").ask()
    content = questionary.text("What is the content of your note").ask()
    tags = get_tags()
    new_note = Note(title, content, tags)
    create_note(new_note)
    console.print(f"[green]Note '{title}' added successfully![/green]")


def view_note():
    notes = list_notes()
    if not notes:
        console.print("[yellow]No notes to view.[/yellow]")
        return
    choices = [f"{note.id}: {note.title}" for note in notes]
    selected = questionary.select(
        "What note would you like to view?", choices=choices
    ).ask()
    if not selected:
        return
    note_id = int(selected.split(":", 1)[0])
    note = get_note(note_id)
    table = Table(title="Your Notes", show_lines=True)
    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Title", style="magenta")
    table.add_column("Content", style="magenta")
    table.add_column("Tags", style="green")
    tags = ", ".join(note.tags) if hasattr(note, 'tags') else ""
    table.add_row(str(getattr(note, 'id', '')), note.title, note.content, tags)
    console.print(table)


def get_updated_changes():
    change_title = questionary.confirm(
        "Do you want to update the title?").ask()
    changes = {}
    if change_title:
        new_title = questionary.text("What is the new title?").ask().strip()
        changes["title"] = new_title

    change_content = questionary.confirm(
        "Do you want to update the content?").ask()

    if change_content:
        new_content = questionary.text(
            "What is the new content?").ask().strip()
        changes["content"] = new_content

    change_tags = questionary.confirm("Do you want to update the tags?").ask()

    if change_tags:
        tags = get_tags()
        changes["tags"] = tags

    return changes


def update_note_cli():
    notes = list_notes()
    if not notes:
        console.print("[yellow]No notes to delete.[/yellow]")
        return
    choices = [f"{note.id}: {note.title}" for note in notes]
    selected = questionary.select(
        "What note would you like to delete?", choices=choices).ask()
    if not selected:
        return
    note_id = int(selected.split(":", 1)[0])

    note = get_note(note_id)
    changes = get_updated_changes()

    if "title" in changes:
        note.title = changes["title"]
    if "content" in changes:
        note.content = changes["content"]
    if "tags" in changes:
        note.tags = changes["tags"]

    note.updated_at(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    update_note(note)


def delete_note_cli():
    notes = list_notes()
    if not notes:
        console.print("[yellow]No notes to delete.[/yellow]")
        return
    choices = [f"{note.id}: {note.title}" for note in notes]
    selected = questionary.select(
        "What note would you like to delete?", choices=choices).ask()
    if not selected:
        return
    note_id = int(selected.split(":", 1)[0])
    delete_note(note_id)
    console.print(f"[red]Note {note_id} deleted.[/red]")


def list_notes_cli():
    notes = list_notes()
    if not notes:
        console.print("[yellow]No notes found.[/yellow]")
        return
    table = Table(title="Your Notes", show_lines=True)
    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Title", style="magenta")
    table.add_column("Tags", style="green")
    for note in notes:
        tags = ", ".join(note.tags) if hasattr(note, 'tags') else ""
        table.add_row(str(getattr(note, 'id', '')), note.title, tags)
    console.print(table)
    return notes


def main():
    pass
