import os
from dotenv import load_dotenv
from typing import Optional

from constants.path import PROJECT_DIR


class Env:
    def __init__(self):
        # env 파일을 불러온다.
        load_dotenv(os.path.join(PROJECT_DIR, ".env"))

    # ENV 파일 안에 있는 값을 Key를 통해 가져온다.
    def get(self, key: str) -> Optional[str]:
        return os.environ.get(key)


""" 사용 예시
env = Env() # 인스턴스(객체) 생성
print(env.get("MYSQL_USER")) # MYSQL_USER의 값을 가져와 출력한다.
"""