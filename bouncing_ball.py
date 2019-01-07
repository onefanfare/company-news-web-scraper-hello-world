"""This program is to simulate a bouncing ball. As time advances,
the program will know the acceleration, velocity, and 1d position
of the ball particle, based on the initial conditions. 
The user will be able to set the time intervals to calculate at."""
import time
import os

changeDefaults = True
class Ball():
        """A simple ball"""
        def __init__(self, position, velocity, mass, radius):
                self.position = position
                self.velocity = velocity
                self.mass = mass
                self.radius = radius


class Environment():
        def __init__(self, gravity, time, timeInterval, iterations, my_ball):
                self.gravity = gravity
                self.time = time
                self.timeInterval = timeInterval
                self.iterations = iterations
        


my_ball = Ball(0,10,1,1)
my_environment = Environment(-10, 0, .01, 100, my_ball)


def askForInput():
    my_ball.position = float(input("What is the ball's starting position? (m) "))
    if changeDefaults == True:
        my_environment.gravity = float(input("What is the Environment's gravity? (kgm/s^2) "))
        my_environment.timeInterval = float(input("What is the time interval? (s) "))
        my_ball.velocity = float(input("What is the ball's velocity? (m/s) " ))
        my_environment.iterations = (float(input("How many seconds to run for? (s) "))/my_environment.timeInterval)+1

def printCurrentInfo():
    print("current gravity: " + str(my_environment.gravity) + " current velocity: " + str(my_ball.velocity) + " current position: " + str(my_ball.position) + " at time: " + str(my_environment.time))

def printGraph():
        os.system('cls')
        n = 26
        while my_ball.position - n < 0:
                if n % 5 == 0:
                        print("| ", n)
                else:
                        print("|")
                n = n - 1
        print("o")
        n = n - 1
        while n > 0:
                if n % 5 == 0:
                        print("| ", n)
                else:
                        print("|")
                n = n - 1
        print("--0")
        time.sleep(.1)

def runEnvironment():
        while my_environment.iterations > 0:
                if my_environment.iterations%10 == 0:
                        printGraph()
                my_environment.time = my_environment.time + my_environment.timeInterval
                my_environment.iterations = my_environment.iterations - 1
                my_ball.position = my_ball.position + my_ball.velocity*my_environment.timeInterval
                my_ball.velocity = my_ball.velocity + my_environment.gravity*my_environment.timeInterval
                if my_ball.position < 0 and my_ball.velocity < 0:
                        my_ball.velocity = -my_ball.velocity
                

        



askForInput()
printCurrentInfo()
runEnvironment()


        



