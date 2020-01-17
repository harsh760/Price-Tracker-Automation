class Product:
    def __init__(self,name ,price,link):
        self.name = name
        self.price = price
        self.link = link

    def serialize(self):
        return{
            "name" : self.name,
            "price" : self.price,
            "link" : self.link
        }    
        