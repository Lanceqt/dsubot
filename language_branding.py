"""Module containing language and color data."""

from collections.abc import KeysView
from dataclasses import dataclass


@dataclass(frozen=True)
class ColorInfo:
    """Represents color information with an integer value and a hex code."""

    int_value: int
    hex_code: str


language_branding: dict[str, ColorInfo] = {
    "Python": ColorInfo(int_value=264936, hex_code="#3776AB"),  # Python Blue
    "JavaScript": ColorInfo(int_value=16766720, hex_code="#F7DF1E"),  # JS Yellow
    "Java": ColorInfo(int_value=16711680, hex_code="#007396"),  # Java Blue
    "C#": ColorInfo(int_value=16711680, hex_code="#239120"),  # C# Green
    "C++": ColorInfo(int_value=14281728, hex_code="#00599C"),  # C++ Blue
    "C": ColorInfo(int_value=16777215, hex_code="#A8B9CC"),  # C Light Blue
    "PHP": ColorInfo(int_value=10181046, hex_code="#777BB4"),  # PHP Purple
    "Go": ColorInfo(int_value=9147647, hex_code="#00ADD8"),  # Go Cyan
    "Swift": ColorInfo(int_value=16752640, hex_code="#F05138"),  # Swift Orange-Red
    "Kotlin": ColorInfo(int_value=15065600, hex_code="#A97BFF"),  # Kotlin Purple
    "Ruby": ColorInfo(int_value=16711680, hex_code="#CC342D"),  # Ruby Red
    "R": ColorInfo(int_value=4249477, hex_code="#276DC3"),  # R Blue
    "Objective-C": ColorInfo(
        int_value=16777215, hex_code="#F09433"
    ),  # Objective-C Orange
    "TypeScript": ColorInfo(int_value=3447003, hex_code="#3178C6"),  # TS Blue
    "Scala": ColorInfo(int_value=13421772, hex_code="#DC322F"),  # Scala Red
    "Perl": ColorInfo(int_value=16777215, hex_code="#002F5F"),  # Perl Blue
    "Lua": ColorInfo(int_value=15066597, hex_code="#2C2D72"),  # Lua Blue
    "Haskell": ColorInfo(int_value=16711680, hex_code="#5D4F85"),  # Haskell Purple
    "Rust": ColorInfo(int_value=16777215, hex_code="#000000"),  # Rust Black
    "Delphi": ColorInfo(int_value=16760576, hex_code="#E64646"),  # Delphi Red
    "OCaml": ColorInfo(
        int_value=16764057, hex_code="#E37F1E"
    ),  # OCaml Orange (Slightly different from Pascal)
    "F#": ColorInfo(int_value=2649164, hex_code="#3700FF"),  # F# Purple-Blue
    "Elixir": ColorInfo(int_value=16711680, hex_code="#4B275F"),  # Elixir Purple
}

language_keys: KeysView[str] = language_branding.keys()
