from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        
    @abstractmethod
    def calculate_fine(self):
        pass
    
    
class Member(Person):
    def __init__(self, name, email, mem_id):
        super().__init__(name, email)
        self.mem_id = mem_id
    def calculate_fine(self, days):
        return days*2        
    
member = Member("farhat", "farhat@hotmail.com", 4)
print(member.mem_id)

print(member.calculate_fine(3))    