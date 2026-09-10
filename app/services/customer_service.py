from httpx import delete

from app.models.customer_model import Customer


class CustomerService:

    def __init__(self, repository, db):
        self.repository = repository
        self.db = db
    
    
    def create_customer(self, customer_data):
        
        with self.db.begin():
            existing_customer = self.repository.get_customer_by_id(customer_data.id)   # 1. Buscar si existe
        
            if existing_customer:
                raise ValueError("Customer already exists")  # 2. Si existe → error

            customer = Customer(            # 3. Si no existe → crear
                id=customer_data.id,
                fullname=customer_data.fullname,
                email=customer_data.email
            )
        
            self.repository.create(customer)  # crea el cliente

        return customer     # 4. Retornar cliente
    
    
    
    def delete_customer(self, id):
            
            with self.db.begin():
                existing_customer = self.repository.get_customer_by_id(id) 
            
                if not existing_customer:
                    raise ValueError("Customer doesn't exist")
                
                self.repository.delete(existing_customer)  
    
            return {"message": "customer_deleted"}    