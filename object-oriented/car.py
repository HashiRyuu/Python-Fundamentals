class Car:
    def __init__(self, efficient):
        #fuel efficiency = how far a car can 
        #travel using a certain amount of fuel
        self._fuelEfficiency = efficient
        self._fuel = 0
    
    def addGas(self, amount):
        self._fuel += amount
    
    def drive(self, amount):
        #gas used = distance / fuel efficiency
        self._fuel -= amount / self._fuelEfficiency
    
    def getGasLevel(self):
        return self._fuel
    
    
myHybrid = Car(50)   
myHybrid.addGas(20)
myHybrid.drive(100)
print(f"The gas level is {myHybrid.getGasLevel()}")
