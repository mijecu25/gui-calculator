from Tkinter import *

# Main class
class calculator():
    # Constructor
    def __init__(self):
        # Running total
        self.total = 0
        # Input from the user
        self.input = ""


#calc = calculator()
window = Tk()
canvas = Canvas(window, width = 515, height = 515)
canvas.grid(row = 0, column = 0)
canvas.update_idletasks()


        
