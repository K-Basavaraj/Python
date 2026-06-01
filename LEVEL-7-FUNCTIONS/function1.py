################### FUNCTIONS #####################
#function with Single paramenter
def greeting(name):
    print("welcome: "+ name)

greeting("Basavaraj") #welcome: Basavaraj

#function with multiple parameters
def greetings(name, department):
    print("welcome, " + name)
    print("your part of " + department + ".")

greetings("Basavaraja", "DevOpsEngineer")
greetings("tyrion Lanister", "SoftwareEngineer")

"""
welcome, Basavaraja
your part of DevOpsEngineer.
welcome, tyrion Lanister
your part of SoftwareEngineer.
"""

