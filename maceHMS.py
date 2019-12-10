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

class Reports(User):
   
    def getReport(self):
        
        if(User.getRole(self) == "Front Desk"):
            return "GSR Report";
        
        

    
    
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
       
      
       
rooms = ["101", "102", "105", "202" , "203", "204", "302", "303", "304"]
print(rooms)
checkedInRoom = rooms[2];
rooms.remove(checkedInRoom);
print(rooms)
dirtyRooms = ["none"];
print(dirtyRooms)
dirtyRooms[0]=checkedInRoom;
print(dirtyRooms)

outOfOrderRooms = [];
print(rooms)

def main():
    
    employee = User(input("What is your name? "),(input("What is your password? ")), roles())
    userRole = employee.getRole();
    print(Reports.getReport(employee));
    
    
main()
    
    
    
    
