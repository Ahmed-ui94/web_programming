from dataclasses import dataclass, field
from typing import List



@dataclass
class Category:
    budget_category: str
  #create a instant variable that is not going to be passed to object 
  #initialisation
    ledger: List[str] = field(default_factory=list, init=False) 

    def deposit(self,amount: int, description: str = " "):
        self.ledger.append(f'Amount: {amount}, description" {description}')

    def withdraw(self, amount, description= " "):
      ...





def create_spend_chart(categories):
    ...


Food = Category("food")
Food.deposit(1000, "initial deposit")
print(Food)