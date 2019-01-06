"""This program is to simulate a bouncing ball. As time advances,
the program will know the acceleration, velocity, and 1d position
of the ball particle, based on the initial conditions. 
The user will be able to set the time intervals to calculate at."""

changeDefaults = True
class Ball():
        """A simple ball"""
        def __init__(self, position, velocity, mass, radius):
                self.position = position
                self.velocity = velocity
                self.mass = mass
                self.radius = radius


class System():
        def __init__(self, gravity, time, timeInterval, iterations, my_ball):
                self.gravity = gravity
                self.time = time
                self.timeInterval = timeInterval
                self.iterations = iterations
        def bounce():
                if (my_ball.position - my_ball.radius) < 0 and my_ball.velocity < 0:
                        my_ball.velocity = -my_ball.velocity
        def iterate():
                bounce()
                my_ball.position = my_ball.position + (timeInterval*my_ball.velocity)
                my_ball.velocity = my_ball.velocity + (timeInterval*gravity)
        def run_simulation():
                while self.iterations > 0:
                        my_ball.iterate()
                        if self.iterations%10 == 0:
                                printCurrentInfo()
                        self.iterations = iterations - 1
                self.time = self.time + timeInterval
        


my_ball = Ball(0,10,1,1)
my_system = System(-10, 0, .01, 100, my_ball)


def askForInput():
    my_ball.position = float(input("What is the ball's starting position? (m) "))
    if changeDefaults == True:
        my_system.gravity = float(input("What is the system's gravity? (kgm/s^2) "))
        my_system.timeInterval = float(input("What is the time interval? (s) "))
        my_ball.velocity = float(input("What is the ball's velocity? (m/s) " ))
        my_system.iterations = (float(input("How many seconds to run for? (s) "))/my_system.timeInterval)+1

def printCurrentInfo():
    print("current gravity: " + str(my_system.gravity) + " current velocity: " + str(my_ball.velocity) + " current position: " + str(my_ball.position) + " at time: " + str(my_system.time))

def runSystem():
        while my_system.iterations > 0:
                if my_system.iterations%10 == 0:
                        printCurrentInfo()
                my_system.time = my_system.time + my_system.timeInterval
                my_system.iterations = my_system.iterations - 1
                my_ball.position = my_ball.position + my_ball.velocity*my_system.timeInterval
                my_ball.velocity = my_ball.velocity + my_system.gravity*my_system.timeInterval
                if my_ball.position < 0 and my_ball.velocity < 0:
                        my_ball.velocity = -my_ball.velocity
                


askForInput()
printCurrentInfo()
runSystem()


        



