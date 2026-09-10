from sqlalchemy import TIMESTAMP, ForeignKey, String, Boolean, text, CheckConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase
from typing import Optional, List

class Base(DeclarativeBase):
    pass

class Customer(Base): 
    __tablename__ = "Customers"

    id: Mapped[str] = mapped_column(String(20),primary_key=True)
    fullname: Mapped [str] = mapped_column(String(50))
    email: Mapped [str] = mapped_column(String(255), unique=True)
    
    def __repr__(self) -> str:
        return f"Customer(id={self.id!r}, full_name={self.fullname!r}, email={self.email!r})"
    
    __table_args__ = (
        CheckConstraint(
        r"email ~ '^[^@\s]+@[^@\s]+\.[^@\s]+$'",
        name="ck_customer_email_format"
        ),
        CheckConstraint(
            "fullname ~ '^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$'",
            name="chk_fullname"
        ),
    )
    
    

# class Category(Base): 
#     __tablename__ = "categories"

#     id: Mapped [int] = mapped_column(primary_key=True, autoincrement=True)
#     name:  Mapped [str] = mapped_column(String(50))
    
#     def __repr__(self) -> str:
#         return f"Category(id={self.id!r}, name={self.name!r})"
    
    
# class User(Base): 
#     __tablename__ = "users"

#     id: Mapped [int] = mapped_column(primary_key=True)
#     username:  Mapped [str] = mapped_column(String(25))
#     lastname: Mapped [str] = mapped_column(String(25))
#     firstname: Mapped [str] = mapped_column(String(25))
#     email: Mapped [str] = mapped_column(String(255), unique=True)
#     password_hash: Mapped [str] = mapped_column(String(255))
    
#     __table_args__ = (
#             CheckConstraint(
#                 r"email ~ '^[^@\s]+@[^@\s]+\.[^@\s]+$'",
#                 name="chk__email_format"
#             ),
            
#     )
    
#     def __repr__(self) -> str:
#         return f"""User(id={self.id!r}, name={self.username!r}, lastname={self.lastname!r}, 
#                     firstname={self.firstname!r}), email={self.email!r}, password={self.password!r})"""