from Mapping_for_Tkinter import Mapping_for_Tkinter
from tkinter import *
import math
import time
import random

class Ball:
    def __init__(self, mapping, canvas, x0, y0, velocity, theta):  # Constructor
        self.mapping = mapping
        self.canvas = canvas
        self.x0 = x0
        self.y0 = y0
        self.velocity = int(velocity)
        self.theta = math.radians(int(theta))
        self.x = x0
        self.y = y0
        self.R = mapping.get_width()/120

    def create_oval(self):
        """Creating a circle with 4 coordinatees"""
        x0 = self.mapping.get_i(self.x0-self.R)
        x1 = self.mapping.get_i(self.x0+self.R)
        y0 = self.mapping.get_j(self.y0-self.R)
        y1 = self.mapping.get_j(self.y0+self.R)

        self.circle = self.canvas.create_oval(x0, y0, x1, y1, fill="blue")


    def update_xy(self, t, bot_bound=None, ball_pos=[], racket1_pos=[], top_bound=None, racket2_pos=[]):
        self.x = float(self.x0 + self.velocity * math.cos(self.theta) * t)
        self.y = float(self.y0 + self.velocity * math.sin(self.theta) * t)
        side = 0

        # left boundary
        if self.x <= self.mapping.get_xmin() + self.R:
            self.x = self.mapping.get_xmin() + self.R
            self.x0 = self.x
            self.y0 = self.y
            self.theta = math.pi - self.theta
            side = 3

        # right boundary
        if self.x >= self.mapping.get_xmax() - self.R:
            self.x = self.mapping.get_xmax() - self.R
            self.x0 = self.x
            self.y0 = self.y
            self.theta = math.pi - self.theta
            side = 4

        """Top boundary"""

        # if a top racket is present
        if top_bound:
            if self.y >= self.mapping.get_ymax() - self.R:
                side = 1
            if self.y >= top_bound:
                if ball_pos[2] >= racket2_pos[0] and ball_pos[0] <= racket2_pos[2]:
                    if racket2_pos[1] <= ball_pos[1] <= racket2_pos[3]:
                        self.y = top_bound
                        self.x0 = self.x
                        self.y0 = self.y
                        self.theta = random.uniform(-170, -10)
                        self.theta = -self.theta
                        side = 5  # if it bounces off the racket

        # if a top racket is not present
        else:
            if self.y >= self.mapping.get_ymax() - self.R:
                self.y = self.mapping.get_ymax() - self.R
                self.x0 = self.x
                self.y0 = self.y
                self.theta = - self.theta
                side = 1

        """Bottom Boundary"""
        # If there is a bottom racket, this snipet of code will take place
        if bot_bound:
            if self.y <= self.mapping.get_ymin() + self.R:
                side = 2

            if self.y <= bot_bound:
                # compares the position of ball and racket and then rebounds if in range of the racket
                # using the coords function to find the position of both the racket and the ball
                if ball_pos[2] >= racket1_pos[0] and ball_pos[0] <= racket1_pos[2]:
                    if racket1_pos[1] <= ball_pos[3] <= racket1_pos[3]:
                        self.y = bot_bound
                        self.x0 = self.x
                        self.y0 = self.y
                        self.theta = random.uniform(10, 170)
                        self.theta = -self.theta
                        side = 6

        # if no racket is present
        else:
            if self.y <= self.mapping.get_ymin() + self.R:
                self.y = self.mapping.get_ymin() + self.R
                self.x0 = self.x
                self.y0 = self.y
                self.theta = -self.theta
                side = 2


        x0 = self.mapping.get_i(self.x - self.R)
        y0 = self.mapping.get_j(self.y - self.R)
        x1 = self.mapping.get_i(self.x + self.R)
        y1 = self.mapping.get_j(self.y + self.R)

        self.canvas.coords(self.circle, x0, y0, x1, y1)
        return side



    # def update_xy(self, t):
    #     """Moving the ball in random direction according to the specified velocity"""
    #
    #     self.x = self.x0 + self.velocity * math.cos(self.theta) * t
    #     self.y = self.y0 + self.velocity * math.sin(self.theta) * t
    #
    #     # checking for boundary hit and changing the values of self.x and self.y accordingly
    #
    #     if self.x <= (self.mapping.get_xmin()+self.R):  # the ball touches the left boundary of the canvas
    #         self.theta = math.pi - self.theta
    #         self.x0 = self.x
    #         self.y0 = self.y
    #         return 3
    #
    #     if self.x >= (self.mapping.get_xmax()-self.R): # the ball touched the right boundary
    #         self.theta = math.pi - self.theta
    #         self.x0 = self.x
    #         self.y0 = self.y
    #         return 4
    #
    #     if self.y >= (self.mapping.get_ymax()-self.R):  # the ball touches the top boundary
    #         self.theta = - self.theta
    #         self.x0 = self.x
    #         self.y0 = self.y
    #         return 1
    #
    #     if self.y <= (self.mapping.get_ymin()+self.R): # the ball touched the bottom boundary
    #         self.theta = - self.theta
    #         self.x0 = self.x
    #         self.y0 = self.y
    #         return 2
    #
    #     x0 = self.mapping.get_i(self.x) - (self.mapping.get_width() / 120)
    #     y0 = self.mapping.get_j(self.y) - (self.mapping.get_height() / 120)
    #     x1 = self.mapping.get_i(self.x) + (self.mapping.get_width() / 120)
    #     y1 = self.mapping.get_j(self.y) + (self.mapping.get_height() / 120)
    #
    #     self.canvas.coords(self.circle, x0, y0, x1, y1)
    #     return 0



def main(): 
        ##### create a mapping
        swidth = input("Enter window size in pixels (press Enter for default 600): ")
        if swidth == "":
            width = 600
        else:
            width = int(swidth)

        # instantiate the mapping and the length and breadth of the racket
        mapping = Mapping_for_Tkinter(-width / 2, width / 2, -width / 2, width / 2, width)
        
        
        ##### User Input 
        data = input("Enter velocity and theta (press Enter for default: 500 pixel/s and 30 degree):")
        if data == "":
            velocity = 500
            theta = 30
        else:
            velocity, theta = data.split()

        
        ##### create a window, canvas and ball object

        root = Tk()
        canvas = Canvas(root, width=mapping.get_width(), height=mapping.get_height(), bg="white")  # create a canvas width*height
        canvas.pack()
        ball1 = Ball(mapping, canvas, 0, 0, velocity, theta)
        ball1.create_oval()


        ###########################################
        ###### start simulation
        ###########################################
        t = 0               # real time between event
        t_total = 0         # real total time
        count = 0           # rebound_total=0
        while True:
            t = t+0.01  # real time between events- in second
            t_total = t_total + 0.01  # real total time- in second
            side = ball1.update_xy(t)  # Update ball position and return collision event
            root.update()   # update the graphic (redraw)
            if side != 0:
                count = count+1  # increment the number of rebounds
                t = 0  # reinitialize the local time
            time.sleep(0.01)  # wait 0.01 second (simulation time)
            if count == 10:
                break  # stop the simulation

        print("Total time: %ss" % t_total)
        root.mainloop()  # wait until the window is closed
        

if __name__=="__main__":
    main()

