"""Module containing language and color data."""

from typing import TypedDict


class ColorInfo(TypedDict):
    """Represents color information with an integer value and a hex code."""

    int_value: int
    hex_code: str


language_color_data: dict[str, ColorInfo] = {
    "Python": {"int_value": 264936, "hex_code": "#3776AB"},  # Python Blue
    "JavaScript": {"int_value": 16766720, "hex_code": "#F7DF1E"},  # JS Yellow
    "Java": {"int_value": 16711680, "hex_code": "#007396"},  # Java Blue
    "C#": {"int_value": 16711680, "hex_code": "#239120"},  # C# Green
    "C++": {"int_value": 14281728, "hex_code": "#00599C"},  # C++ Blue
    "C": {"int_value": 16777215, "hex_code": "#A8B9CC"},  # C Light Blue
    "PHP": {"int_value": 10181046, "hex_code": "#777BB4"},  # PHP Purple
    "TypeScript": {"int_value": 3447003, "hex_code": "#3178C6"},  # TS Blue
    "Swift": {"int_value": 16752640, "hex_code": "#F05138"},  # Swift Orange-Red
    "Go": {"int_value": 9147647, "hex_code": "#00ADD8"},  # Go Cyan
    "HTML": {"int_value": 16752640, "hex_code": "#E34F26"},  # HTML Orange-Red
    "CSS": {"int_value": 2649164, "hex_code": "#1572B6"},  # CSS Blue
    "React": {"int_value": 9147647, "hex_code": "#61DAFB"},  # React Cyan
    "Vue.js": {"int_value": 438040, "hex_code": "#42B883"},  # Vue Green
    "Angular": {"int_value": 13607510, "hex_code": "#DD0031"},  # Angular Red
    "Node.js": {"int_value": 3669118, "hex_code": "#339933"},  # Node Green
    "Ruby": {"int_value": 16711680, "hex_code": "#CC342D"},  # Ruby Red
    "Kotlin": {"int_value": 15065600, "hex_code": "#A97BFF"},  # Kotlin Purple
    "Rust": {"int_value": 16777215, "hex_code": "#000000"},  # Rust Black
    "Dart": {"int_value": 2179301, "hex_code": "#00B4AB"},  # Dart Teal
    "Flutter": {"int_value": 2179301, "hex_code": "#02569B"},  # Flutter Blue
    "SQL": {"int_value": 16777215, "hex_code": "#FFFFFF"},  # SQL White
    "PowerShell": {"int_value": 16777215, "hex_code": "#012456"},  # PowerShell Blue
}
