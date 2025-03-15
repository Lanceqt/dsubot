"""Module containing title branding data for software developer titles."""

from collections.abc import KeysView
from dataclasses import dataclass


@dataclass(frozen=True)
class TitleInfo:
    """Represents basic information for a developer title."""

    display_name: str


title_branding: dict[str, TitleInfo] = {
    "Fullstack Developer": TitleInfo(display_name="Fullstack Developer"),
    "Backend Developer": TitleInfo(display_name="Backend Developer"),
    "Frontend Developer": TitleInfo(display_name="Frontend Developer"),
    "Software Engineer": TitleInfo(display_name="Software Engineer"),
    "DevOps Engineer": TitleInfo(display_name="DevOps Engineer"),
    "Data Scientist": TitleInfo(display_name="Data Scientist"),
    "Mobile Developer": TitleInfo(display_name="Mobile Developer"),
    "QA Engineer": TitleInfo(display_name="QA Engineer"),
    "Cloud Engineer": TitleInfo(display_name="Cloud Engineer"),
    "Security Engineer": TitleInfo(display_name="Security Engineer"),
}

title_keys: KeysView[str] = title_branding.keys()
