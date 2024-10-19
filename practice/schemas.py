from pydantic import BaseModel, Field
from typing_extensions import Optional

# request 받거나, response를 받을때
# 기본 형식을 만들어 놓을 수 있다.
class CalculationBase(BaseModel):
    num1: float
    num2: float
    operation: str = Field(..., pattern=r'^(\\+|\\-|\\*|\\/|\\^|sqrt)')  # '\\' 사용하여 이스케이프 처리
    result: Optional[float] = None

# SqlAlchemy 모델 : 데이터베이스의 통신을 위한 데이터 구조정의
# Pydantic 모델 : API 요청과 응답을 위한 데이터 구조정의 

# request 요청 모델
class CalculationCreate(CalculationBase):
    pass

# response 응답 모델
class CalculationResponse(CalculationBase):
    id : int

# 업데이트할때 사용되는 request 모델
class TeacherUpdate(BaseModel):
    name: Optional [str] = None
    is_active: Optional [bool] = None
    nickname: Optional[str] = None
    description: Optional[str] = None
