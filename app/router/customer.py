from fastapi import HTTPException, status, Depends
from typing_extensions import Annotated
from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.repositories.customer_repository import CustomerRepository
from app.schemas.customer_schema import CustomerCreate, CustomerResponse
from app.services.customer_service import CustomerService
from app.database import get_session

router = APIRouter(prefix="/customer",
    tags=["customers"])


@router.post("/", response_model=CustomerResponse,status_code=status.HTTP_201_CREATED)
def create_customer(customer_data: CustomerCreate, db: Annotated[Session, Depends(get_session)]):
    repository = CustomerRepository(db)
    service = CustomerService(repository, db)

    try:
        return service.create_customer(customer_data)

    except ValueError as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=str(error))
        

@router.delete("/{id}",status_code=status.HTTP_200_OK)
def delete_customer(id: str, db: Annotated[Session, Depends(get_session)]):
    repository = CustomerRepository(db)
    service = CustomerService(repository, db)

    try:
        return service.delete_customer(id)

    except ValueError as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(error))