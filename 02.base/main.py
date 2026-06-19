class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = []
    def deposit(self,amount,description=""):
        self.ledger.append({'amount': amount, 'description': description})
    def withdraw(self,amount,description=""):
        if not self.check_funds(amount):
            return "Not Enough Balance"
        self.ledger.append({'amount': -amount, 'description': description})        
    def get_balance(self):
        if not self.ledger:
            return 0
        total = 0
        for value in self.ledger:
            total += value["amount"] 
        return total  
    def transfer(self,amount,category):          
            if self.check_funds(amount):
                self.withdraw(amount,f"Transfer to {category.name}")
                category.deposit(amount,f"Transfered from  {self.name}")
                return True
            return False        
    def check_funds(self,amount):
        if self.get_balance() < amount:
            return False
        return True
    def __str__(self):
        title = f"{self.name.center(30,"*")}\n"
        struct = ""
        for val in self.ledger:
            desc = f"{val["description"][:23].ljust(23)}"
            amn = f"{val["amount"]}".rjust(7)+"\n"
            struct = struct + desc+amn
        return title + struct
    
food = Category("Food")
food.deposit(500,"Food1")
food.deposit(500,"Food2")
food.withdraw(50,"Food2")

print(food)

def create_spend_chart(categories):
    pass
x = "HELLO".center(30,"*")
print(x)


