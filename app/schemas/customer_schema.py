from pydantic import BaseModel, EmailStr, Field, field_validator


class CustomerCreate(BaseModel):
    id: str = Field(min_length=6,max_length=20,pattern=r"^\d+$")
    fullname: str = Field(min_length=2,max_length=25,pattern=r"^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$")
    email: EmailStr
    
class CustomerResponse(BaseModel):
    fullname: str