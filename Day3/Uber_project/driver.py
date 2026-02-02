import time
cities={1:"Hyderabad",
            2:"Mumbai",
            3:"Banglore",
            4:"Chennai",
            5:"Delhi"
            }
def displayCity():
    for key,value in cities.items():
        print(f"{key} = {value}")

def cityname(city):
    return cities[city]

def delay():
    time.sleep(1)
    for i in range(3):
        print(". ", end="")
def selectDriver(pickup):
    driver={
            1:"Ravi",
            2:"Ram",
            3:"Raju",
            4:"Srinu",
            5:"John"
            }
    return driver[pickup]

def calcFare(*args):
    sum=1
    for i in args:
        sum*=i
    return sum*243