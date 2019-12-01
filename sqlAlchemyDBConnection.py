from sqlalchemy import create_engine #object relation mapping(store object in relational db)
from sqlalchemy.ext.declarative import declarative_base;
from sqlalchemy import Column, Integer, String;
from sqlalchemy.orm import sessionmaker;

Base = declarative_base() #global var, base class provided by SqlAlchemy to ORM compatiable/capable

class Customer(Base): #Base here is to make my class ORM compatiable/capable.   
    #constructor
    def __init__(self, name, address, creditCardNum, licensePlate):
        self.name = name
        self.address = address
        self.creditCardNum = creditCardNum
        self.licensePlate = licensePlate
        
        #name of the table, for objects of this to be stored in.
    __tablename__ = "customer"
        
    #column defining in db
    id = Column(Integer, primary_key = True); #unique identifier of table
    name = Column(String);
    address = Column(String);
    creditCardNum = Column(Integer);
    licensePlate = Column(String);
        
    def __repr__(self):  #printable representational of the object
        return "<customer(name= {0}, address= {1}, creditcard Number= {2}, license Plate= {3} )>".format(self.name, self.address, self.creditCardNum, self.licensePlate);
                
                
def main():
    engine = create_engine('sqlite:///:memory:', echo=False) # uses system memory, display sql on screen false = no.    
    Base.metadata.create_all(engine); #knows what engine to use to store objects.
    
    Session = sessionmaker(bind=engine); #creates session opens connection. 
    session = Session(); #instantiates object from Session

    #add content to the database.
    session.add_all([
        Customer('Boy Guy', '2209 Fresh Road',  987654321123, 'BLAH56'),
        Customer('Curious George', '1 Tree Top Lane',  888888888888, 'NANNAS'),
        Customer("Frank White", "555 Place Lane Dr.", 4444543223547894, "L8ER5") ])
    session.commit(); #commits the info
    
    for row in session.query(Customer).all(): #Loops through the db.
        print(row.name, ", ", row.address); #prints out the name and address of customers
       

main()





