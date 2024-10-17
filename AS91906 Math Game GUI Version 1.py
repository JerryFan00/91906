import random
from tkinter import *

class FirstWindow:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x400")  
        self.root.configure(bg="hot pink")
        self.root.title("The Maths Game")

        self.create_widgets()

    def create_widgets(self):
        play_button = Button(self.root, text="Play", command=self.open_play_window, height=10, width=10, bg="light pink")
        play_button.pack()

        exit_button = Button(self.root, text="Exit", command=self.root.destroy)
        exit_button.pack(anchor=W, padx=10)

        instructions_button = Button(self.root, text="Instructions", command=self.show_instructions)
        instructions_button.pack(anchor=W, padx=10)

        leaderboard_button = Button(self.root, text="Leaderboard", command=self.show_leaderboard)
        leaderboard_button.pack(anchor=W, padx=10)

        username_label = Label(self.root, text="Enter Username")
        username_label.pack(anchor=W, padx=10)

        self.username_textbox = Entry(self.root)
        self.username_textbox.pack(anchor=W, padx=10)

        age_label = Label(self.root, text="Enter Age")
        age_label.pack(anchor=W, padx=10)

        self.age_textbox = Entry(self.root)
        self.age_textbox.pack(anchor=W, padx=10)

    def open_play_window(self):
        PlayWindow(self.root)

    def show_instructions(self):
        instructions = Toplevel(self.root)
        instructions.title("Instructions")
        instructions.geometry("400x300")
        instructions.configure(bg="hot pink")
        instructions_label = Label(instructions, text="Instructions: Solve the math problems correctly!")
        instructions_label.pack(pady=20)

    def show_leaderboard(self):
        leaderboard = Toplevel(self.root)
        leaderboard.title("Leaderboard")
        leaderboard.geometry("400x300")
        leaderboard.configure(bg="hot pink")
        leaderboard_label = Label(leaderboard, text="Leaderboard!")
        leaderboard_label.pack(pady=20)

class PlayWindow:
    def __init__(self, parent):
        self.parent = parent
        self.play_window = Toplevel(self.parent)
        self.play_window.geometry("250x300")  
        self.play_window.configure(bg="hot pink")

        # Define widgets for the play window
        self.num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        self.solving = Entry(self.play_window)
        self.solving.place(relx=0.35, rely=0.4, relwidth=0.34, relheight=0.23)

        self.submit = Button(self.play_window, text="Submit", command=self.submit_answer)
        self.submit.place(relx=0.35, rely=0.64, relwidth=0.34, relheight=0.23)

        self.try_again_button = Button(self.play_window, text="Try Again", command=self.try_again)
        self.try_again_button.place(relx=0.39, rely=0.9)

        self.correct_label = None
        self.wrong_label = None
        self.question_label = None

        # Start button
        start = Button(self.play_window, text="Start", command=self.try_again)
        start.place(relx=0.45, rely=0.2)

    def submit_answer(self):
        user_answer = self.solving.get()
        try:
            num1, num2 = map(int, self.question_label.cget("text").split('+'))
            correct_answer = num1 + num2
            if user_answer.isdigit() and int(user_answer) == correct_answer:
                if self.wrong_label:
                    self.wrong_label.destroy()
                if self.correct_label:
                    self.correct_label.destroy()
                self.correct_label = Label(self.play_window, text='Correct', fg='green', font=("Courier", 16))
                self.correct_label.place(relx=0.3, rely=0.2)
            else:
                if self.correct_label:
                    self.correct_label.destroy()
                if self.wrong_label:
                    self.wrong_label.destroy()
                self.wrong_label = Label(self.play_window, text='Wrong', fg='red', font=("Courier", 16))
                self.wrong_label.place(relx=0.3, rely=0.2)
        except ValueError:
            if self.correct_label:
                self.correct_label.destroy()
            if self.wrong_label:
                self.wrong_label.destroy()
            self.wrong_label = Label(self.play_window, text='Wrong', fg='red', font=("Courier", 16))
            self.wrong_label.place(relx=0.3, rely=0.2)

    def try_again(self):
        num1 = random.choice(self.num)
        num2 = random.choice(self.num)
        question_text = f"{num1}+{num2}"

        if self.question_label:
            self.question_label.destroy()

        self.question_label = Label(self.play_window, text=question_text, font=("Courier", 16))
        self.question_label.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)

        # Clear the entry widget
        self.solving.delete(0, END)


# Main application
if __name__ == "__main__":
    root = Tk()
    FirstWindow(root)
    root.mainloop()
