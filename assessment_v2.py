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
        self.temp_frame = Frame(padx=100, pady=10)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame,
                                  text="NCEA credits to pass",
                                  font=("Arial", "16", "bold"))
        self.temp_heading.grid(row=0, columnspan=2)

        instructions = "Please select your year level and enter the number of credits you have."
        self.temp_instructions = Label(self.temp_frame,
                                       text=instructions,
                                       wraplength=250, width=110,
                                       justify="left")
        self.temp_instructions.grid(row=1, columnspan=2)

        # Dropdown menu
        self.level_label = Label(self.temp_frame, text="Select Level:")
        self.level_label.grid(row=2, column=0, padx=10, pady=5)

        self.level_var = tk.StringVar()
        self.level_combobox = ttk.Combobox(self.temp_frame, width=27, textvariable=self.level_var)
        self.level_combobox['values'] = ('Level 1', 'Level 2', 'Level 3')  # Example values
        self.level_combobox.grid(row=2, column=1, padx=10, pady=5)

        # Enter credits box
        self.credits_label = Label(self.temp_frame, text="Enter Credits:")
        self.credits_label.grid(row=3, column=0, padx=10, pady=5)

        self.credits_entry = Entry(self.temp_frame, font=("Arial", "14"))
        self.credits_entry.grid(row=3, column=1, padx=10, pady=5)

        # Display box
        self.display_box = Text(self.temp_frame, height=5, width=30)
        self.display_box.grid(row=4, columnspan=2, padx=10, pady=5)

        # Convert button
        self.convert_button = Button(self.temp_frame,
                                     text="Convert",
                                     bg="#007bff",
                                     fg=button_fg,
                                     font=button_font, width=12,
                                     command=self.convert_credits)
        self.convert_button.grid(row=5, columnspan=2, pady=5)

    # Convert credits
    def convert_credits(self):
        level = self.level_var.get()
        credits = self.credits_entry.get()

        try:
            credits = int(credits)
        except ValueError:
            self.var_feedback.set("Please enter a valid number")
            self.output_answer()
            return

        if level == "Level 1":
            required_credits = 60
        elif level == "Level 2":
            required_credits = 80
        elif level == "Level 3":
            required_credits = 100
        else:
            self.var_feedback.set("Please select a level")
            self.output_answer()
            return

        credits_needed = required_credits - credits
        self.var_feedback.set(f"You need {credits_needed} more credits to pass at {level}")

        self.output_answer()

    # Shows user output and clears entry widget
    # ready for next calculation
    def output_answer(self):
        output = self.var_feedback.get()

        self.display_box.delete(1.0, tk.END)
        self.display_box.insert(tk.END, output)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("NCEA Credit Converter")
    Converter()
    root.mainloop()
