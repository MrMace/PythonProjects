import json as j


class InventoryItem:
    
    def __init__(self, itemName):
        self.name = itemName
        self.totalStocked = 0
        self.totalInStock = 0
        self.totalSlots = 0
        
    def addToStocked (self, stockAmt ):
        self.totalStocked = self.totalStocked + stockAmt
          
    def addToInStock (self, inStockAmt):
        self.totalInStock = self.totalInStock + inStockAmt
        
    def incrementSlots(self):
        self.totalSlots = self.totalSlots + 1
        
    def __repr__(self):
        return '{} In Stock: {}, Stocked: {}, Slots: {}'.format(self.name,self.totalInStock, self.totalStocked, self.totalSlots)
    
    def getNumSold(self):
        return self.totalStocked - self.totalInStock
    
    def getSoldPct(self):
        return self.getNumSold() / self.totalStocked
    
    def getStockNeed(self):
        return 8 * self.totalSlots - self.totalInStock
    
    def getName(self):
        return self.name
    
    def getNumInStock(self):
        return self.totalInStock
    
def main():
    itemNameToInventoryItem = {}
    inventoryFileNames = "REID_1F_20171004.json","REID_2F_20171004.json","REID_3F_20171004.json"
    for inventoryFileName in inventoryFileNames:
        inventoryFile = open(inventoryFileName, 'r')

        inventoryData = j.loads(inventoryFile.read())
        print(inventoryData['machine_label'])
        print(inventoryData['machine_id'])

        contents = inventoryData['contents']

        for row in contents:
            #print(row['row'])
            for slot in row['slots']:
                #searches inventoryItem to see if avail, if not creates.
                itemName = slot['item_name']
                inventoryItem = itemNameToInventoryItem.get(itemName, InventoryItem(itemName))
                
                inventoryItem.addToStocked(slot['last_stock'])
                inventoryItem.addToInStock(slot['current_stock'])
                inventoryItem.incrementSlots();
                #store item
                itemNameToInventoryItem[itemName] = inventoryItem
    cokeItem = itemNameToInventoryItem['Coke']
    
    print(cokeItem)
    print(cokeItem.getNumSold())
    print(cokeItem.getSoldPct() * 100 )
    print(cokeItem.getStockNeed())
    
    sortChoice = ''
    inventoryItemsList = list(itemNameToInventoryItem.values() )
    while sortChoice != 'q':
        sortChoice = input("Sort by (n)ame, (p)ct sold, (s)tocking need, or (q) to quit: ")
        if sortChoice == 'n':
            inventoryItemsList.sort(key = InventoryItem.getName)
        elif sortChoice == 'p':
            inventoryItemsList.sort(key = InventoryItem.getSoldPct)
            inventoryItemsList.reverse()
        elif sortChoice == 's':
            inventoryItemsList.sort(key = InventoryItem.getStockNeed)
            inventoryItemsList.reverse()
            
        print('Item Name            Sold     % Sold     In Stock Stock needs ')
        
        for item in inventoryItemsList:
            print('{:20} {:8} {:8.2f}% {:8} {:8}'.format(item.getName(), item.getNumSold(), item.getSoldPct() * 100, item.getNumInStock(), item.getStockNeed()))
        print()
main()