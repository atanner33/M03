# Name: Alex Tanner
# Date: 9/5/2023
# Purpose of this code is to accept input from the user invovling details of a car, store that information, then correctly repeat it back.

class vehicle():
    def __init__(type):
         vehicle.type = type


class automobile(vehicle):
    def __init__(year, make, model, doorCount, roofType):
        automobile.year = year
        automobile.make = make
        automobile.model = model
        automobile.doorCount = doorCount
        automobile.roofType = roofType

vehicle.type = input("Please select your vehicle type - car, truck, plane, boat, or a broomstick: ")

automobile.year = input("Please enter the year of your vehicle: ")
automobile.make = input("Please enter the make of your vehicle: ")
automobile.model = input("Please enter the model of your vehicle: ")
automobile.doorCount = input("Please enter the doorcount of your vehicle: ")
automobile.roofType = input("Please enter the roof type (soild or sun roof) of your vehicle: ")

print("Vehicle type: ", vehicle.type)
print("Year: ", automobile.year)
print("Make: ", automobile.make)
print("Model: ", automobile.model)
print("Number of doors: ", automobile.doorCount)
print("Type of roof: ", automobile.roofType)



#error checking loop needed? not sure....

# vtype_sen = False
# while vtype_sen == False:
#     if vtype == "car" or "truck" or "plane" or "boat" or "a broomstick":
#         user_vehicle = vehicle(vtype)
#         vtype_sen = True
#     else:
#         print("Invalid input, please try again.")


# vehicle.name = print("Please input the vehicle name")
