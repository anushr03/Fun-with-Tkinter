from Mapping_for_Tkinter import Mapping_for_Tkinter
from tkinter import *
from Ball import *
from Racket import *
import random

import math
import time


def main():
    """The main method to run the game"""

    ##### create a mapping
    swidth = input("Enter window size in pixels (press Enter for default 600): ")
    if swidth == "":
        width = 600
    else:
        width = int(swidth)

    # instantiate the mapping and the length and breadth of the racket
    mapping = Mapping_for_Tkinter(-width / 2, width / 2, -width / 2, width / 2, width)
    Lx = width / 10
    Ly = width / 60

    # creating the canvas, window, racket and ball
    window = Tk()
    canvas = Canvas(window, width=mapping.get_width(), height=mapping.get_height(), bg="white" )  # create a canvas width*height
    canvas.pack()

    # creating the racket from racket.py and getting it to move
    myRacket = Racket ( mapping, canvas, Lx, Ly)
    myRacket.create_rectangle ()
    canvas.bind("<Button-1>", lambda e: myRacket.shift_left())
    canvas.bind("<Button-2>", lambda e: myRacket.shift_right())

    # creating the ball from ball.py
    x0 = 0  # initializing the starting position of the ball
    y0 = myRacket.mapping.get_ymin() + myRacket.Ly + width / 120
    ball1 = Ball(mapping, canvas, x0, y0, velocity=200, theta=53)
    ball1.create_oval()

    ###########################################
    ###### start simulation
    ##########################################
    t = 0  # real time between event
    t_total = 0  # real total time
    while True:
        t = t + 0.01  # real time between events- in second
        t_total = t_total + 0.01  # real total time- in second
        racket_pos = canvas.coords(myRacket.rectangle)
        ball_pos = canvas.coords(ball1.circle)

        # update_xy arguments(time, position of new bottom boundary, position of ball, position of racket)
        side = ball1.update_xy(t, myRacket.mapping.get_ymin () + myRacket.Ly + width / 120, ball_pos,racket_pos )  # Update ball position and return collision event
        window.update()  # update the graphic (redraw)

        if side != 0:
            t = 0  # reinitialize the local time

        if side == 1:
            ball1.velocity = ball1.velocity + ball1.velocity * (25 / 100)
            ball1.theta = random.uniform(-170, -10)

        time.sleep(0.01)  # wait 0.01 second (simulation time)
        if side == 2:
            break  # stop the simulation if it touches the actual bottom of the canvas

    print("Game over! Total time: %ss" % t_total)

    window.mainloop()


if __name__ == "__main__":
    main ()




