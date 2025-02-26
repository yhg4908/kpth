# koreanpython/translator.py

import re
from .keywords import KOREAN_TO_PY_KEYWORDS

def translate_code(code: str) -> str:
    pattern_map = []
    for ko, py in KOREAN_TO_PY_KEYWORDS.items():
        regex = r"\b" + re.escape(ko) + r"\b"
        pattern_map.append((re.compile(regex), py))

    lines = code.splitlines()
    translated_lines = []

    for line in lines:
        new_line = line
        for (regex_pattern, replacement) in pattern_map:
            new_line = regex_pattern.sub(replacement, new_line)
        translated_lines.append(new_line)

    return "\n".join(translated_lines)
