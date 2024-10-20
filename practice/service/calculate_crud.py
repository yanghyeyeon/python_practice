from sqlalchemy.orm import Session
import practice.schemas.schemas as schemas, practice.models.models as models, math
from fastapi import HTTPException

def create_calculation(db : Session, calculation = schemas.CalculationCreate):
    
    # 유효성 검사: operation 값 확인
    valid_operations = {"+", "-", "*", "/", "^", "sqrt"}
    if calculation.operation not in valid_operations:
        raise HTTPException(status_code=400, detail="Invalid operation")
    
    if calculation.operation == "/" and calculation.num2 == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    
    if calculation.operation == "sqrt" and calculation.num1 < 0:
        raise HTTPException(status_code=400, detail="Cannot take square root of negative number")
    
    # 연산 수행
    if calculation.operation == "+":
        calculation.result = calculation.num1 + calculation.num2
    elif calculation.operation == "-":
        calculation.result = calculation.num1 - calculation.num2
    elif calculation.operation == "*":
        calculation.result = calculation.num1 * calculation.num2
    elif calculation.operation == "/":
        calculation.result = calculation.num1 / calculation.num2
    elif calculation.operation == "^":
        calculation.result = calculation.num1 ** calculation.num2
    elif calculation.operation == "sqrt":
        calculation.result = math.sqrt(calculation.num1)
    
    db_calculation = models.Calculation(
        num1 = calculation.num1,
        num2 = calculation.num2,
        operation = calculation.operation,
        result = calculation.result
    )
    
    db.add(db_calculation)
    db.commit()
    
    return db_calculation


def get_all_calculation(db : Session):
    
    all_calculation = db.query(models.Calculation).all()
    
    return all_calculation