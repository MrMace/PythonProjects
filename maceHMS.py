class User():
    
    def __init__(self,name, password, role):
        self.name = name;
        self.password = password
        self.role = role;
        
    def getName(self):
        return self.name;
    
    def getRole(self):
        return self.role;
    
class Reports(User):
    
    def __init__(self, roomsList, dirtyRooms, outOfOrderRooms, chosenRoom):
        self.roomsList = roomsList;
        self.dirtyRooms = dirtyRooms;
        self.outOfOrder = outOfOrderRooms;
        self.roomNum = chosenRoom;
        
    def getRoomsList(self):
        return self.roomsList;
        
    def getDirtyRooms(self):
        return self.dirtyRooms;
    
    def getOutOfOrder(self):
        return self.outOfOrder;
    
    def getRoomNum(self):
        return self.roomNum;
    
    def setRoomDirty(self):
        self.dirtyRooms.append(self.roomNum);
        
    def setRoomOOO(self):
        self.outOfOrder.append(self.roomNum);
        
    def removeRoom(self):
        self.cleanRooms.remove(self.roomNum);
        
    def checkRoom(self):
        if(self.roomNum in self.cleanRoom):
            print("In clean list");
        elif(self.roomNum in self.dirtyRooms):
            print("In dirty room list");
        elif(self.roomNum in self.outOfOrder):
            print("In Out of Order");
        else:
            print("Something went wrong");
       
def getReport(userRole,roomsObj):
        
    if(userRole == "Front Desk"):
        frontDesk(roomsObj);   
    elif(userRole == "House Keeping"):
        houseKeeping(roomsObj);
    elif(userRole == "Maintenace"):
        maintenace(roomsObj);
    else:
        return "Something went wrong";
                      
def frontDesk(roomObj):
    while True:
        print("--------------------------")
        
        print("Check guest in enter 1. ")
        print("Check guest out enter 2. ")
        print("Set Room Out of Order enter 3. ")
        print("Set Room Dirty enter 4. ")
        print("In house list enter 5. ")
        print("Exit enter 6")
        choice = input("What would you like to do? ")
        
        if(choice == "1"):
            print("Check in ");
        elif(choice == "2"):
            print("");
        elif(choice == "3"):
            print("");
        elif(choice == "4"):
            print(roomObj.getDirtyRooms());
            input("enter enter to continue: ");
        elif(choice == "5"):
            print("");
        elif(choice == "6"):
            break;
        
def houseKeeping(roomObj):
    while True:
        print("--------------------------")
        
        print("Print dirty room list enter 1. ")
        print("Set room to clean enter 2. ")
        print("Exit enter 3. ")
        choice = input("What would you like to do? ")
        
        if(choice == "1"):
            print(roomObj.getDirtyRooms());
            input("enter enter to continue: ");
        elif(choice == "2"):
            print("Rooms out of order: {}".format(roomObj.getDirtyRooms()));
            roomCleaned = input("Which of these rooms you want to mark as clean? ")
            input("");
        elif(choice == "3"):
            break;
        
def maintenace(roomObj):
    while True:
        print("--------------------------")
        
        print("Print out of order room list enter 1. ")
        print("Set room back to order enter 2. ")
        print("Exit enter 3. ")
        choice = input("What would you like to do? ")
        
        if(choice == "1"):
            print("Rooms out of order: {}".format(roomObj.getDirtyRooms()));
            roomToOrder = input("")
            print("");
        elif(choice == "2"):
            print("");
        elif(choice == "3"):
            break;
                         
def roles():
    print("______________________ ");
    print("Enter 1 for front desk. ");
    print("Enter 2 for House Keeping. ");
    print("Enter 3 for Maintenace. ");
    print("______________________ ");
    
    roleChoice = input("What is your role? ")
    
    if(roleChoice == "1"):
        return "Front Desk";
    elif(roleChoice == "2"):
        return  "House Keeping";
    elif(roleChoice == "3"):
        return "Maintenace";
    
    else:
        print("Invalid input try again")
        roles();

def getRoomNum(x):

    chosenRoom = input("Which room to check guest into? ");
    if(chosenRoom in x):
        return chosenRoom;
    else: 
        print("Room Number Not Available!")
        getRoomNum(rooms);
 

def main():

    roomsList = ["101", "102", "105", "202" , "203", "204", "302", "303", "304"]
    dirtyRooms = [];
    outOfOrderRooms = [];
    chosenRoom = "";
    roomsObj = Reports(roomsList,dirtyRooms,outOfOrderRooms,chosenRoom);
    employee = User(input("Username: "),(input("Password: ")), roles())
    userRole = employee.getRole();
    print(userRole);
    getReport(userRole,roomsObj);
    
    
    
main()
    
    
    
    
