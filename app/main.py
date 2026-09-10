from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field, field_validator
from app.models.customer_model import Base
from app.router import customer
from app.database import engine
import re

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(customer.router)

    
class Usercreate(BaseModel):
    id: int
    username: str
    lastname: str
    firstname: str
    email: EmailStr
    password: str = Field(min_length=6, max_length=15)
    
    
    @field_validator("password")
    @classmethod
    def validate_password(cls, value: str) -> str:

        if not re.search(r"[A-Z]", value):
            raise ValueError("La contraseña debe contener una mayúscula")

        if not re.search(r"[0-9]", value):
            raise ValueError("La contraseña debe contener un número")

        if not re.search(r"[^A-Za-z0-9]", value):
            raise ValueError("La contraseña debe contener un símbolo")

        return value
    
# prueba
# customer = CustomerCreate(
#     id= 1,
#     name="Andres",
#     email="andres@gmail.c"
# )

# print(customer)

# with Session(engine) as session:
#     andres = Customer(
#     id= 1095808765,
#     name="andres",
#     email="andelg.aje9@gmail.com")
    
#     session.add_all([andres])
    
#     session.commit()


@app.get("/")
async def root():
    return {"message": "Hello World"}