# Prolog
# Author:  JACKSON GRETHER
# Email:   jtgr@uky.edu
# Section: 006
# Date: 9/9/19 
'''
  Purpose: to find the volume of a sphere given the diameter of the sphere. 
  Preconditions: (input)
    User supplies the diameter as a float number
  Postconditions: (outputs)
    User greeted and prompted for input of the diameter 
    Volume of the sphere displayed with 3 decimal places
  Reference https://m.wikihow.com/Calculate-the-Volume-of-a-Sphere
    and the radius of a sphere is half the diameter

'''
from math import pi

def main():
# Design and implementation

   #  1.  Output a message to identify the program
   
   print("Calculating volume of a sphere\n")
   
   #  2.  Input diameter from user
   diameter = float(input("Enter diameter: "))

   #  3.  Calculate radius from known diameter
   radius =  diameter / 2

   #  4.  Calculate the volume of the sphere
   volume = 4/3 * pi * radius ** 3  #  formula from above reference

   #  5. Output resulting volume and inputs 
   print()
   print("The volume of a sphere with a diameter of", round(diameter,2),
       "and a radius of", round(radius,2), "is", round(volume, 3))

main()
# end of program file
''' 
1. Line 24 was missing semi-colans when tring to print 
2. Syntax Error: invalid syntax: <string>, line 24, pos 27
3. I added quotations between Caculationg volume of sphere\n
4. A semantic error is an error that gives me an undesirable outcomeit
5. The program used the wrong formula to calculate the radius of a square it used 4 * pi ** 3 instead of 3/4 * pi ** 3
6. Turned it into 3/4 instead of 4
'''