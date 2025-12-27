"""Initialization of the CLI module."""

from typer import Typer 

from .project import initialize

app = Typer()
app.command()(initialize)
