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

    # creating the 2 rackets racket from racket.py and getting it to move
    myRacket1 = Racket(mapping, canvas, Lx, Ly)  # bottom racket
    myRacket1.create_rectangle()
    # canvas.bind("<Button-1>", lambda e: myRacket1.shift_left())
    # canvas.bind("<Button-2>", lambda e: myRacket1.shift_right())


    myRacket2 = Racket(mapping, canvas, Lx, Ly)  # top racket
    myRacket2.create_rectangle(True)
    Racket.change_colour ( myRacket2, "red" )
    canvas.bind("<Button-1>", lambda e: myRacket2.shift_left())
    canvas.bind("<Button-2>", lambda e: myRacket2.shift_right())



    # creating the ball from ball.py
    x0 = 0  # initializing the starting position of the ball
    y0 = myRacket1.mapping.get_ymin() + myRacket1.Ly + width / 120
    # y0 = myRacket2.mapping.get_ymax() - myRacket2.Ly - width/120
    ball1 = Ball(mapping, canvas, x0, y0, velocity=300, theta=45)
    ball1.create_oval()

    # if mapping.get_xmin () < 0 and mapping.get_xmax () > 0:
    #     canvas.create_line ( mapping.get_i ( 0.0 ), mapping.get_j ( mapping.get_ymin () ), mapping.get_i ( 0.0 ),
    #                          mapping.get_j ( mapping.get_ymax () ) )
    # if mapping.get_ymin () < 0 and mapping.get_ymax () > 0:
    #     canvas.create_line ( mapping.get_i ( mapping.get_xmin () ), mapping.get_j ( 0.0 ), mapping.get_i ( mapping.get_xmax () ),
    #                          mapping.get_j ( 0.0 ) )



    ###########################################
    ###### start simulation
    ##########################################
    t = 0  # real time between event
    t_total = 0  # real total time
    count = 0  # rebound_total=0
    while True:
        t = t + 0.01  # real time between events- in second
        t_total = t_total + 0.01  # real total time- in second

        racket1_pos = canvas.coords(myRacket1.rectangle)
        racket2_pos = canvas.coords(myRacket2.rectangle)
        ball_pos = canvas.coords(ball1.circle)

        bottom_bound = (myRacket1.mapping.get_ymin() + myRacket1.Ly + width / 120)
        top_bound = (myRacket1.mapping.get_ymax() - myRacket2.Ly - width / 120)

        # update_xy arguments(time, position bottom boundary, pos_ball, pos_racket, pos Top Boundary, Racket2 pos)
        side = ball1.update_xy(t, bottom_bound, ball_pos, racket1_pos, top_bound, racket2_pos)  # Update ball position and return collision event
        window.update()  # update the graphic (redraw)

        if side != 0:
            t = 0  # reinitialize the local time

        if side == 5:  # shifts control from one ball to another. Here, shifts control from top to bottom
            Racket.change_colour(myRacket2, "black")
            Racket.change_colour(myRacket1, "red")
            canvas.bind("<Button-1>", lambda e: myRacket1.shift_left())
            canvas.bind("<Button-2>", lambda e: myRacket1.shift_right())

        if side == 6:  # control shifts from bottom to top racket
            Racket.change_colour(myRacket1, "black")
            Racket.change_colour(myRacket2, "red")
            canvas.bind("<Button-1>", lambda e: myRacket2.shift_left())
            canvas.bind("<Button-2>", lambda e: myRacket2.shift_right())




        time.sleep(0.01)  # wait 0.01 second (simulation time)
        if side == 1:
            loser = 2
            break

        if side == 2:
            loser = 1
            break  # stop the simulation if it touches the actual bottom of the canvas

    print("Game over for racket %s" % loser)

    window.mainloop()

if __name__ == "__main__":
    main ()