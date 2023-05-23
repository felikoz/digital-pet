import time 
import random as rd
money = 0

class pet :
    def __init__(self, name , age , hunger , hapinnes,alive,type) :
        self.name = name 
        self.age = 1 
        self.hunger = 100
        self.hapiness = 100
        self.type = type 
        self.alive = True
    

    def giveName(self):
        newname = input("enter your pets name ")
        self.name = newname
        print(f"your pet's name is  {self.name}")

    
    def hungerdown(self):
        print(f"your {self.name}'s  hunger has depleted by 5 ")
        self.hunger -= 5 ; 
        print(f"his  hunger is {self.hunger}")

    def died(self):
        if self.hunger <= 0 :
            print(f"your animal named {self.name} as died a the age of {self.age}")
            self.alive = False

        elif self.age==100: 
            print(f"your pet {self.name} was very old and passed away , he lived at good life and died a 100y/o")
            self.alive = False
        

    def aging(self):
        self.age += 1 
        print(f"happy birthday {self.name}  , it  is now  now {self.age}")

    def hungry(self):
        if self.hunger <=20 :
            print("he hungy is so he grogy")
            self.hapiness -= 10



def work (money):
    workqlt = rd.randint(1,3)
    match workqlt:
        case 1: 
            print("your did exelent today and earned 20$")
            money += 20
        case 2: 
            print("your did ok and won 15$")
            money += 15
        case 3:
            print("youd did terrible and only earned 5$")
            money += 5




def action ():
    print("what would you like to do")
    print("work:1")
    print("play with your pet:2")
    print("buy something :3")
    print("save and leave ?:4")
    useraction = input("?         ")
    match useraction:
        case 1:
            work(money)
        case 2: 
            print("your pet is now a bit happier ")
            cat.hapiness += 10
        case 3:
            print(f"you have {money}$")
            



cat = pet("",1,100,100,True,"")




while cat.alive ==True :
    if cat.name == "":
        cat.giveName()
    cat.hungerdown()
    cat.died()
    cat.aging()
    work(money)
    time.sleep(30)

    