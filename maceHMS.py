class User():
    
    def __init__(self,name, password, role):
        self.name = name;
        self.password = password
        self.role = role;
        
    def getName(self):
        return self.name;
    
    def getRole(self):
        return self.role;
    
class FrontDesk(User):
       
    def guestCheckIn(self):
        pass
    
    def guestCheckOut(self):
        pass
       
class HouseKeeping(User):
    pass
class Maintenace(User):
    pass

class Rooms():
    
    def __init__(self, roomList, dirtyRooms, outOfOrderRooms, chosenRoom):
        self.cleanRooms = roomList;
        self.dirtyRooms = dirtyRooms;
        self.outOfOrder = outOfOrderRooms;
        self.roomNum = chosenRoom;
        
    def getRoomList(self):
        return self.cleanRooms;
        
    def getDirtyRooms(self):
        return self.dirtyRooms;
    
    def getOutOfOrder(self):
        return self.outOfOrder;
    
    def getRoomNum(self):
        return self.roomNum;
    
    def setRoomDirty(self):
        self.removeRoom()
        self.dirtyRooms.append(self.roomNum);
        
    def setRoomOOO(self):
        self.removeRoom()
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
                   
class Reports(Rooms):
       
    def getReport(self):
        
        if(User.getRole(self) == "Front Desk"):
            return "GSR Report";
        elif(User.getRole(self) == "House Keeping"):
            return "HouseKeeping Reports";
        elif(User.getRole(self) == "Maintenace"):
             return "Maintainece Reports";
        else:
             return "Something went wrong";
              
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

def getRoomNum(rooms):

    chosenRoom = input("Which room to check guest into? ");
    if(chosenRoom in rooms):
        return chosenRoom;
    else: 
        print("Room Number Not Available!")
        getRoomNum(rooms);
       
rooms = ["101", "102", "105", "202" , "203", "204", "302", "303", "304"]
dirtyRooms = [];
outOfOrderRooms = [];
print(rooms);
chosenRoom = getRoomNum(rooms)
roomsObj = Rooms(rooms,dirtyRooms,outOfOrderRooms,chosenRoom);
print(roomsObj.getRoomNum())

def login():
    employee = User(input("Username: "),(input("Password: ")), roles())
    userRole = employee.getRole();
    print(Reports.getReport(employee));

def main():
    
    login();
    
main()
    
    
    
    
