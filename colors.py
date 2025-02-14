from typing import TypedDict


class ColorInfo(TypedDict):
    int_value: int
    hex_code: str


color_data: dict[str, ColorInfo] = {
    "Default": {"int_value": 0, "hex_code": "#000000"},
    "Aqua": {"int_value": 1752220, "hex_code": "#1ABC9C"},
    "DarkAqua": {"int_value": 1146986, "hex_code": "#11806A"},
    "Green": {"int_value": 5763719, "hex_code": "#57F287"},
    "DarkGreen": {"int_value": 2067276, "hex_code": "#1F8B4C"},
    "Blue": {"int_value": 3447003, "hex_code": "#3498DB"},
    "DarkBlue": {"int_value": 2123412, "hex_code": "#206694"},
    "Purple": {"int_value": 10181046, "hex_code": "#9B59B6"},
    "DarkPurple": {"int_value": 7419530, "hex_code": "#71368A"},
    "LuminousVividPink": {"int_value": 15277667, "hex_code": "#E91E63"},
    "DarkVividPink": {"int_value": 11342935, "hex_code": "#AD1457"},
    "Gold": {"int_value": 15844367, "hex_code": "#F1C40F"},
    "DarkGold": {"int_value": 12745742, "hex_code": "#C27C0E"},
    "Orange": {"int_value": 15105570, "hex_code": "#E67E22"},
    "DarkOrange": {"int_value": 11027200, "hex_code": "#A84300"},
    "Red": {"int_value": 15548997, "hex_code": "#ED4245"},
    "DarkRed": {"int_value": 10038562, "hex_code": "#992D22"},
    "Grey": {"int_value": 9807270, "hex_code": "#95A5A6"},
    "DarkGrey": {"int_value": 9936031, "hex_code": "#979C9F"},
    "DarkerGrey": {"int_value": 8359053, "hex_code": "#7F8C8D"},
    "LightGrey": {"int_value": 12370112, "hex_code": "#BCC0C0"},
    "Navy": {"int_value": 3426654, "hex_code": "#34495E"},
    "DarkNavy": {"int_value": 2899536, "hex_code": "#2C3E50"},
    "Yellow": {"int_value": 16776960, "hex_code": "#FFFF00"},
}
