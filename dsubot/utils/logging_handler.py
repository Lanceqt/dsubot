"""Provides logging configuration for the Discord bot using Rich formatting."""

from __future__ import annotations

import logging

from rich.console import Console
from rich.logging import RichHandler
from rich.traceback import install

install(show_locals=True)
console = Console()


def setup_bot_logging() -> None:
    """Configure logging for the bot with Rich formatting."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[
            RichHandler(
                rich_tracebacks=True,
                tracebacks_show_locals=True,
                show_time=True,
                console=console,
                markup=True,
            ),
        ],
    )

    logger = logging.getLogger("dsubot")
    logger.setLevel(logging.INFO)
