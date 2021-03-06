from Tkinter import Tk, W, E, FLAT, RIGHT, END
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
        
        # Running total 
        self.current_total = 0
        
        # Current number
        self.current_num = 0
        
        # Current operation
        # 0 -> None
        # 1 -> Add
        # 2 -> Substract
        # 3 -> Multiply
        # 4 -> Divide
        self.operation = 0
        
        self.max_operations = 4
                
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
        entry = Entry(self, justify = RIGHT)
        self.clear(entry)
        
        # Place in first row and span 4 columns. Sticky expands widget in a given direction.
        # In this case from left to right
        entry.grid(row = 0, columnspan = 4, sticky = W + E)
                
        # Clear button, Second row, first column
        clear_button = Button(self, text = "Clr", command = lambda: self.clear(entry))
        clear_button.grid(row = 1, column = 0)
        
        # Back button
        back_button = Button(self, text = "Back", command = lambda: self.back(entry))
        back_button.grid(row = 1, column = 1)
        
        # Empty space that uses the Tkinter button in order to make it flat
        empty = Tkinter.Button(self, relief = FLAT)
        empty.grid(row = 1, column = 2)
        
        # Close button
        close_button = Button(self, text = "Close", command = self.quit_app)
        close_button.grid(row = 1, column = 3)
        
        # 7 button
        seven_button = Button(self, text = "7", command = lambda: self.insert_int(entry, "7"))
        seven_button.grid(row = 2, column = 0)
        
        # 8 button
        eight_button = Button(self, text = "8", command = lambda: self.insert_int(entry, "8"))
        eight_button.grid(row = 2, column = 1)
        
        # 9 button
        nine_button = Button(self, text = "9", command = lambda: self.insert_int(entry, "9"))
        nine_button.grid(row = 2, column = 2)
        
        # Division button
        division_button = Button(self, text = "/")
        division_button.grid(row = 2, column = 3)
        
        # 4 button
        four_button = Button(self, text = "4", command = lambda: self.insert_int(entry, "4"))
        four_button.grid(row = 3, column = 0)
        
        # 5 button
        five_button = Button(self, text = "5", command = lambda: self.insert_int(entry, "5"))
        five_button.grid(row = 3, column = 1)
        
        # 6 button
        six_button = Button(self, text = "6", command = lambda: self.insert_int(entry, "6"))
        six_button.grid(row = 3, column = 2)
        
        # Multiplication button
        multiply_button = Button(self, text = "*")
        multiply_button.grid(row = 3, column = 3)
        
        # 1 button
        one_button = Button(self, text = "1", command = lambda: self.insert_int(entry, "1"))
        one_button.grid(row = 4, column = 0)
        
        # 2 button
        two_button = Button(self, text = "2", command = lambda: self.insert_int(entry, "2"))
        two_button.grid(row = 4, column = 1)
        
        # 3 button
        three_button = Button(self, text = "3", command = lambda: self.insert_int(entry, "3"))
        three_button.grid(row = 4, column = 2)
        
        # Minus button
        minus_button = Button(self, text = "-")
        minus_button.grid(row = 4, column = 3)
        
        # Dot button
        dot_button = Button(self, text = ".")
        dot_button.grid(row = 5, column = 0)
        
        # 0 button
        zero_button = Button(self, text = "0", command = lambda: self.insert_int(entry, "0"))
        zero_button.grid(row = 5, column = 1)
        
        # Equal button
        equal_button = Button(self, text = "=", command = lambda: self.equals(entry))
        equal_button.grid(row = 5, column = 2)
        
        # Plus button
        plus_button = Button(self, text = "+", command =lambda: self.add(entry))
        plus_button.grid(row = 5, column = 3)    
                
        # Show the fram widget and gives it an initial size
        self.pack()
        
    # Add numbers
    def add(self, entry):
        # Set the operation to add
        self.operation = 1
                
        # Get the current number
        self.current_num = int(entry.get())
        
        # Do current operation
        self.do_operation(entry)
        
        # Delete all the contents fo the entry widget
        entry.delete(0, Tkinter.END)
        
        # Insert 0
        entry.insert(0, int(0))
        
    # Print the current total
    def equals(self, entry):
        if(self.operation == 0):
            return
        
        # TODO this is a bug when clicking equals multiple times
        # Get the current number
        self.current_num = int(entry.get())
        
        # Do current opertaion
        self.do_operation(entry)
        
        # Set current operation to null
        self.operation = 0
        
        # Set the current number to 0
        self.current_num = 0
        
        # Delete all the contents fo the entry widget
        entry.delete(0, Tkinter.END)
        
        # Insert the new contents as an int
        entry.insert(0, int(self.current_total))
        
    # Do the current operation
    def do_operation(self, entry):
        print "current total: " + str(self.current_total) + " current num: " + str(self.current_num)
        if(self.operation == 0 or self.operation > self.max_operations):
            # No operation or a non operation number
            print "Error! Contact developer"
        elif(self.operation == 1): 
            # Add the numbers
            self.current_total = self.current_total + self.current_num
        elif(self.operation == 2):
            print "Subtract the numbers"
        elif(self.operation == 3):
            print "Multiply the numbers"
        elif(self.operation == 4):
            print "Divide the numbers"
                                    
    # Insert int in the Entry widget
    def insert_int(self, entry, value):
        # Get the current contents of the entry widget
        current = entry.get();
        
        # Concatenate the new value
        current = current + value
        
        # Delete all the contents fo the entry widget
        entry.delete(0, Tkinter.END)
        
        # Insert the new contents as an int
        entry.insert(0, int(current))
                
    # Clear the whole calculator as if the app was just opened
    def clear(self, entry):
        # Clear textbox
        self.delete_textbox(entry)
        
        # Set current total to 0
        self.current_total = 0
        
        # Set current number to 0
        self.current_num = 0
        
    # Delete the last added number in the text box
    def back(self, entry):
        # Get the current contents and delete textbox content
        current = entry.get()
        entry.delete(0, Tkinter.END)
        
        if(len(current) > 1):
            # Slice out the last number
            current = current[0:len(current) - 1]

            # Add the new number
            entry.insert(0, int(current))
        else:
            self.delete_textbox(entry)
            
    # Deletes the contents of the entry and puts a 0
    def delete_textbox(self, entry):
        # Delete all the contents fo the entry widget
        entry.delete(0, Tkinter.END)
        
        # Insert 0
        entry.insert(0, int(0))
        
    # Quit the application
    def quit_app(self):
        print "Bye"
        self.quit()
        
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
