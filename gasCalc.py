# gasCalc.py

def fuelConversion(fuel):
    g = 3.785411784   # liters per gallon
    m = 1609.344    # meters per mile
    kpg = (g / m * 1000)    # kilometers per gallon
    return  100 / fuel * kpg    # returns fuel as mpg to l/100km or vice versa
    
