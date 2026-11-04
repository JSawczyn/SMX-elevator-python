#!/usr/bin/env python3
import sys

""" Simulate an elevator traveling between floors
    The Executable Script will accept user input for an elevator, starting floor
    and floors to be traveled, and print floors traveled to the console.
    Accept arguments at command line execution when running the script """

# Program Constant - Travel Time between floors 10 seconds
TRAVEL_TIME = 10
# Set default starting floor of 1
STARTING_FLOOR = 1

## Inputs: [list of floors to visit] (e.g. elevator start=12 floor=2,9,1,32)
## Outputs: [total travel time, floors visited in order] (e.g. 560 12,2,9,1,32)
## Program Constants: Single floor travel time: 10

def main() -> None:

    # assume that this script runs and accepts user input
    # assume input passed as command line arguments, accept input as expected command line arguments
    # want to be able to accept multiple arguments, passed as series of positive integer numbers, so that running 'python main.py 12 2 9 1 32' works
    # or also, accept arguments with labels and spaces, so running 'python main.py elevator start=12 floor=2,9,1,32' works too
    # if the user entered negative numerical values, then the script will ignore the negative denotation and treat the numbers as possitive integers, example '-10' is parsed, ignoring the '-' symbol and treated as '10'
    # also fractional and decimal values are ignored, value of '10.5' would be parsed as '10' and '5' respectively thus treateds as two seperate floors to visit

    if len(sys.argv) <= 1:
        print("Error, no arguments passed. Please pass starting floor and floors to visit as command line arguments. \n Execute Script on command line as: 'python main.py 12 2 9 1 32' or 'python main.py elevator start=12 floor=2,9,1,32', \n Arguments accepted as individual numbers or as labeled comma seperated lists")
        exit()
    # assume user must pass in arguments when running script from command line
    # if they do not pass in any arguments, script fails to execute / exit script

    # parse through scripts arguments, look for numerical values
    # ignore alphabetic characters and seperate on commas and spaces
    # store the found numerical characters as a list of the floors to visit
    # assume first floor is starting floor
    floorNumbers = []
    floorsVisited = []
    digits = ""
    # account for first argument being script name, system argument list includes script name as first argument, arg(0) -- start at arg(1) to ignore script name
    # subtract 1 from arg().length to get true number of user input arguments
    for argument in sys.argv[1:]:
        # for each argument passed
        for char in argument + " ":
            # for each character in the argument and add scape to ensure last numerical value captured
            ## print(f"Checking character: {char}")
            if char.isdigit():
                # check each character, if it is a digit, then add to running string of digits
                ## print(f"Found digit: {char}")
                digits = digits + char
                ## print(f"Current digits: {digits}")
            elif char == "," or char == "." or char == " " or char.isalpha():
                # else if characters is not a digit, then check if it is a comma or decimal or space or alphabetic character
                # if it is so then, add the running string of digits to the list of floor numbers if it is not empty
                if digits != "":
                    floorNumbers.append(int(digits))
                    # then reset the running string of digits to empty
                    digits = ""

    ## print(f"Floor Numbers: {floorNumbers}")

    # now have list of floors to visit, assuming first floor in list is the starting floor
    # and to visit the rest of the floors in order in list

    # set total time traveled to zzero
    total_travel_time = 0
    # set starting floor to the first value in the list of floors to visit
    start_floor = floorNumbers[0]
    # set current floor to the starting floor
    current_floor = start_floor

    ## print(f"Starting Floor: {start_floor}")
    for floorNumbers in floorNumbers:
        # set target floor to the currectn value of floor in the list of floors to visit
        target_floor = floorNumbers
        ## print(f"Floor to visit: {target_floor}")

        # calculate travel time between current floor and target and add to running total of travel time
        travel_time = abs(target_floor - current_floor) * TRAVEL_TIME
        ## print(f"Travel Time from Floor {current_floor} to Floor {target_floor}: {travel_time} seconds")
        total_travel_time += travel_time
        ## print(f"Total Travel Time so far: {total_travel_time} seconds")
        # keep track of floors visisted in order
        floorsVisited.append(target_floor)
        # set current floor to previous target floor for next iteration of the loop
        current_floor = target_floor
        ## print(f"Current Floor after visiting: {current_floor}")

    ## print(f"Total Travel Time in seconds: {total_travel_time} seconds")
    ## print(f"Floors Visited in Order: {floorsVisited}")
    print(total_travel_time, floorsVisited)


    #####
    ### Unimplemented Feature: Handle edge cases for specific user inputs
    #####
    # need to handle fractional or decimal values
    # need to handle negative values
    # need to handle other special edge cases

    #####
    ### Unimplemented Feature: Interactive Mode for the Program
    #####
    # What if the elevator script is an interactive program?
    # execute the script with no arguments or parameters given at command line
    # And instead it prompts the user for input
    # Initial prompt for a starting floor, or assume Starting Floor 1
    # Then prompt the user for target floor (one at a time) to travel to
    # loop, providing travel time each iteration for floor
    # and continue until user choices to quit/exit
    # print("Elevator Project Enter Numerical Value for Starting Floor. \n Type 'quit' or 'exit' to stop executable script")
    # while True:
    #     try:
    #       user_input = input("> ")
    #     except EOFError:
    #       print()
    #       break
    #     if user_input.strip().lower() in {"quit", "exit"}:
    #       break
    #     print(f"Output: {user_input}")

if __name__ == "__main__":
    main()

