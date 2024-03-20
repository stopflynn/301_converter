from tkinter import *
import tkinter as tk
from tkinter import ttk
import re

class Converter:
    def __init__(self):
        # Initialise variables (such as the feedback variable)
        self.var_feedback = StringVar()
        self.var_feedback.set("")

        # Set up GUI Frame
        self.temp_frame = Frame(padx=20, pady=20)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame,
                                  text="NCEA Credits to Pass",
                                  font=("Arial", 16, "bold"),
                                  pady=10)
        self.temp_heading.grid(row=0, columnspan=2)

        # Dropdown menu for level selection
        self.level_label = Label(self.temp_frame, text="Select Level:", anchor="w")
        self.level_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.level_var = tk.StringVar()
        self.level_combobox = ttk.Combobox(self.temp_frame, width=24, textvariable=self.level_var)
        self.level_combobox['values'] = ('Level 1', 'Level 2', 'Level 3')  # Example values
        self.level_combobox.set('Level 1')  # Set default value
        self.level_combobox.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Enter credits box
        self.credits_label = Label(self.temp_frame, text="Enter Credits:", anchor="w")
        self.credits_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.credits_entry = Entry(self.temp_frame, font=("Arial", 14))
        self.credits_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Convert button
        self.convert_button = Button(self.temp_frame,
                                     text="Convert",
                                     bg="#4CAF50",
                                     fg="white",
                                     font=("Arial", 12, "bold"),
                                     width=12,
                                     command=self.convert_credits)
        self.convert_button.grid(row=3, columnspan=2, pady=10)

        # Output label
        self.output_label = Label(self.temp_frame, text="", anchor="w", justify="left", wraplength=300)
        self.output_label.grid(row=4, columnspan=2, padx=10, pady=10, sticky="w")

    # Convert credits
    def convert_credits(self):
        level = self.level_var.get()
        credits_text = self.credits_entry.get()

        if not credits_text:
            self.var_feedback.set("Please enter the credits in the correct format")
            self.output_answer()
            return

        try:
            credits_list = self.parse_credits(credits_text)
        except ValueError:
            self.var_feedback.set("Please enter the credits in the correct format")
            self.output_answer()
            return

        total_achieved = 0
        total_merit = 0
        total_excellence = 0

        for credit in credits_list:
            if credit[1] == 'A':
                total_achieved += int(credit[0])
            elif credit[1] == 'M':
                total_merit += int(credit[0])
            elif credit[1] == 'E':
                total_excellence += int(credit[0])

        required_credits = 80 if level == "Level 1" else 60

        if total_achieved >= required_credits:
            self.var_feedback.set(f"Congratulations! You have enough credits to pass at {level}")
        else:
            required_achieved = required_credits - total_achieved
            self.var_feedback.set(f"You need {required_achieved} more achieved credits to pass at {level}")

        if total_merit >= 50:
            self.var_feedback.set(self.var_feedback.get() + "\nYou will get a Merit endorsement.")
        if total_excellence >= 50:
            self.var_feedback.set(self.var_feedback.get() + "\nYou will get an Excellence endorsement.")

        self.output_answer()

    # Parse the input credits
    def parse_credits(self, credits_text):
        credits_list = re.findall(r'(\d+)([AME])', credits_text.upper())
        if not credits_list:
            raise ValueError("Invalid format")
        return credits_list

    # Update output label
    def output_answer(self):
        output = self.var_feedback.get()
        self.output_label.config(text=output)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("NCEA Credit Converter")
    Converter()
    root.mainloop()
