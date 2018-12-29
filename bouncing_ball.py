"""This program is to simulate a bouncing ball. As time advances,
the program will know the acceleration, velocity, and 1d position
of the ball particle, based on the initial conditions. 
The user will be able to set the time intervals to calculate at."""
gravity = -9.81
otherForce = 0
velocity = 9.81
position = 0
time = 0
timeInterval = .01
iterations = 100
changeDefaults = True

def printCurrentInfo():
    print("current gravity: " + str(gravity) + " current velocity: " + str(velocity) + " current position: " + str(position) + " at time: " + str(time))
def askForInput():
    position = float(input("What is the ball's starting position? (m) "))
    if changeDefaults == True:
        gravity = float(input("What is the system's gravity? (kgm/s^2) "))
        timeInterval = float(input("What is the time interval? (s) "))
        velocity = float(input("What is the ball's velocity? (m/s) " ))
        iterations = (float(input("How many seconds to run for? (s) "))/timeInterval)+1

askForInput()
printCurrentInfo()

while iterations > 0:
        position = position + (velocity * timeInterval)
        if position < 0 and velocity < 0:
                velocity = -velocity
        velocity = velocity + (gravity * timeInterval)
        acceleration = gravity + otherForce
        time = time + timeInterval
        iterations = iterations - 1
        if 0 == iterations%10:
                printCurrentInfo()
        

printCurrentInfo()
    




