"""Logging, traceback and terminal in general."""

import logging

from rich.console import Console
from rich.logging import RichHandler
from rich.traceback import install

install(show_locals=True)

console = Console()

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True, markup=True, console=console)],
    force=True,
)

# or __name__, in case the logging schema isn't destined for lambda functions.
log = logging.getLogger("Run-Lambda")
