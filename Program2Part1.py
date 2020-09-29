'''
Name: Jackson Grether
Email: jtgr242@uky.edu
Date: 11-13-19
Section: 006


Purpose: allow a user to tag a balloon with a paint ball gun
Pre-conditions:  difficulty (integer between 1 and 10, inclusive, validated)
velocity (meters) (float) and angle (degrees) (float)
Post-conditions:  user sees their name on the card
'''

#need math library - trig functions
import math
#need random library - randint, seed functions
import random
#seed function
random.seed(78)

#set global gravity constant as 9.81 
#meters per second per second - surface of the Earth
gravity = 9.81
def main():
        come_play = 1 
        shot_number = 1
        #Intro and instructions
        print("\nBalloons!")
        print("\nYou are shooting at a balloon which is 100 meters away.")
        print("But its altitude is random, between 0 and 400 meters above the ground.")
        print("\nDifficulty goes from 1 to 10, 1 being hard, 10 being easy")
        #level select
        level = int(input("What level do you want? (1-10): "))
        
        while level < 1 or level > 10:
                print("Select a level in the range of 1-10 please")
                level = int(input("What level do you want? (1-10): "))
        #get andom int for height of balloon
        height_of_balloon = random.randint(0,401)
        #print altitude
        print("\nThe balloon's altitude is",height_of_balloon,"meters")
        #print shot number
        print("Shot number: ",shot_number)
        '''
        Traveled
        purpose: calculate the distance traveled by a projectile that is
        fired with a given velocity at a given angle of elevation
    
        pre-conditions:  velocity and angle are both floats
        velocity in meters per second, angle in radians
        Uses a GLOBAL constant, for acceleration due to gravity, float
    
        post-conditions:  returns the distance as a float
        '''
        #loop come_play
        while come_play in range(1,28,2):
                def distance_traveled(velocity,radians):
                        distance = (velocity**2)*(math.sin(2*radians))/gravity
                        return(distance)
                velocity = float(input("What velocity do you want to shoot at (m/s): "))
                angle = float(input("What angle from the ground do you want to shoot at (degrees): "))
                radians = math.radians(angle)
                distance = (velocity**2)*(math.sin(2*radians))/gravity
                print('Your shot traveled', round(distance_traveled(velocity,radians),0),"meters")
                '''
                Max Height
                purpose: calculate the maximum height reached by a projectile that is
                fired with a given velocity at a given angle of elevation
                
                pre-conditions:  velocity and angle are both floats
                velocity in meters per second, angle in radians
                Uses a GLOBAL constant, for acceleration due to gravity, float
        
                post-conditions: returns the maximum height as a float
                '''
                #Useful in Phase II
                def height(max_height):
                        velocity = distance_traveled(velocity,radians)
                        radians = distance_traveled(velocity,radians)
                        return(max_height)
                max_height = ((velocity**2)*(math.sin(radians))**2/(2*gravity))
                #print("You missed the balloon by",round((balloon_height-max_height),0),"meters")
                print("At the distance to the balloon, 100 meters, your shot was at", round(max_height,0),"meters")
                '''
                Altitude
        
                Purpose:
                This function calculates the altitude the paint ball will be at when 
                it reaches the balloon's location (distance) if launched at given
                velocity and angle.
        
                Pre-conditions:
                Velocity is in meters per second the paint ball is fired
                Angle is in radians, the angle the paint ball is launched at (from the ground)
                Distance is in meters that the user is from the balloon
                All are floats
        
                Post-conditions:
                It returns the altitude as a float.
                '''
                def altitude (altitude_of_ball):
                        distance = distance_traveled(velocity,radians)
                        radians = distance_traveled(velocity,radians)
                        return(altitude_of_ball)
                altitude_of_ball = distance * math.tan(radians) - gravity / (2 * velocity ** 2 * math.cos(radians) ** 2) * distance ** 2
                #enter velocity until they hit it or they give up
                #if the altitude of ball is balloon height, they hit the target 
                if altitude_of_ball == height_of_balloon:
                        print("You hit the balloon!\nGame over!")
                        print("\nYou took",shot_number,"shots at the balloon")
                #else, they missed the balloon 
                else:
                        print("You missed the balloon by",round(height_of_balloon - max_height,0),"meters")
                        answer = str(input("Do you want another shot at him? y or n: "))
                        #do they want to play again
                        if answer !="y" and answer !="n":
                                print("please enter y or n")
                                answer = str("Do you want another shot at him? y or n: ")
                        #either way shot count is updated and reported
                        #if no game is over, if yes game is continued starting at
                        if answer == "n":
                                shot_number += 1
                                print("You took",shot_number,"shots at the balloon")
                                come_play += 1
                        if answer == "y":
                                shot_number += 1
                                print("Shot number",shot_number)
                                come_play += 2
#main()                                
main()
'''
Test Cases

9.
10.
11.
12.
13.
14.   
'''