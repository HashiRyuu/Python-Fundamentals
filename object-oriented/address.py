class Address:
    def __init__(self, HouseNumber, Street, ApartmentNumber, 
                 City, State, PostalCode):
        
        self._houseNum = HouseNumber
        self._street = Street
        self._apartmentNumber = ApartmentNumber
        self._city = City
        self._state = State
        self._postalCode = PostalCode
        
    def printAddress(self):
        if self._apartmentNumber != "":
            print(f"{self._houseNum} {self._street} {self._apartmentNumber}")
            print(f"{self._city}, {self._state} {self._postalCode}")
        else:
            print(f"{self._houseNum} {self._street}")
            print(f"{self._city}, {self._state} {self._postalCode}")
            
    
    def comesBefore(self, other):
        return self._postalCode < other._postalCode
    
def main():
    a = Address("2500", "University Drive", "", "Some City", "Some State", "12345")
    b = Address("12-1200", "College Blvd", "", "Other City", "Other State", "99102")
    
    print("Address a is:")
    a.printAddress()
    
    print()
    
    print("Address b is:")
    b.printAddress()
    
    print()
    
    print(f"a comes before b is {a.comesBefore(b)}")

main()
