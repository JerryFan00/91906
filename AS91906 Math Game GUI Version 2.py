import random
from tkinter import *
from tkinter import messagebox 

class FirstWindow:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x300")
        self.root.configure(bg="#FFC0CB") 
        self.root.title("The Maths Game")

        self.create_widgets()

    def create_widgets(self):
        # Top frame for Exit and Play buttons
        top_frame = Frame(self.root, bg="#FFB6C1")  
        top_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

        # Exit button on the left
        exit_button = Button(top_frame, text="Exit", command=self.root.destroy, height=2, width=12, bg="#FF69B4", font=("Arial", 12, "bold"), fg="white")  # Hot Pink
        exit_button.pack(side=LEFT, padx=10, pady=10)

        # Play button on the right
        play_button = Button(top_frame, text="Play", command=self.open_play_window, height=2, width=12, bg="#FF69B4", font=("Arial", 12, "bold"), fg="white")  # Hot Pink
        play_button.pack(side=RIGHT, padx=10, pady=10)

        # Frame for Difficulty options
        difficulty_frame = Frame(self.root, bg="#FFB6C1")
        difficulty_frame.grid(row=1, column=1, padx=20, pady=10, sticky="ne")

        difficulty_label = Label(difficulty_frame, text="Select Difficulty", bg="#FF69B4", font=("Arial", 14, "bold"), fg="white")  # Hot Pink
        difficulty_label.pack(anchor=W, padx=10, pady=5)

        self.difficulty = StringVar(value="Easy")
        difficulty_options = ["Easy", "Medium", "Hard"]
        for option in difficulty_options:
            Radiobutton(
                difficulty_frame,
                text=option,
                variable=self.difficulty,
                value=option,
                bg="#FFB6C1",  
                font=("Arial", 12),
                fg="black",  
                selectcolor="#FF69B4"  
                ).pack(anchor=W, padx=10)
            
        # Creating a frame to hold labels and entry boxes
        form_frame = Frame(self.root, bg="#FFB6C1")  # Light Pink
        form_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nw")

        # Username label and textbox
        username_label = Label(form_frame, text="Enter Username", bg="#FF69B4", font=("Arial", 12, "bold"), fg="white")  # Hot Pink
        username_label.grid(row=0, column=0, padx=5, pady=5)

        self.username_textbox = Entry(form_frame, font=("Arial", 12))
        self.username_textbox.grid(row=0, column=1, padx=5, pady=5)

        # Empty label for spacing
        empty_label = Label(form_frame, text="", bg="#FFB6C1")  
        empty_label.grid(row=1, column=0, padx=5, pady=5)

        # Age label and textbox
        age_label = Label(form_frame, text="Enter Age", bg="#FF69B4", font=("Arial", 12, "bold"), fg="white")  
        age_label.grid(row=2, column=0, padx=5, pady=5)

        self.age_textbox = Entry(form_frame, font=("Arial", 12))
        self.age_textbox.grid(row=2, column=1, padx=5, pady=5)

        # Bottom frame for Instructions and Leaderboard buttons
        bottom_frame = Frame(self.root, bg="#FFB6C1")  
        bottom_frame.grid(row=2, column=0, columnspan=2, sticky="ew")

        instructions_button = Button(bottom_frame, text="Instructions", command=self.show_instructions, height=2, width=15, bg="#FF69B4", font=("Arial", 12, "bold"), fg="white")  # Hot Pink
        instructions_button.pack(side=LEFT, padx=10, pady=10)

        leaderboard_button = Button(bottom_frame, text="Leaderboard", command=self.show_leaderboard, height=2, width=15, bg="#FF69B4", font=("Arial", 12, "bold"), fg="white")  # Hot Pink
        leaderboard_button.pack(side=RIGHT, padx=10, pady=10)

    def open_play_window(self):
        # Validate username and age before opening the play window
        if self.validate_user_input():
            PlayWindow(self.root, self.difficulty.get())
        else:
            messagebox.showwarning("Warning", "Please fill out all fields correctly!")

    def validate_user_input(self):
        # Validate the username and age entries
        username = self.username_textbox.get()
        age = self.age_textbox.get()
        return username and age.isdigit()

    def show_instructions(self):
        instructions = Toplevel(self.root)
        instructions.title("Instructions")
        instructions.geometry("400x300")
        instructions.configure(bg="#FFC0CB")  
        instructions_label = Label(instructions, text="Instructions: Solve the math problems correctly!", bg="#FFC0CB", font=("Arial", 14), fg="black")  # Light Pink
        instructions_label.pack(pady=20)

    def show_leaderboard(self):
        leaderboard = Toplevel(self.root)
        leaderboard.title("Leaderboard")
        leaderboard.geometry("400x300")
        leaderboard.configure(bg="#FFC0CB")  
        leaderboard_label = Label(leaderboard, text="Leaderboard!", bg="#FFC0CB", font=("Arial", 14), fg="black")  # Light Pink
        leaderboard_label.pack(pady=20)

