from Tkinter import Tk, W, E, FLAT
from ttk import Frame, Button, Label, Style, Entry
import Tkinter

#################### Calculator class ####################
class Calculator(Frame):
    
    def __init__(self, parent):
        # Calling the constructor method of the inherited class.
        Frame.__init__(self, parent)
        
        # Instance variables of the class
        # Root window
        self.parent = parent
        
        # Initialize the window
        self.initUI()
        
        
    # Initialize the UI
    def initUI(self):
        # Set the style of the window
        self.style()
        
        # Set title
        self.parent.title("Calculator")
        
        # Add padding to columns
        for i in range(0, 4):
            self.columnconfigure(i, pad = 3)  
        
        # Add padding to rows
        for i in range(0, 5):
            self.rowconfigure(i, pad = 3)
        
        # Entry widget is where digits are displayed
        entry =  Entry(self)
        
        # Place in first row and span 4 columns. Sticky expands widget in a given direction.
        # In this case from left to right
        entry.grid(row = 0, columnspan = 4, sticky = W + E)
        
        # Clear button, Second row, first column
        clear_button = Button(self, text = "Clr")
        clear_button.grid(row = 1, column = 0)
        
        # Back button
        back_button = Button(self, text = "Back")
        back_button.grid(row = 1, column = 1)
        
        # Empty space that uses the Tkinter button in order to make it flat
        empty = Tkinter.Button(self, relief = FLAT)
        empty.grid(row = 1, column = 2)
        
        # Close button
        close_button = Button(self, text = "Close")
        close_button.grid(row = 1, column = 3)
        
        # 7 button
        seven_button = Button(self, text = "7");
        seven_button.grid(row = 2, column = 0);
        
        # 8 button
        eight_button = Button(self, text = "8");
        eight_button.grid(row = 2, column = 1);
        
        # 9 button
        nine_button = Button(self, text = "9");
        nine_button.grid(row = 2, column = 2);
        
        # Division button
        division_button = Button(self, text = "/");
        division_button.grid(row = 2, column = 3);
        
        # 4 button
        four_button = Button(self, text = "4");
        four_button.grid(row = 3, column = 0);
        
        # 5 button
        five_button = Button(self, text = "5");
        five_button.grid(row = 3, column = 1);
        
        # 6 button
        six_button = Button(self, text = "6");
        six_button.grid(row = 3, column = 2);
        
        # Multiplication button
        multiply_button = Button(self, text = "*");
        multiply_button.grid(row = 3, column = 3);
        
        # 1 button
        one_button = Button(self, text = "1");
        one_button.grid(row = 4, column = 0);
        
        # 2 button
        two_button = Button(self, text = "2");
        two_button.grid(row = 4, column = 1);
        
        # 3 button
        three_button = Button(self, text = "3");
        three_button.grid(row = 4, column = 2);
        
        # Minus button
        minus_button = Button(self, text = "-");
        minus_button.grid(row = 4, column = 3);
        
        # Dot button
        dot_button = Button(self, text = ".");
        dot_button.grid(row = 5, column = 0);
        
        # 0 button
        zero_button = Button(self, text = "0");
        zero_button.grid(row = 5, column = 1);
        
        # Equal button
        equal_button = Button(self, text = "=");
        equal_button.grid(row = 5, column = 2);
        
        # Plus button
        plus_button = Button(self, text = "+");
        plus_button.grid(row = 5, column = 3);
        
                
        # Show the fram widget and gives it an initial size
        self.pack()
        
        
    # Set the style of the window
    def style(self):
        # Configure Button widget with padding and font
        Style().configure("TButton", padding = (0, 5, 0, 5), font = "serif 10")
        
        


#################### Main function ####################
def Main():
    # Main window
    root = Tk()
    
    # Instance of the window
    main_window = Calculator(root)
    
    # Entering mainloop
    main_window.mainloop()
    
    
#################### Run script ####################    
if __name__ == '__main__':
    Main()
