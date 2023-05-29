class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        # initialising the values 
        self.big = big
        self.medium = medium
        self.small = small
        
    def addCar(self, carType: int) -> bool:
        if carType == 1: # use the if statements to check the carType
            if self.big == 0: # check if they are not 0
                return False # if it is 0, return False
            self.big -= 1 # other wise return true but reduce the number of spots 
            return True
        elif carType == 2: # same for the rest
            if self.medium == 0:
                return False
            self.medium -= 1
            return True
        elif carType == 3:
            if self.small == 0:
                return False
            self.small -= 1
            return True
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

