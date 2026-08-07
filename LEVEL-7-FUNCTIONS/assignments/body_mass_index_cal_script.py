"""
#!/usr/bin/env python3.6

BMI = (weight in kg / height in meters squared)
(if osmebody using imperail system) imperial version:  BMI * 703
"""

def gather_info():
    height = float(input("what is your height? (inches or meters) "))
    weight = float(input("what is your weight? (pounds or kilograms) "))
    system = input("Are your measurements in metric or imperial units? ").lower().strip() 
    return (height, weight, system)

def calculate_bmi(weight, height, system='metric'):
    """
     Return the BODY MASS INDEX (BMI) FOR THE 
     GIVEN WEIGHT, HEIGHT, AND MESURMENT SYSTEM.
    """
    if system == 'metric': 
        bmi = (weight / (height ** 2)) #Bmi formula using imperial units.
    else: 
        bmi = 703 * (weight / (height ** 2)) #703 converts pounds and inches to the standard bmi calculatio.
    return bmi

while True: 
    height, weight, system = gather_info()
    if system.startswith('i'): 
        bmi = calculate_bmi(weight, height=height, system=system)
        print(f"your BMI is {bmi}")
        break
    elif system.startswith('m'):
        bmi = calculate_bmi(weight, height) #already we define defult argument above metric no need to define here 
        print(f"your BMI is {bmi}")
    else: 
        print("ERROR: Unkon Mesurement system. Please use imperial or metric.")
