"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name,details):
        self.name = name
        self.details = details

    def get_pay(self):
        pass

    def __str__(self):
        return self.name

class MonthlyEmployee(Employee):
    
    def __init__ (self,name,salary,bonus = 0 ,contractPay = 0, contracts = 0):
        super().__init__(self,name)
        self.salary = salary
        self.bonus = bonus
        self.contractPay = contractPay
        self.contracts = contracts

    
    def get_pay(self):
        return (self.salary + self.bonus + (self.contractPay * self.contracts))
        

    def __str__(self):
        string = f"{self.name} works on a monthly salary of {self.salary}"
       
        if self.contractPay:
            string += f"and recieves a commission for {self.contracts} contract(s) at {self.contractPay}/contract"
        if self.bonus:
          string += f" and recieves a bonus commission of 1500"
    
        string += f". Their total pay is {self.get_pay}"

        return string


class ContractEmployee(Employee):
    
    def __init__ (self,name,wage,wageHours,bonus = 0 ,contractPay = 0, contracts = 0):
        super().__init__(self,name)
        self.wage = wage

        self.bonus = bonus
        self.contractPay = contractPay
        self.contracts = contracts
        self.wageHours = wageHours

    
    def get_pay(self):
        return ((self.wage * self.wageHours) + self.bonus + (self.contractPay * self.contracts))
        

    def __str__(self):
        string = f"{self.name} works on a contract of {self.wageHours} at {self.wage}/hour"
       
        if self.contractPay:
            string += f"and recieves a commission for {self.contracts} contract(s) at {self.contractPay}/contract"
        if self.bonus:
          string += f" and recieves a bonus commission of 1500"
    
        string += f". Their total pay is {self.get_pay}"

        return string


        
       



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = MonthlyEmployee('Billie',4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = ContractEmployee('Charlie',25,100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = MonthlyEmployee('Renee',3000,0,220,4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = ContractEmployee('Jan',25,150,0,220,3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = MonthlyEmployee('Robbie',2000,1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = ContractEmployee('Ariel',30,120,600)
