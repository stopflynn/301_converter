from tkinter import *
import tkinter as tk
from tkinter import ttk

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

        # Dropdown menu for achievement level
        self.achievement_label = Label(self.temp_frame, text="Select Achievement:", anchor="w")
        self.achievement_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.achievement_var = tk.StringVar()
        self.achievement_combobox = ttk.Combobox(self.temp_frame, width=24, textvariable=self.achievement_var)
        self.achievement_combobox['values'] = ('Achieved', 'Merit', 'Excellence')  # Example values
        self.achievement_combobox.set('Achieved')  # Set default value
        self.achievement_combobox.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Enter credits box
        self.credits_label = Label(self.temp_frame, text="Enter Credits:", anchor="w")
        self.credits_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        self.credits_entry = Entry(self.temp_frame, font=("Arial", 14))
        self.credits_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Convert button
        self.convert_button = Button(self.temp_frame,
                                     text="Convert",
                                     bg="#4CAF50",
                                     fg="white",
                                     font=("Arial", 12, "bold"),
                                     width=12,
                                     command=self.convert_credits)
        self.convert_button.grid(row=4, columnspan=2, pady=10)

        # Output label
        self.output_label = Label(self.temp_frame, text="", anchor="w", justify="left", wraplength=300)
        self.output_label.grid(row=5, columnspan=2, padx=10, pady=10, sticky="w")

    # Convert credits
    def convert_credits(self):
        level = self.level_var.get()
        achievement = self.achievement_var.get()
        credits = self.credits_entry.get()

        try:
            credits = int(credits)
        except ValueError:
            self.var_feedback.set("Please enter a valid number")
            self.output_answer()
            return

        if level == "Level 1":
            required_credits = 80
        elif level == "Level 2" or level == "Level 3":
            required_credits = 60
        else:
            self.var_feedback.set("Please select a level")
            self.output_answer()
            return

        if achievement == "Achieved":
            required_credits -= credits
        elif achievement == "Merit":
            required_credits -= (credits * 2)
        elif achievement == "Excellence":
            required_credits -= (credits * 3)

        if required_credits <= 0:
            if achievement == "Excellence" and credits >= 50:
                self.var_feedback.set(f"Congratulations! You will get an Excellence endorsement at {level}")
            elif achievement == "Merit" and credits >= 50:
                self.var_feedback.set(f"Congratulations! You will get a Merit endorsement at {level}")
            else:
                self.var_feedback.set(f"Congratulations! You have enough credits to pass at {level}")
        else:
            self.var_feedback.set(f"You need {required_credits} more credits to pass at {level}")

        self.output_answer()

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
