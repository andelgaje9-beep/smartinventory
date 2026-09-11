from sqlalchemy import select
from app.models.customer_model import Customer

class CustomerRepository:

    def __init__(self, db):
        self.db = db

    def get_customer_by_id(self, customer_id):
        stmt = select(Customer).where(Customer.customer_id == customer_id)

        return self.db.execute(stmt).scalar_one_or_none()
    
    
    def get_customers(self):
            stmt = select(Customer)
    
            return self.db.execute(stmt).scalars().all()
        
        
    def create(self, customer):
        self.db.add(customer)
        return customer
    
    def delete(self, customer):
        self.db.delete(customer)
        return customer
    