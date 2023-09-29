

#Class with 2 Methods
#Create Test cases

class TestClass:


    def __init__(self):
        pass

    def getString(self):
        self.s = input("Give me sth to say: ")
        
    def printString(self):
        print(self.s)

test = TestClass()
test.getString()
test.printString()