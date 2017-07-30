'''
Purpose: Python Control Structures and Function Practice
Programmer: Joe Herrera
CS117 Section 1610 CS13-01
Lab 4 Part 1
'''

import math

def main():

    # creating empty list containers
    takeoffAngle = []
    initialVelocity = []
    projectileRange = []

    # initializing variables
    angle = 0.
    velocity = 0.
    gravity = 9.8

    # beginning of for loop
    for i in range(1, 9):
        a = float(input('Enter Takeoff Angle {}: '.format(i)))
        # angle to radians conversion
        angle = a * math.pi / 180.0
        takeoffAngle.append(a)

        velocity = float(input('Enter a value for Initial Velocity {}: '.format(i)))
        initialVelocity.append(velocity)

        pRange = math.sin(2.0 * angle) * velocity ** 2 / gravity

        projectileRange.append(pRange)

    # end of for loop
    print("\nTakeoff Angle\tInitial Velocity\tProjectile Range")
    for i in range(0, len(takeoffAngle)):
        print("{}\t\t\t{}\t\t\t\t{:.2f}".format(takeoffAngle[i], initialVelocity[i], projectileRange[i]))

main()