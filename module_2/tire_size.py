from math import pi

"""For Carla, that could mean doing the following every time she "wakes up":

Measure the distance between herself and an object directly behind her.
Turn her wheels exactly one full rotation.
Make the same distance measurement again.
Use the measurements from 1 and 3 to calculate the distance traveled. This is the current circumference of her tires.
Perform the appropriate math to compute the current diameter of her tires.
Unfortunately, Carla has a bug in the code that performs steps 4 and 5! Help Carla drive by finding and fixing the bug"""

def get_tire_diameter(dist_before_turn, dist_after_turn):
    # TODO - there's a bug in this function! Find and fix it!

    circumference = dist_after_turn - dist_before_turn
    diameter = circumference * pi
    return diameter