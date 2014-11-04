from Tkinter import *

# Creating the window for the calculator
window = Tk()
# Creating the canvas
canvas = Canvas(window, width = 515, height = 515)
# Organizes widgets in a table-like structure in the parent widget.
canvas.grid(row = 0, column = 0)
# Bring the application up to date by invoking idel callbacks
canvas.update_idletasks()
# Set title
window.title("Calculator")
# Avoid resizing the window
window.resizable(width = False, height = False)
#calc = calculator()
