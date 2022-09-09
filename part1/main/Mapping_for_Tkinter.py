from tkinter import *
from math import *


class Mapping_for_Tkinter:
    def __init__(self, xmin=None, xmax=None, ymin=None, ymax=None, width=None):  # Constructor
        self.set_xmin(xmin)
        self.set_xmax(xmax)
        self.set_ymin(ymin)
        self.set_ymax(ymax)
        self.set_width(width)
        self.__set_height(self)

    """Setter methods"""
    def set_xmin(self, x1):
        self.__xmin = x1

    def set_xmax(self, x2):
        x1 = self.__xmin
        self.__xmax = x2

        """To check whether the xmin value is not greater than xmax and rectify that accordingly"""
        while True:
            if x2 <= x1:
                x1, x2 = input( "Your xmax is invalid (xmax<=xmin), Re-Enter correct [xmin,xmax]: " ).split()
            else:
                break

        self.__xmin = int(x1)
        self.__xmax = int(x2)

    def set_ymin(self, y1):
        self.__ymin = y1

    def set_ymax(self, y2):
        y1 = self.__ymin
        self.__ymax = y2

        """To check whether the ymin value is not greater than ymax and rectify that accordingly"""
        while True:
            if y2 <= y1:
                y1, y2 = input("Your xmax is invalid (ymax<=ymin), Re-Enter correct [ymin,ymax]: ").split()
            else:
                break

        self.__ymin = int(y1)
        self.__ymax = int(y2)

    def set_width(self,w):
        self.__width = w

    def __set_height(self,h):
        self.__height = int(self.__width * ((self.__ymax-self.__ymin)/(self.__xmax-self.__xmin)))

    """Getter Methods"""
    def get_xmin(self):
        return self.__xmin

    def get_xmax(self):
        return self.__xmax

    def get_ymin(self):
        return self.__ymin

    def get_ymax(self):
        return self.__ymax

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    """Str Method"""
    def __str__(self):
        result = "xmin=%s, xmax=%s, ymin=%s, ymax=%s, width=%s, Height=%s" % (self.__xmin, self.__xmax, self.__ymin, self.__ymax, self.__width, self.__height)
        return result

    """Instance methods"""
    def get_x(self, i):
        """Takes the tkinter Input and returns the corresponding value in coordinate system"""
        x = i * (self.__xmax - self.__xmin) / (self.__width - 1) + self.__xmin
        return x

    def get_y(self, j):
        y = j * (self.__ymin - self.__ymax) / (self.__height - 1) + self.__ymax
        return y

    def get_i(self, x):
        """Takes the Coordinate Input and returns the corresponding value in Tkinter"""
        min = 0
        max = self.__xmax - self.__xmin
        temp = x - self.__xmin

        i = float(temp/max) * (self.__width - 1)
        return int(i)

    def get_j(self, y):
        min = 0
        max = self.__ymin - self.__ymax
        temp = y - self.__ymax
        j = float(temp / (max - min)) * (self.__height - 1)
        return int(j)



""" to complete"""


def main(): 
    """ TESTING MAPPING using FUNCTION PLOTTER """

    #### formula input
    formula=input("Enter math formula (using x variable): ")

    #### coordinate input
    coord=input("Enter xmin,xmax,ymin,ymax (press Enter for default -5,5,-5,5): ")
    if coord == "":
        xmin, xmax = -5, 5
        ymin, ymax = -5, 5
    else:
        # split the string/create list of string
        xmin, xmax, ymin, ymax = coord.split()

    #### instantiate a mapping
    width = 800
    m = Mapping_for_Tkinter(float(xmin), float(xmax), float(ymin), float(ymax), width)
    print(m)  # print info about object

    #### instantiate a tkinter window
    window = Tk()
    canvas = Canvas(window, width=m.get_width(),height=m.get_height(),bg="white") # create a canvas width*height
    canvas.pack()

    #### create axis
    if m.get_xmin()<0 and m.get_xmax()>0:
        canvas.create_line(m.get_i(0.0),m.get_j(m.get_ymin()),m.get_i(0.0),m.get_j(m.get_ymax()))
    if m.get_ymin()<0 and m.get_ymax()>0:
        canvas.create_line(m.get_i(m.get_xmin()),m.get_j(0.0),m.get_i(m.get_xmax()),m.get_j(0.0))



    #### plot function
    for i in range(width):
        x=m.get_x(i)
        y = eval(formula)
        canvas.create_rectangle((m.get_i(x),m.get_j(y))*2,outline="blue")

    window.mainloop() # wait until the window is closed



if __name__=="__main__":
    main()
