#abstraction

from abc import ABC, abstractmethod

class Cars(ABC):
    
    @abstractmethod
    def start_engine(self):
        pass
    

class Ford(Cars):
    def start_engine():
        print ("Ford Started")
    
    def display_name():
        print ("Ford Car")
        

class Bikes:
    def color():
        return "Red"
    
    def _model():
        return"Yamaha"
        
    def __engine():
        return "250cc"


        
obj = Ford
obj.start_engine()
obj.display_name()

bike = Bikes
print("name= ", bike._model(), "color= ", bike.color())
