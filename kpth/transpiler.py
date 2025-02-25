# koreanlang/transpiler.py

# 한국어 키워드와 파이썬 키워드 매핑 딕셔너리
KEYWORD_MAPPING = {
    "불러오기": "import",
    "에서": "from",
    "출력": "print",
    # 추후 필요에 따라 다른 키워드 추가
}

def translate_line(line: str) -> str:
    """
    한 줄의 코드를 순회하며 매핑된 한국어 키워드를 파이썬 키워드로 치환.
    """
    for ko_keyword, py_keyword in KEYWORD_MAPPING.items():
        line = line.replace(ko_keyword, py_keyword)
    return line

def translate_code(code: str) -> str:
    """
    전체 소스 코드를 라인 단위로 번역.
    """
    lines = code.splitlines()
    translated_lines = [translate_line(line) for line in lines]
    return "\n".join(translated_lines)
