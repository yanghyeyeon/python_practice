# SQLAlchemy를 사용한 데이터베이스 연동

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_URL = "sqlite:///calculation.sqlite3"

# 데이터베이스 엔진 생성
# sqlite는 동시에 한 스레드에서만 접근이 가능하기 때문에
# 여러스레드에서 접근 할 수 있도록 옵션 설정
engine = create_engine(DB_URL, connect_args={"check_same_thread" : False})

# 데이터베이스 연결세션 설정
session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)

# 모델클래스가 상속받을 기본 모델 클래스 지정
Base = declarative_base()