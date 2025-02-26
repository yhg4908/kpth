import sys
from .번역기 import 코드_번역

def 메인():
    if len(sys.argv) < 2:
        print("사용법: ㅋㅍ [파일명].kpy")
        sys.exit(1)

    파일_경로 = sys.argv[1]
    with open(파일_경로, encoding="utf-8") as 파일:
        원본_코드 = 파일.read()

    파이썬_코드 = 코드_번역(원본_코드)

    exec(파이썬_코드, globals())

if __name__ == "__main__":
    메인()
