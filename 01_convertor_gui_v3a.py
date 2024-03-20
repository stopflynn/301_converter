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
        self.temp_frame = Frame(padx=100, pady=120)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame,
                                  text="NCEA credits to pass",
                                  font=("Arial", "16", "bold")
                                  )
        self.temp_heading.grid(row=0)

        instructions = "Please select your year level and enter the number of credits you have."
        self.temp_instructions = Label(self.temp_frame,
                                       text=instructions,
                                       wraplength=250, width=110,
                                       justify="left")
        self.temp_instructions.grid(row=1)

        self.temp_entry = Entry(self.temp_frame,
                                font=("Arial", "14")
                                )
        self.temp_entry.grid(row=2, padx=10, pady=10)

        error = "Please enter a number"
        self.output_label = Label(self.temp_frame, text="",
                                  fg="#9C0000")
        self.output_label.grid(row=2)

        # Conversion, help and history / export buttons
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=6)

        self.to_celsius_button = Button(self.button_frame,
                                        text="To Celsius",
                                        bg="#990099",
                                        fg=button_fg,
                                        font=button_font, width=12,
                                        command=lambda: self.temp_convert(-459))
        self.to_celsius_button.grid(row=6, column=1, padx=10, pady=10)

        self.to_help_button = Button(self.button_frame,
                                     text="SEARCH",
                                     bg="#CC6600",
                                     fg=button_fg,
                                     font=button_font, width=12)
        self.to_help_button.grid(row=6, column=0, padx=5, pady=5)

        # python program demonstrating
        # Combobox widget using tkinter

        # label text for title
        # label

        # Combobox creation
        n = tk.StringVar()
        senior_subjects = ttk.Combobox(self.temp_frame, width=27,
                                       textvariable=n)

        # Adding combobox drop down list
        senior_subjects['values'] = (' English',
                                     ' Contextualised English',
                                     ' Mathematics',
                                     ' Calculus',
                                     ' Statistics',
                                     ' Biology'
                                     ' Chemistry',
                                     ' Marine Studies',
                                     ' Earth and Space Science',
                                     ' Physics',
                                     ' Classical Studies',
                                     ' History',
                                     ' Geography',
                                     ' Tourism',
                                     ' Media Studies',
                                     ' Psychology',
                                     ' Applied Recreation',
                                     ' Health',
                                     ' Nutrition and Wellbeing in Society',
                                     ' Mauao Athlete Pathways',
                                     ' Outdoor Education'
                                     ' Physical Education',
                                     ' Art Design',
                                     ' Dance',
                                     ' Drama',
                                     ' Music',
                                     ' Painting',
                                     ' Photography',
                                     ' Accounting',
                                     ' Business Studies',
                                     ' Economics',
                                     ' Personal Financial Management',
                                     ' English Second Language',
                                     ' French',
                                     ' Mahi Toi / Tikanga Maori',
                                     ' Te Ao Haka',
                                     ' Te Reo Maori'
                                     ' Te Reo Rangatira',
                                     ' Computer Science',
                                     ' Food and Nutrition',
                                     ' Graphics (DVC)',
                                     ' Hard Materials - Wood',
                                     ' Hard Materials - Engineering',
                                     ' Culinary Arts',
                                     ' Soft Materials',
                                     ' Gateway',
                                     ' University Papers',
                                     ' STAR',
                                     )

        senior_subjects.grid(column=0, row=4)
        senior_subjects.current(1)
        senior_subjects.mainloop()

    # checks user input and if it's valid, converts temperature
    def check_temp(self, min_value):

        has_error = "no"
        error = "Please enter a number that is more " \
                "than {}".format(min_value)

        # check that user has entered a valid number...

        response = self.temp_entry.get()

        try:
            response = float(response)

            if response < min_value:
                has_error = "yes"

        except ValueError:
            has_error = "yes"

        # Sets var_has_error so that entry box and
        # labels can be correctly formatted by formatting function
        if has_error == "yes":
            self.var_has_error.set("yes")
            self.var_feedback.set(error)
            return "invalid"

        # If we have no errors...
        else:
            # set to 'no' in case of previous errors
            self.var_has_error.set("no")

            # return number to be
            # converted and enable history button
            return response

    @staticmethod
    def round_ans(val):
        var_rounded = (val * 2 + 1) // 2
        return "{:.0f}".format(var_rounded)

    # check temperature is more than -459 and convert it
    def temp_convert(self, min_val):
        to_convert = self.check_temp(min_val)

        # create degree symbol and set up variables edit
        # feedback if user enters valid number
        deg_sign = u'\N{DEGREE SIGN}'
        set_feedback = "yes"
        answer = ""
        from_to = ""

        if to_convert == "invalid":
            set_feedback = "no"

        # Convert to Celsius
        elif min_val == -459:
            # do calculation
            answer = (to_convert - 32) * 5 / 9
            from_to = "{} F{} is {} C{}"

        # Convert to Farenheit
        else:
            answer = to_convert * 1.8 + 32
            from_to = "{} C{} is {} F{}"

        if set_feedback == "yes":
            to_convert = self.round_ans(to_convert)
            answer = self.round_ans(answer)

            # create user output and add to calculation history
            feedback = from_to.format(to_convert, deg_sign, answer, deg_sign)
            self.var_feedback.set(feedback)

            self.all_calculations.append(feedback)

            # Delete code below when history component is working!
            print(self.all_calculations)

        self.output_answer()

    # Shows user output and clears entry widget
    # ready for next calculation
    def output_answer(self):
        output = self.var_feedback.get()
        has_errors = self.var_has_error.get()

        if has_errors == "yes":
            # red text, pink entry box
            self.output_label.config(fg="#9C0000")
            self.temp_entry.config(bg="#F8CECC")

        else:
            self.output_label.config(fg="#004C00")
            self.temp_entry.config(bg="#FFFFFF")

        self.output_label.config(text=output)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
