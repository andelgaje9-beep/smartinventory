from httpx import delete

from app.models.customer_model import Customer


class CustomerService:

    def __init__(self, repository, db):
        self.repository = repository
        self.db = db
    
    
    def create_customer(self, customer_data):
        
        with self.db.begin():
            existing_customer = self.repository.get_customer_by_id(customer_data.customer_id)   # 1. Buscar si existe
        
            if existing_customer:
                raise ValueError("Customer already exists")  # 2. Si existe → error

            customer = Customer(            # 3. Si no existe → crear
                customer_id=customer_data.customer_id,
                customer_fullname=customer_data.customer_fullname,
                customer_email=customer_data.customer_email
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
        
        
    def get_customer(self, id):
                
        with self.db.begin():
            existing_customer = self.repository.get_customer_by_id(id) 

        
            if not existing_customer:
                raise ValueError(f"Customer with if {id} doesn't exist")

        return existing_customer
    
    
    def get_all_customers(self):
                    
            with self.db.begin():
                customers_list = self.repository.get_customers() 
            
                if not customers_list:
                    raise ValueError(f"Customer with if {id} doesn't exist")
    
            return customers_list