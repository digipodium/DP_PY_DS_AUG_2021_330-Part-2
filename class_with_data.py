
 # not using data class
class Medicine:

    def __init__(self, name, brand, price, component, mfg, exp,details) :
        self.name = name
        self.brand = brand
        self.price = price
        self.component = component
        self.mfg = mfg
        self.exp = exp
        self.details = details
    
    def __str__(self):
        return self.name

    def __lt__(self,other):
        return self.price < other.price


m = Medicine('Sumo','idontcare',50,
            'paracetamol & nimusilide','11/21','11/23','i dont care')
m2 = Medicine('Disprin','idontcare',20,
            'paracetamol','11/21','11/23','i dont care ok')

print(m)

print(m < m2)