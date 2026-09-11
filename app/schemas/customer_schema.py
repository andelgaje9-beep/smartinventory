from pydantic import BaseModel, EmailStr, Field, field_validator


class CustomerCreate(BaseModel):
    customer_id: str = Field(min_length=6,max_length=20,pattern=r"^\d+$")
    customer_fullname: str = Field(min_length=2,max_length=25,pattern=r"^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$")
    customer_email: EmailStr
    
class CustomerResponse(BaseModel):
    customer_fullname: str