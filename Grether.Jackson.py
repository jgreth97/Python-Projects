# Jackson Grether
# Section: 006
# Email: Jgtr242@uky.edu
# Date: 10/07/19
#Lab Test 1 
def main():
    totalbill = 0
    basic = 25.75
    reg = 55.75
    prem = 95.75
    sportP = 10
#choice of package
    choice = input("Do you want the basic, regular or premium cable package? (b/r/p) >")
    if choice == 'b':  
        totalbill = 25.75 
    elif choice == 'r':  
        totalbill = 55.75 
         
    elif choice == 'p':  
        totalbill = 95.75 
    else:
        totalbill += 0 
#sports package 
    choice2 = input("Do you want the sports package? y or n >") 
    if choice2 == 'y':
        totalbill += 10
    else: 
        totalbill += 0
#number of devices 
    print("") 
    num_devices = int(input("How many devices do you want to connect?: "))
    if num_devices < 5:
        totalbill += 20
    else:
        totalbill += 0
    print("Your total package would be", totalbill,"$ a month")     
main()
