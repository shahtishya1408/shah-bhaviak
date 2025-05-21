from tkinter import *
from tkinter import messagebox
def marck():
    try:
        # Get user inputs and convert them to integers
        sem1 = int(acount.get())
        sem2 = int(stae.get())
        sem3 = int(economice.get())
        sem4 = int(ba.get())


        # Calculate the result
        result = sem1 + sem2 + sem3 + sem4

       


        # Check if any mark is greater than 100 or less than 0
        if sem1 > 100 or sem2 > 100 or sem3 > 100 or sem4 > 100 or sem1 < 0 or sem2 < 0 or sem3 < 0 or sem4 < 0:
            messagebox.showerror("Invalid Marks", "Marks must be between 0 and 100.")
            return
        # Check the result and display the message
        elif result == 200:
            result_label.config(text="You are eligible for CA examination!")
        elif sem1 == 50 and sem2 == 50 and sem3 == 50 and sem4 == 50:
            result_label.config(text="Each semester mark is 50.")
   
        else:
            result_label.config(text=f"Your total marks are {result}.")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

# Create the main Tkinter window
root = Tk()
root.title("CA Eligibility")
root.geometry("400x300")

# Labels and Entry widgets for user input
Label(root, text="Enter Account marks:").pack()
acount = Entry(root)
acount.pack()

Label(root, text="Enter Statistics marks:").pack()
stae = Entry(root)
stae.pack()

Label(root, text="Enter Economics marks:").pack()
economice = Entry(root)
economice.pack()

Label(root, text="Enter Business Admin marks:").pack()
ba = Entry(root)
ba.pack()

# Button to calculate and display the result
Button(root, text="Check Eligibility", command=marck).pack()

# Label to display the result
result_label = Label(root, text="")
result_label.pack()

# Run the Tkinter application
root.mainloop()
