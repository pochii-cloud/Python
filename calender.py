import tkinter as tk
import customtkinter 
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

submit_button = customtkinter.CTkButton(master=root, text="Submit", corner_radius=10,command=display_input)
submit_button.pack()

# Create the label to display the user's input
label = tk.Label(root, text="")
label.pack()

root.mainloop()


# import tkinter
# import customtkinter  # <- import the CustomTkinter module

# root_tk = tkinter.Tk()  # create the Tk window like you normally do
# root_tk.geometry("400x240")
# root_tk.title("CustomTkinter Test")

# def button_function():
#     print("button pressed")

# # Use CTkButton instead of tkinter Button
# button = customtkinter.CTkButton(master=root_tk, corner_radius=10, command=button_function)
# button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# root_tk.mainloop()




