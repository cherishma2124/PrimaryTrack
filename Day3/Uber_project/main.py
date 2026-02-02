#build an uber application, 
# search for location, city, select city as input from user, assign driver from system, status waiting, starting drive, fare: 
# conform booking, once drive is completed, status need to be updated to completed, generate invoice:driver, city,fare
#driver info, confirmation, booking ride, data, main program

import driver
import invoice
import time

name=input("Enter Name:")
phnum=input("Enter Phone Number:")
maskedphnum=phnum[2]+"******"+phnum[-2:]

driver.displayCity()

pickup=int(input("Select Pickup Location:"))
drop=int(input("Select Dropoff Location:"))


fare=driver.calcFare(pickup+1,drop+1)
print(f"Fare is: {fare}")


confirm=input("Do you want to confirm your ride (Y/N): ")

if confirm == "N":
    print("Ride is cancelled")

else :
        
    print(f"Your booking status is confirmed")
    time.sleep(1)
    print("\nDriver is being assigned")
    driver.delay()
    print(f"\nDriver {driver.selectDriver(pickup)} is assigned for your ride!")

    print("Please enjoy your ride!")

    list=invoice.getInvoice(Name=name.title().strip(), PhoneNumber= maskedphnum,Source=driver.cityname(pickup), Destination=driver.cityname(drop), Fare=fare)
    print("\n-----INVOICE-----")
    for i in list:
        print(i)