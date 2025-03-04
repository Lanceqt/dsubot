"""Provides logging configuration for the Discord bot using Rich formatting."""

from __future__ import annotations

import json
import logging
import re

from rich.console import Console, ConsoleRenderable
from rich.logging import RichHandler
from rich.panel import Panel
from rich.syntax import Syntax
from rich.traceback import Traceback, install

install(show_locals=True)
console = Console()


class JSONRichHandler(RichHandler):
    """Custom Rich handler that formats JSON content."""

    def render(
        self,
        *,
        record: logging.LogRecord,
        traceback: Traceback | None,
        message_renderable: ConsoleRenderable,
    ) -> ConsoleRenderable:
        """Render log messages with special handling for JSON content."""
        try:
            if isinstance(record.msg, str) and "has connected to Gateway" in record.msg:
                # Extract the JSON part using a more precise regex
                match = re.search(
                    r"Gateway:\s*(\[.*?\].*?)\s*\(Session",
                    record.msg,
                    re.DOTALL,
                )
                if match:
                    json_content = match.group(1)
                    try:
                        # Parse and format the JSON
                        parsed_json = json.loads(json_content)
                        formatted_json = json.dumps(parsed_json, indent=2)

                        # Create syntax-highlighted panel
                        panel = Panel(
                            Syntax(
                                formatted_json,
                                "json",
                                theme="monokai",
                                word_wrap=False,
                                line_numbers=True,
                            ),
                            title="Gateway Information",
                            expand=False,
                            width=120,
                        )

                        # Reconstruct the message
                        record.msg = panel
                    except json.JSONDecodeError as e:
                        console.print(
                            f"[red]Failed to parse Gateway JSON: {e!s}\nContent: {json_content}"
                        )
                else:
                    console.print("[yellow]No JSON content found in log message.")

        except (json.JSONDecodeError, AttributeError, ValueError) as e:
            console.print(f"[red]Error formatting message: {e!s}")

        return super().render(
            record=record,
            traceback=traceback,
            message_renderable=message_renderable,
        )


def setup_bot_logging() -> None:
    """Configure logging for the bot with Rich formatting."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[
            JSONRichHandler(
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
