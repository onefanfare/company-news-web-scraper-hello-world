"""This program is to simulate a bouncing ball. As time advances,
the program will know the acceleration, velocity, and 1d position
of the ball particle, based on the initial conditions. 
The user will be able to set the time intervals to calculate at."""
float gravity = -9.81
float velocity = 0
float position = 0
float time = 0
float timeInterval = .01
int iterations = 100
bool changeDefaults = False

def printCurrentInfo():
    print("current gravity: " + gravity + " current velocity: " + " current position: " + position + " at time: " + time)

def askForInput():
    position = float(input("What is the ball's starting position? (m) "))
    if changeDefaults = true:
        gravity = float(input("What is the system's gravity? (kgm/s^2) "))
        timeInterval = float(input("What is the time interval? (s) "))
        velocity = float(input("What is the ball's velocity? (m/s) " ))
        iterations = (float(input("How many seconds to run for? (s) "))/timeInterval)+1

askForInput()
printCurrentInfo()


    




