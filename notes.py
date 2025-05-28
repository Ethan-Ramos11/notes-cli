import questionary
from rich.console import Console
from rich.table import Table
from utils import create_note, get_note, update_note, delete_note, list_notes

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


def view_note():
    pass


def update_note_cli():
    pass


def delete_note_cli():
    pass


def list_notes_cli():
    pass


def main():
    pass
