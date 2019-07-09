

class GroceryItem:
    def __init__(self, name, id, price):
        self.name = name
        self.id = id
        self.price = price
        
    def priceForNPurchases(self, numOfPurchases):
        return self.price * numOfPurchases
        
def main():
    burritoGroceryItem = GroceryItem("Burrito", 241, 4.99)
    
    print(burritoGroceryItem.priceForNPurchases(3))

    
    hotDogGroceryItem = GroceryItem("Hot Dog", 173, 1.99)
    print(hotDogGroceryItem.priceForNPurchases(3))
    
    
main()