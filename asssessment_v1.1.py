from tkinter import *
import tkinter as tk
from tkinter import ttk


class Converter:
    def __init__(self):
        # Initialise variables (such as the feedback variable)
        self.var_feedback = StringVar()
        self.var_feedback.set("")

        self.var_has_error = StringVar()
        self.var_has_error.set("no")

        self.all_calculations = []

        # common format for all buttons
        # Arial size 14 bold, with white text
        button_font = ("Arial", "12", "bold")
        button_fg = "#FFFFFF"

        # Set up GUI Frame
        self.temp_frame = Frame(padx=20, pady=20)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame,
                                  text="NCEA credits to pass",
                                  font=("Arial", "16", "bold"))
        self.temp_heading.grid(row=0, columnspan=2)

        instructions = "Please select your year level and enter the number of credits you have."
        self.temp_instructions = Label(self.temp_frame,
                                       text=instructions,
                                       wraplength=250, width=40,
                                       justify="left")
        self.temp_instructions.grid(row=1, columnspan=2)

        self.temp_entry_label = Label(self.temp_frame, text="Enter Credits:")
        self.temp_entry_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

        self.temp_entry = Entry(self.temp_frame,
                                font=("Arial", "14"))
        self.temp_entry.grid(row=2, column=1, padx=5, pady=5)

        self.subject_label = Label(self.temp_frame, text="Select Subject:")
        self.subject_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")

        self.subject_var = tk.StringVar()
        self.subject_combobox = ttk.Combobox(self.temp_frame, width=20, textvariable=self.subject_var)
        self.subject_combobox['values'] = (
        'English', 'Mathematics', 'Physics', 'Chemistry', 'Biology')  # Example values
        self.subject_combobox.grid(row=3, column=1, padx=5, pady=5)

        self.to_celsius_button = Button(self.temp_frame,
                                        text="Convert",
                                        bg="#990099",
                                        fg=button_fg,
                                        font=button_font, width=10,
                                        command=self.temp_convert)
        self.to_celsius_button.grid(row=4, column=0, padx=5, pady=5)

        self.to_help_button = Button(self.temp_frame,
                                     text="SEARCH",
                                     bg="#CC6600",
                                     fg=button_fg,
                                     font=button_font, width=10)
        self.to_help_button.grid(row=4, column=1, padx=5, pady=5)

        # Display box
        self.display_box = Text(self.temp_frame, height=5, width=30)
        self.display_box.grid(row=5, columnspan=2, padx=5, pady=5)

    def temp_convert(self):
        # Get the credits entered by the user
        credits = self.temp_entry.get()

        # Get the selected subject from the dropdown menu
        selected_subject = self.subject_var.get()

        # Perform some conversion or action (for demonstration purposes)
        result = f"You have entered {credits} credits for the subject {selected_subject}."

        # Display the result in the display box
        self.display_box.insert(tk.END, result + "\n")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("NCEA Credits Converter")
    Converter()
    root.mainloop()
