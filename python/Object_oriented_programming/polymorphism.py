class Shopping:
    def __init__(self,basket,buyer):
        self.basket = list(basket)
        self.buyer = buyer

    def __len__(self):
        print("Redefine basket")
        count = len(self.basket)
        return count * 2

shopping = Shopping(["Adhmed","abdi"],"abdi")
print(len(shopping))
    