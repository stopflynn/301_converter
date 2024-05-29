from tkinter import *
import tkinter as tk
from tkinter import ttk


class Converter:
    def __init__(self):
        # Initialise variables (such as the feedback variable)
        self.var_feedback = StringVar()
        self.var_feedback.set("")
        self.history = []

        # Set up GUI Frame
        self.temp_frame = Frame(padx=20, pady=20)
        self.temp_frame.grid()

        # Dropdown menu
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

        # Buttons frame
        buttons_frame = Frame(self.temp_frame)
        buttons_frame.grid(row=4, column=0, columnspan=2, pady=10)

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
        self.output_label.grid(row=5, columnspan=2, padx=10, pady=10, sticky="w")

        # Set up GUI Frame
        self.temp_frame = Frame(padx=20, pady=20)
        self.temp_frame.grid()

    # Function to show history
    def show_history(self):
        history_window = Toplevel()
        history_window.title("History")
        history_window.geometry("600x400")

        # Create Treeview widget
        tree = ttk.Treeview(history_window)
        tree['columns'] = ('Input', 'Feedback')
        tree.heading('#0', text='ID')
        tree.heading('Input', text='Input')
        tree.heading('Feedback', text='Feedback')
        tree.column('#0', width=50)
        tree.column('Input', width=250)
        tree.column('Feedback', width=250)
        tree.pack(expand=True, fill='both')

    # Function to convert credits
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
            required_credits = 80
        elif level == "Level 2" or level == "Level 3":
            required_credits = 60
        else:
            self.var_feedback.set("Please select a level")
            self.output_answer()
            return

        credits_needed = required_credits - credits
        if credits_needed <= 0:
            # User passed
            excess_credits = abs(credits_needed)
            feedback = f"Congratulations! You passed at {level} with {excess_credits} excess credits."
        else:
            # User hasn't passed yet
            feedback = f"You need {credits_needed} more credits to pass at {level}"

        self.var_feedback.set(feedback)
        self.output_answer()

        # Record input-feedback pair in history
        input_data = f"Level: {level}, Credits: {credits}"
        self.history.append({"input": input_data, "feedback": feedback})

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
