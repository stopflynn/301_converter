from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt


def open_endorsements_window():
    endorsements_window = Toplevel()
    endorsements_window.title("Endorsements")
    endorsements_window.geometry("300x200")

    # Frame to organize elements
    frame = Frame(endorsements_window, padx=20, pady=10)
    frame.pack(expand=True, fill='both')

    # Title label
    title_label = Label(frame, text="Enter Credits for Endorsements", font=("Arial", 12, "bold"))
    title_label.grid(row=0, columnspan=2, pady=(0, 10))

    # Labels and entry fields for credits at different levels
    Label(frame, text="Achieved Credits:", font=("Arial", 12)).grid(row=1, column=0, sticky='w')
    achieved_entry = Entry(frame, font=("Arial", 12), width=10)
    achieved_entry.grid(row=1, column=1, padx=5, pady=5)

    Label(frame, text="Merit Credits:", font=("Arial", 12)).grid(row=2, column=0, sticky='w')
    merit_entry = Entry(frame, font=("Arial", 12), width=10)
    merit_entry.grid(row=2, column=1, padx=5, pady=5)

    Label(frame, text="Excellence Credits:", font=("Arial", 12)).grid(row=3, column=0, sticky='w')
    excellence_entry = Entry(frame, font=("Arial", 12), width=10)
    excellence_entry.grid(row=3, column=1, padx=5, pady=5)

    def check_endorsements():
        # Get the text from each entry field
        achieved_text = achieved_entry.get()
        merit_text = merit_entry.get()
        excellence_text = excellence_entry.get()

        # Convert the text to integers if they are not empty
        try:
            achieved_credits = int(achieved_text)
            merit_credits = int(merit_text)
            excellence_credits = int(excellence_text)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integer values for credits.")
            return

        # Display endorsement message
        endorsement_message = ""
        if achieved_credits >= 50:
            endorsement_message += "Achieved Endorsement\n"

        if merit_credits >= 50:
            endorsement_message += "Merit Endorsement\n"

        if excellence_credits >= 50:
            endorsement_message += "Excellence Endorsement\n"

        # If none of the endorsements are earned
        if not endorsement_message:
            endorsement_message = "No endorsements earned."
        messagebox.showinfo("Endorsement Status", endorsement_message)

        # Display pie chart with the number of credits
        labels = 'Achieved', 'Merit', 'Excellence'
        sizes = [achieved_credits, merit_credits, excellence_credits]
        plt.pie(sizes, labels=labels, autopct='%1.0f', startangle=140,
                textprops={'fontsize': 12}, labeldistance=1.1)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title('Endorsement Credits', fontsize=14, fontweight='bold')
        plt.show()

    # Button to check endorsements
    check_button = Button(frame, text="Check Endorsements", command=check_endorsements, font=("Arial", 12, "bold"))
    check_button.grid(row=4, columnspan=2, pady=10)


class Converter:
    def __init__(self):
        # Initialise variables (such as the feedback variable)
        self.var_feedback = StringVar()
        self.var_feedback.set("")
        self.history = []

        # Set up GUI Frame
        self.temp_frame = Frame(padx=20, pady=20)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame,
                                  text="NCEA Credits to Pass",
                                  font=("Arial", 16, "bold"),
                                  pady=10)
        self.temp_heading.grid(row=0, columnspan=2)

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

        # MAKE CONVERT BUTTON BIGGER

        # Convert button
        self.convert_button = Button(self.temp_frame,
                                     text="Convert",
                                     bg="#4CAF50",
                                     fg="white",
                                     font=("Arial", 12, "bold"),
                                     width=12,
                                     command=self.convert_credits)
        self.convert_button.grid(row=3, columnspan=2, pady=10)

        # New window button (Open Endorsements)
        self.new_window_button = Button(buttons_frame,
                                        text="Open Endorsements",
                                        bg="#007bff",
                                        fg="white",
                                        font=("Arial", 12, "bold"),
                                        width=15,
                                        command=open_endorsements_window)
        self.new_window_button.grid(row=0, column=0, padx=(0, 10))

        # History button
        self.history_button = Button(buttons_frame,
                                     text="History",
                                     bg="#ff9800",
                                     fg="white",
                                     font=("Arial", 12, "bold"),
                                     width=12,
                                     command=self.show_history)
        self.history_button.grid(row=0, column=1)

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
        history_window.geometry("400x300")

        # Frame to organize history elements
        history_frame = Frame(history_window, padx=20, pady=10)
        history_frame.pack(expand=True, fill='both')

        # Title label
        title_label = Label(history_frame, text="History of Inputs and Feedbacks", font=("Arial", 14, "bold"))
        title_label.grid(row=0, columnspan=2, pady=(0, 10))

        # Display history
        for i, entry in enumerate(self.history):
            Label(history_frame, text=f"Input {i + 1}: {entry['input']}", font=("Arial", 12)).grid(row=i + 1, column=0,
                                                                                                   sticky='w')
            Label(history_frame, text=f"Feedback {i + 1}: {entry['feedback']}", font=("Arial", 12)).grid(row=i + 1,
                                                                                                         column=1,
                                                                                                         sticky='w')

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
            self.var_feedback.set(f"Congratulations! You passed at {level} with {excess_credits} excess credits.")
        else:
            # User hasn't passed yet
            self.var_feedback.set(f"You need {credits_needed} more credits to pass at {level}")

        self.output_answer()

    # Endorsements window
    @staticmethod
    def endorsements_window(self):
        endorsements_window = Toplevel()
        endorsements_window.title("Endorsements")
        endorsements_window.geometry("300x200")

        # Labels and entry fields for credits at different levels
        Label(endorsements_window, text="Achieved Credits:").pack()
        achieved_entry = Entry(endorsements_window)
        achieved_entry.pack()

        Label(endorsements_window, text="Merit Credits:").pack()
        merit_entry = Entry(endorsements_window)
        merit_entry.pack()

        Label(endorsements_window, text="Excellence Credits:").pack()
        excellence_entry = Entry(endorsements_window)
        excellence_entry.pack()

        from tkinter import messagebox

        # Function to check endorsements
        def check_endorsements():
            # Get the text from each entry field
            achieved_text = achieved_entry.get()
            merit_text = merit_entry.get()
            excellence_text = excellence_entry.get()

            # Check if any entry field is empty
            if not (achieved_text and merit_text and excellence_text):
                messagebox.showerror("Error", "Please enter credits for all levels.")
                return

            try:
                # Convert the text to integers
                achieved_credits = int(achieved_text)
                merit_credits = int(merit_text)
                excellence_credits = int(excellence_text)
            except ValueError:
                messagebox.showerror("Error", "Please enter valid integer values for credits.")
                return

            endorsement_message = ""
            if achieved_credits > 50:
                endorsement_message += "Endorsed with Achieved\n"
            if merit_credits > 50:
                endorsement_message += "Endorsed with Merit\n"
            if excellence_credits > 50:
                endorsement_message += "Endorsed with Excellence\n"

            if not endorsement_message:
                endorsement_message = "No endorsements earned."

            # Display endorsement message
            messagebox.showinfo("Endorsement Status", endorsement_message)

            # Display endorsement message
            messagebox.showinfo("Endorsement Status", endorsement_message)

        # Button to check endorsements
        Button(endorsements_window, text="Check Endorsements", command=check_endorsements).pack()

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
