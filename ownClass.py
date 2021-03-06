Advait Namburi

import random

#demo
def main():
    
    newCoin = Coin("penny", 10, "Gold", 2002, 100) #creates a new coin object

    newCoin.flip() #simulates the coin flip

    #Edits the size variable and the year variable which also changes the value variable
    newCoin.setSize(100)
    newCoin.setYear(2002)

    #prints out the variables of the coin
    newCoin.getYear()
    newCoin.getMetal()
    newCoin.getName()
    newCoin.getValue()
    newCoin.getSize()


class Coin:

    shape = 'Circle'
    metal = 'Gold'
   
    def __init__(self,name,size,metal,year,value):
        self.__name = name #unique name of the coin, cannot be changed
        self.__size = size #size of the coin, which can later be changed but will affect the value
        self.__metal = metal #what the coin is made of, cannot be changed
        self.__value = value #value of the coin, cannot be directly changed
        self.__year = year #when the coin was made

    def flip(self): #simulates the flipping of the coin
        if random.randint(0,1) == 1:
            print("The coin landed as heads!")
        else:
            print("The coin landed as tails!")

    def age(self,newYear): #simulating if someone left the coin somewhere and how much value it would gain for X amount of years
        newVal = self.__value*(2.718^(0.062*(newYear-self.__year)))
        self.__value = newVal
        setYear(newYear)

    #below are all the get-set methods

    def getName(self):
        return self.__name

    def getSize(self):
        return self.__size

    def setSize(self,new):
        print("Changing the size depreciated the value of your coin!")
        self.__value/=2
        self.__size = new

    def getMetal(self):
        return self.__metal

    def getYear(self):
        return self.__year

    def setYear(self,new):
        self.__year = new

    def getValue(self):
        return self.__value

if __name__ == "__main__":
    main()

