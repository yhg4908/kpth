# runner.py 예시

import sys
from .translator import translate_code

def main():
    if len(sys.argv) < 2:
        print("사용법: ㅋㅍ [파일명].kpy")
        sys.exit(1)

    file_path = sys.argv[1]
    with open(file_path, encoding="utf-8") as f:
        original_code = f.read()

    python_code = translate_code(original_code)

    exec(python_code, globals())

if __name__ == "__main__":
    main()
