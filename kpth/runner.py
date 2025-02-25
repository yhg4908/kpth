# koreanlang/runner.py
import sys
from koreanlang.transpiler import translate_code

def run_file(file_path: str):
    with open(file_path, encoding="utf-8") as f:
        code = f.read()
    # 한국어 코드 -> 파이썬 코드로 변환
    python_code = translate_code(code)
    
    # 변환된 파이썬 코드를 실행
    exec(python_code, globals())

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("사용법: python runner.py [소스파일 경로]")
    else:
        run_file(sys.argv[1])
