from tkinter import N


print("""

    1 >   CAR_1  |||  Name : Tesla
    2 >   CAR_2  |||  Name : Saipa 


""")

class window:
    def __init__(self, type, color, bulletproof):
        self.type = type
        self.color = color
        self.bulletproof = bulletproof
    
    def __str__(self):
        return f"Type : {self.type} Color : {self.color} Bulletproof : {self.bulletproof}"

class Wheel:
    def __init__(self, name, company):
        self.name = name
        self.company = company


    def __str__(self):
        return f"Name_Wheel : {self.name} Company : {self.company}"

class car:
    def __init__(self, name, window, wheel):
        self.name = name
        self.wheel = wheel
        self.window = window
    
    def __str__(self):
        return f"Name : {self.name} window : {self.window} wheel : {self.wheel}"


window1 = window(type="Smoky", color="Black", bulletproof="Yes")
window2 = window(type="Smoky", color="Yellow", bulletproof="No")

wheel1 = Wheel(name="wheel_tesla", company="Tesla")
wheel2 = Wheel(name="wheel_saipa", company="saipa")

car_1 = car(name="Tesla", window=window2, wheel=wheel1)
car_2 = car(name="saipa", window=window2, wheel=wheel1)

# print(car_1)

car_selection = int(input("Select The Type Of Car : "))

for i in range(car_selection):
    if car_selection == 1:
        print(car_1)
    elif car_selection == 2:
        print(car_2)
    else:
        print("The value entered is incorrect .... :( ")
