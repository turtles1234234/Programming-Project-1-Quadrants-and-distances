#Author: Dylan Clark 
#Project Name: Project 1 Quadrants and Distance 
#Date Created: 4/16/24
#Description: Oject Oriented Programming Project
#             

import math

def quadrant_check(p1, p2): #TODO
    if p1 == 0:
        if p2 == 0:
            return "Origin"
        else:
            return "Y-axis"
    elif p2 == 0:
        return "X-axis"
    else:
        if p1 > 0:
            if p2 > 0:
                return "Quadrant I"
            else:
                return "Quadrant IV"
        else:
            if p2 > 0:
                return "Quadrant II"
            else:
                return "Quadrant III"
    
def find_distance(p1, p2): #TODO
    distance = math.sqrt(((p1-0)**2) + ((p2-0)**2))
    return distance

def cont(): #TODO
    user = input("Would you like to continue? (y/n) ")
    if user == "y" or user == "Y":
        main()
    else:
        quit()

def main():

    #TODO
    x = input("Enter the x coordinate: ")
    y = input("Enter the y coordinate: ")
    coordinate = (float(x), float(y))

    #DONE
    print("The point is located in", quadrant_check(int(x), int(y)), coordinate) #Uses the return value of quadrant_check() to print the quadrant
    
    print("The distance from the origin is: ", find_distance(float(x), float(y))) #Uses the return of find_distance to print the distance from origin
    
    cont() #Calls the cont() function to see if the user would like to continue continue the program or end


main() #Only function call. DO NOT CHANGE THIS
