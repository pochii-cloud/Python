import tkinter as tk
import calendar
root = tk.Tk()

# Define the function to display the user's input
def display_input():
    user_input = entry.get()
    label.config(text=calendar.calendar(int(user_input)))


# Create the Entry widget with a placeholder
entry = tk.Entry(root)
entry.insert(0, "enter year")

entry.pack()

# Create the Submit button
submit_button = tk.Button(root, text="Submit", command=display_input)
submit_button.pack()

# Create the label to display the user's input
label = tk.Label(root, text="")
label.pack()

root.mainloop()







