'''
Program 1
Purpose: calculate the orbital velocity, acceleration, and period of a
 satellite orbiting the earth, given the altitude of the satellite above
 the Earth's surface.
Pre-conditions: user input of altitude, as a float, greater than 1 km
Post-conditions: title, prompt for altitude, velocity, acceleration, period
  error message if altitude is less than or equal to 1 km, value replaced
  with 2 km

'''
import math
def main():
#   display title and author
    print("Program 1 by Jackson Grether and Gabriel Jarema") 
#   input the altitude in kilometers (float)
    alt = float(input("Enter the altitude in km: "))
#   if altitude less than or equal to 1 km, 
#         tell user this is too small, replace altitude with 2 (km)
# Worked on by Jackson and Gabe
    if alt <= 1:
        alt = 2
        print("Too low, using 2 km")
#   set up two variables for given constants
    rad_of_e = 6378.1370
    gm_of_e = 3.986005e14
#   calculate radius of the orbit by adding Earth's radius and altitude 
#     and convert to meters.  (times 1000)
    rad_of_o = ((rad_of_e + alt) * 1000)
#   calculate the velocity, acceleration and period using formulas given
#   convert period in seconds to minutes by dividing by 60 
#   convert period in minutes to hours by dividing by 60
# Math and code by Jackson, Debugging by Gabe 
    velocity = (math.sqrt(gm_of_e / rad_of_o))
    period = ((4 * math.pi**2) * rad_of_o**3) / gm_of_e 
    period2 = math.sqrt(period) 
    periodmin = period2 / 60
    periodhours = periodmin / 60
    accel = gm_of_e / (rad_of_o**2) 
#   output blank line
    print("")
#   output value of velocity, rounded to 3 places, with units mps
#   output value of acceleration, rounded to 3 places, with units mps^2
#   output value of period, rounded to 3)) 
# Code by Jackson,Debugging by Gabe
    print("Velocity: ",round(velocity,3),"mps")
    print("Acceleration: ",round(accel,3),"mps^2")
    print("Period in seconds: ",round(period2,3),"seconds")
    print("Period in minutes: ",round(periodmin,3),"minutes")
    print("Period in hours: ",round(periodhours,3),"hours")
main()
#TEST CASES
'''
A. velocity 7.85e3 m/s (7.84 also ok)
B. acceleration 9.53 m/s^2 (9.50 also ok)
C. period 5176 sec = 86.484 min = 1.44 hours (5189.0 sec = 86.48 min = 1.44 hr)
D. velocity 1013.908 mps
E. acceleration 0.003 m/s^2
F. period 2402823.428 sec = 40047.057 min = 667.451 hours
G. velocity 3,071.603 mps
H. acceleration 0.223 m/s^2
I. period 86421.598 sec = 1440.36 min = 24.006 hours
J. velocity 7,904.125 mps
K. acceleration 9.792 m/s^2
L. period 5071.73 sec = 84.529 min = 1.4088 hours
M. message "too low, using 2 km" and then the answers are the same as J,K,L (can either repeat the numbers or just say that it's the same as the previous test case)
'''
