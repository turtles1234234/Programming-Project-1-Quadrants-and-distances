#Author: Dylan Clark 
#Project Name: Project 1 Quadrants and Distance 
#Date Created: 4/16/24
#Description: Oject Oriented Programming Project
         
#Imports MATH
import math 

def quadrant_check(p1, p2): #Checks where the coordinate is
    if p1 == 0:    
        if p2 == 0:     #Checks if the coordinate's on the origin or the Y-axis
            return "Origin"
        else:           #Checks if the coordinate is on the Y-axis
            return "Y-axis"
    elif p2 == 0:       #Checks if the coordinate's on the X-axis
        return "X-axis"
    else:
        if p1 > 0:  
            if p2 > 0:  #Checks if the coordinates in the First Quadrant
                return "Quadrant I"
            else:       #Checks is the coordinates in the Fourth Quadrant
                return "Quadrant IV"
        else:
            if p2 > 0:  #Checks if the coordinate is in the Second Quadrant
                return "Quadrant II"
            else:       #Checks if the coordinate is in the Third Quadrant
                return "Quadrant III"
    
def find_distance(p1, p2): #Finds the distance from the origin using the distance formula
    distance = math.sqrt(((p1-0)**2) + ((p2-0)**2))
    return distance

def cont(): #Asks the user if they would like to continue
    user = input("Would you like to continue? (y/n) ") 
    if user == "y" or user == "Y":
        main()  #continue
    else:
        quit() # doesn't continue or quits the program

def main():

    #Takes the users input of X and Y
    x = input("Enter the x coordinate: ") 
    y = input("Enter the y coordinate: ")
    coordinate = (float(x), float(y)) #gets the coordinate from the users input

    #DONE
    print("The point is located in", quadrant_check(int(x), int(y)), coordinate) #Uses the return value of quadrant_check() to print the quadrant
    
    print("The distance from the origin is: ", find_distance(float(x), float(y))) #Uses the return of find_distance to print the distance from origin
    
    cont() #Calls the cont() function to see if the user would like to continue continue the program or end


main() #Only function call. DO NOT CHANGE THIS
