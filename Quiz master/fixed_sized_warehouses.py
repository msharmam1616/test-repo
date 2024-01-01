import os
class Product:
    count = 0

    def __init__(self, name):
        if Product.count < Limit.get_limit():
            self.name = name
            Product.count += 1
        else:
            raise UserLimitExceeded(name)

    def __del__(self):
        Product.count -= 1

    
class Limit:
    limit = 3

    @classmethod
    def get_limit(cls):
        return cls.limit
    
    @classmethod
    def set_limit(cls, new_limit):
        cls.limit = new_limit

    
class UserLimitExceeded(Exception):
    def __init__(self, name):
        limit = Limit.get_limit()
        super().__init__(f"Product {name} cannot be created. Maximum {limit} products allowed")

def main(path="/dev/stdout"):
    max_limit = int (input ())
    Limit.set_limit(max_limit)
    products = {}
    def new_product (product_name: str) -> str:
        product = Product(product_name)
        products[product_name] = product
        return f"{product.name} created"
    
    def del_product (product_name: str) -> str:
        product = products.get(product_name, f"{product_name} not found")
        if isinstance (product, Product):
            del products[product_name]
            return f"{product_name} deleted successfully" 
        raise Exception(product)
    
    def print_product (product_name: str) -> str:
        product = products. get(product_name, f"{product_name} not found")
        if isinstance (product, Product):
            return f"{product. name} found" 
        raise Exception (product)

    def change_limit (limit: int) -> str:
        limit = int (limit)
        Limit.set_limit(limit)
        return f"limit updated to {limit}"
    func_map = {
        "new": new_product,
        "del": del_product,
        "print": print_product,
        "limit": change_limit,
    }
    num_operations = int(input ())

    for i in range (num_operations) :
        cmd, arg = input () .split ()
        try:
            res = func_map [cmd] (arg)
            print (res)
        except UserLimitExceeded as ule:
            print (ule)
        except Exception as e:
            print (e)

if __name__ == '__main__':
    path = " /dev/stdout"
    if "OUTPUT_PATH" in os.environ.keys () :
        path = os. environ ["OUTPUT_PATH"]
    main (path=path)

