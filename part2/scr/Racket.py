from Mapping_for_Tkinter import Mapping_for_Tkinter
from tkinter import *

class Racket:
    def __init__(self, mapping=None, canvas=None, length=None, width=None):
        self.mapping = mapping
        self.canvas = canvas
        self.Lx = length
        self.Ly = width
        self.pos_x = 0
        self.pos_y = float(mapping.get_ymin() + self.Ly/2)
        # self.pos_y = float(mapping.get_ymax() - self.Ly/2)


    def create_rectangle(self, racket2=False):
        """drawing the racket at the bottom of the canvas"""
        x0 = self.mapping.get_i(-self.Lx/2)
        y0 = self.mapping.get_j(self.pos_y-self.Ly/2)
        x1 = self.mapping.get_i(self.Lx/2)
        y1 = self.mapping.get_j(self.pos_y+self.Ly/2)

        if racket2:  # if there is another racket, getting the new coordinates
            y0 = self.mapping.get_j(float(self.mapping.get_ymax() - self.Ly*1.5/2)-self.Ly/2)
            y1 = self.mapping.get_j(float(self.mapping.get_ymax() - self.Ly*1.5/2)+self.Ly/2)

        self.rectangle = self.canvas.create_rectangle(x0, y0, x1, y1, fill="black")

    def shift_left(self):
        """Moving the racket by few pixels"""
        if self.mapping.get_xmin() != (self.pos_x-self.Lx/2):
            self.pos_x = self.pos_x - self.Lx / 2
            self.canvas.move(self.rectangle, -self.Lx/2, 0)

    def shift_right(self):
        if self.mapping.get_xmax() != (self.pos_x + self.Lx / 2):
            self.pos_x = self.pos_x + self.Lx / 2
            self.canvas.move(self.rectangle, self.Lx / 2, 0)

    def change_colour(self, colour):
        """Changes the color of the racket to indicate which one is playable"""
        self.canvas.itemconfig(self.rectangle, fill=colour)


    """ to complete """


def main():

    ###### create a mapping
    swidth=input("Enter window size in pixels (press Enter for default 600): ")
    if swidth == "":
        width = 600
    else:
        width = int(swidth)

    # instantiate the mapping and the length and breadth of the racket
    mapping = Mapping_for_Tkinter(-width/2, width/2, -width/2, width/2, width)
    Lx = width/10
    Ly = width/60

    ##### create a window, canvas, and racket

    window = Tk()
    canvas = Canvas(window, width=mapping.get_width(), height=mapping.get_height(), bg="white")  # create a canvas width*height
    canvas.pack()
    myRacket = Racket(mapping, canvas, Lx, Ly)
    myRacket.create_rectangle()



    ####### bind mouse click with action
    canvas.bind("<Button-1>", lambda e: myRacket.shift_left())
    canvas.bind( "<Button-2>", lambda e: myRacket.shift_right())


    
    window.mainloop()
if __name__=="__main__":
    main()

