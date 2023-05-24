import time 
import random as rd
money = 10000000
inventory = {
    "food" : 0,
    "premium_food" : 0,
    "toy "  : 0,
    "premium_toy" : 0

}
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
    
    def giveType(self):
        petty = input(f"what is the pet type")
        print(f"your pet type is {petty}")
    



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



def feed(inventory):
    print("")



def shop (money, inventory):
    print("-----------------------------------------------------------------------------------")
    print("your inventory ")
    print(inventory)
    print("-----------------------------------------------------------------------------------")
    print ("items in shop")
    print("1:food :15$")
    print("2:premium food : 30$")
    print ("3:toy :50$")
    print ("4:premium toy : 100$")
    itembought = input("what is the item you want to buy")
    match itembought:
        case "1": 
            if money >= 15:
                money -= 15 
                inventory["food"] += 1 
                print("you bought food for 15$")
                print(f"you now own food and your balance is {money}")
        case "2": 
            if money >= 30:
                money -= 30 
                inventory["premium_food"] += 1 
                print("you bought  premium food for 30$")
                print(f"you now own premium food and your balance is {money}")
        case "3":
            if money >= 50:
                money -= 50
                inventory["toy"] += 1 
                print("you bought toy for 50$")
                print(f"you now own a toy and you balance is {money}")
        case "4":
            if money >= 100:
                money -= 100
                inventory["premium_toy"] += 1
                print("you bought premium toy for 100$")
                print(f"you now own a premium toy and your balance is {money}")
        case _:
            print("this is not a valid action")

def action ():
    print("----------------------------------------------------------------")
    print("what would you like to do")
    print("work:1")
    print("play with your pet:2")
    print("buy something :3")
    print("save and leave ?:4")
    print("feed your pet :5")
    print("----------------------------------------------------------------")

    useraction = input("?"   )
    
    match useraction:
        case "1":
            work(money)
        case "2": 
            print("your pet is now a bit happier ")
            cat.hapiness += 10
        case "3":
            print(f"you have {money}$")
            shop(money,inventory)
        case "5":
            print("")
        case _:
            print("this is not a valid action")

            



cat = pet("",1,100,100,True,"")




while cat.alive ==True :
    if cat.name == "" :
        cat.giveName()
    cat.hungerdown()
    cat.died()
    cat.aging()
    action()

    
    

    