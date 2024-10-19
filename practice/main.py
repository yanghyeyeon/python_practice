from fastapi import FastAPI, Depends, HTTPException
from database import session_local, engine
import models, schemas, calculate_crud
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind = engine)

app = FastAPI()


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()


@app.post("/calculate", response_model=schemas.CalculationResponse)
async def calculate(calculation: schemas.CalculationCreate,
                    db: Session = Depends(get_db)):
    
    response = calculate_crud.create_calculation(db, calculation)

    return response

@app.get("/calculte", response_model=list[schemas.CalculationResponse])
async def find_all_calculation(db: Session = Depends(get_db)):
    
    all_calculation = calculate_crud.get_all_calculation(db)
    
    return all_calculation