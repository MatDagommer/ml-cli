"""Project initialization CLI."""

from typer import Typer
from cookiecutter.main import cookiecutter
from pathlib import Path

app = Typer()

PROJECT_TEMPLATE_DIR = Path(__file__).parent.parent / "templates" / "project"

@app.command()
def initialize():
    """Initialize project fdrom template."""
    cookiecutter(str(PROJECT_TEMPLATE_DIR.resolve()))
    