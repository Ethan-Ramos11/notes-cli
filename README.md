# Note App

A simple command-line note-taking application with tagging, built using Python.

## Features

- Add, view, update, and delete notes
- Tag notes with multiple tags
- Pretty terminal UI using [rich](https://github.com/Textualize/rich)
- Interactive prompts using [questionary](https://github.com/tmbo/questionary)

## Requirements

- Python 3.8+
- [questionary](https://pypi.org/project/questionary/)
- [rich](https://pypi.org/project/rich/)

## Installation

1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd note
   ```
2. (Optional) Create and activate a virtual environment:
   ```sh
   python -m venv env
   source env/bin/activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run the main program:

```sh
python notes.py
```

Follow the interactive prompts to manage your notes.

## Development & Testing

- To run tests (if any):
  ```sh
  pytest
  ```

## Project Structure

- `notes.py` — Main CLI interface
- `models.py` — Data models
- `utils.py` — Database and CRUD utilities
- `database.py` — Database connection and setup

## License

MIT