class PlayWindow:
    def __init__(self, parent, difficulty):
        self.parent = parent
        self.difficulty = difficulty
        self.play_window = Toplevel(self.parent)
        self.play_window.geometry("250x300")
        self.play_window.configure(bg="#FFC0CB")  

        # Define widgets for the play window
        self.solving = Entry(self.play_window, font=("Arial", 12))
        self.solving.place(relx=0.35, rely=0.4, relwidth=0.34, relheight=0.23)

        self.submit = Button(self.play_window, text="Submit", command=self.submit_answer, bg="#FF69B4", font=("Arial", 12, "bold"), fg="white")  # Hot Pink
        self.submit.place(relx=0.35, rely=0.64, relwidth=0.34, relheight=0.23)

        self.try_again_button = Button(self.play_window, text="Try Again", command=self.try_again, bg="#FF69B4", font=("Arial", 12, "bold"), fg="white")  # Hot Pink
        self.try_again_button.place(relx=0.39, rely=0.9)

        self.correct_label = None
        self.wrong_label = None
        self.question_label = None

        # Start button
        start = Button(self.play_window, text="Start", command=self.try_again, bg="#FF69B4", font=("Arial", 12, "bold"), fg="white")  # Hot Pink
        start.place(relx=0.45, rely=0.2)

    def generate_question(self):
        if self.difficulty == "Easy":
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            return f"{num1} + {num2}", num1 + num2
        elif self.difficulty == "Medium":
            num1 = random.randint(10, 50)
            num2 = random.randint(10, 50)
            return f"{num1} - {num2}", num1 - num2
        elif self.difficulty == "Hard":
            num1 = random.randint(10, 100)
            num2 = random.randint(10, 10)
            return f"{num1} * {num2}", num1 * num2

    def submit_answer(self):
        user_answer = self.solving.get()
        try:
            correct_answer = self.correct_answer
            if user_answer.isdigit() and int(user_answer) == correct_answer:
                if self.wrong_label:
                    self.wrong_label.destroy()
                if self.correct_label:
                    self.correct_label.destroy()
                self.correct_label = Label(self.play_window, text='Correct', fg='green', font=("Arial", 16, "bold"))
                self.correct_label.place(relx=0.3, rely=0.2)
            else:
                if self.correct_label:
                    self.correct_label.destroy()
                if self.wrong_label:
                    self.wrong_label.destroy()
                self.wrong_label = Label(self.play_window, text='Wrong', fg='red', font=("Arial", 16, "bold"))
                self.wrong_label.place(relx=0.3, rely=0.2)
        except ValueError:
            if self.correct_label:
                self.correct_label.destroy()
            if self.wrong_label:
                self.wrong_label.destroy()
            self.wrong_label = Label(self.play_window, text='Wrong', fg='red', font=("Arial", 16, "bold"))
            self.wrong_label.place(relx=0.3, rely=0.2)

    def try_again(self):
        question_text, self.correct_answer = self.generate_question()

        if self.question_label:
            self.question_label.destroy()

        self.question_label = Label(self.play_window, text=question_text, font=("Arial", 16, "bold"))
        self.question_label.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)

        # Clear the entry widget
        self.solving.delete(0, END)

# Main application
if __name__ == "__main__":
    root = Tk()
    FirstWindow(root)
    root.mainloop()
