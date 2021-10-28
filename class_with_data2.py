from dataclasses import dataclass

@dataclass
class Medicine:
    name : str
    brand : str
    price : str 
    component : str
    mfg : str = "12/21"  # default
    exp : str = "12/23"
    detail : str = "no detail"


m = Medicine('Sumo','idontcare',50,
            'paracetamol & nimusilide','11/21','11/23','i dont care')

m2 = Medicine('Disprin','idontcare',20,
            'paracetamol','11/21','11/23','i dont care ok')

print(m)

print(m == m2)
