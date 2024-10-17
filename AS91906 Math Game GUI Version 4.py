import random
from tkinter import *
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk

class FirstWindow:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x600")
        self.root.configure(bg="#FFC0CB")
        self.root.title("The Maths Game")

        self.photo = None

        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = Label(self.root, text="The Maths Game", bg="#FFC0CB", font=("Arial", 24, "bold"), fg="#FF69B4")
        self.title_label.pack(pady=10)

        # Frame for buttons
        button_frame = Frame(self.root, bg="#FFB6C1")
        button_frame.pack(pady=10, fill=X)

        # Exit and Play buttons
        exit_button = Button(button_frame, text="Exit", command=self.root.destroy, height=2, width=12, bg="#FF69B4", font=("Arial", 12, "bold"), fg="white")
        exit_button.pack(side=LEFT, padx=10)

        play_button = Button(button_frame, text="Play", command=self.open_play_window, height=2, width=12, bg="#FF69B4", font=("Arial", 12, "bold"), fg="white")
        play_button.pack(side=RIGHT, padx=10)

        # Frame for difficulty options
        difficulty_frame = Frame(self.root, bg="#FFB6C1")
        difficulty_frame.pack(pady=10)

        difficulty_label = Label(difficulty_frame, text="Select Difficulty", bg="#FF69B4", font=("Arial", 14, "bold"), fg="white")
        difficulty_label.pack(anchor=W, padx=10)

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

        # Frame for user input and image upload
        form_frame = Frame(self.root, bg="#FFB6C1")
        form_frame.pack(pady=10)

        # Username label and textbox
        username_label = Label(form_frame, text="Enter Username", bg="#FF69B4", font=("Arial", 12, "bold"), fg="white")
        username_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        self.username_textbox = Entry(form_frame, font=("Arial", 12))
        self.username_textbox.grid(row=0, column=1, padx=5, pady=5)

        # Age label and textbox
        age_label = Label(form_frame, text="Enter Age", bg="#FF69B4", font=("Arial", 12, "bold"), fg="white")
        age_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        self.age_textbox = Entry(form_frame, font=("Arial", 12))
        self.age_textbox.grid(row=1, column=1, padx=5, pady=5)

        # Photo upload label and button
        photo_label = Label(form_frame, text="Upload Photo", bg="#FF69B4", font=("Arial", 12, "bold"), fg="white")
        photo_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        upload_button = Button(form_frame, text="Upload", command=self.upload_photo, height=1, width=15, bg="#FF69B4", font=("Arial", 12, "bold"), fg="white")
        upload_button.grid(row=2, column=1, padx=5, pady=5)

        # Placeholder for displaying the uploaded image
        self.photo_label = Label(form_frame, bg="#FFB6C1")
        self.photo_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        # Bottom frame for Instructions and Leaderboard buttons
        bottom_frame = Frame(self.root, bg="#FFB6C1")
        bottom_frame.pack(pady=10, fill=X)

        instructions_button = Button(bottom_frame, text="Instructions", command=self.show_instructions, height=2, width=15, bg="#FF69B4", font=("Arial", 12, "bold"), fg="white")
        instructions_button.pack(side=LEFT, padx=10)

        leaderboard_button = Button(bottom_frame, text="Leaderboard", command=self.show_leaderboard, height=2, width=15, bg="#FF69B4", font=("Arial", 12, "bold"), fg="white")
        leaderboard_button.pack(side=RIGHT, padx=10)

    def upload_photo(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            image = Image.open(file_path)
            image = image.resize((100, 100), Image.Resampling.LANCZOS)
            self.photo = ImageTk.PhotoImage(image)
            self.photo_label.config(image=self.photo)

    def open_play_window(self):
        if self.validate_user_input():
            username = self.username_textbox.get()
            PlayWindow(self.root, self.difficulty.get(), username)
        else:
            messagebox.showwarning("Warning", "Please fill out all fields correctly!")

    def validate_user_input(self):
        username = self.username_textbox.get()
        age = self.age_textbox.get()
        return username and age.isdigit()

    def show_instructions(self):
        instructions = Toplevel(self.root)
        instructions.title("Instructions")
        instructions.geometry("400x300")
        instructions.configure(bg="#FFC0CB")
        instructions_label = Label(instructions, text="Instructions: Solve the math problems correctly!", bg="#FFC0CB", font=("Arial", 14), fg="black")
        instructions_label.pack(pady=20)

    def show_leaderboard(self):
        leaderboard = Toplevel(self.root)
        leaderboard.title("Leaderboard")
        leaderboard.geometry("400x300")
        leaderboard.configure(bg="#FFC0CB")
        leaderboard_label = Label(leaderboard, text="Leaderboard!", bg="#FFC0CB", font=("Arial", 14, "bold"), fg="black")
        leaderboard_label.pack(pady=10)

        try:
            with open('leaderboard.txt', 'r') as f:
                results = f.readlines()
                results.sort(key=lambda x: int(x.split(": ")[1].split("/")[0]), reverse=True)

                for result in results:
                    result_label = Label(leaderboard, text=result.strip(), bg="#FFC0CB", font=("Arial", 12), fg="black")
                    result_label.pack(pady=5)
        except FileNotFoundError:
            result_label = Label(leaderboard, text="No results yet!", bg="#FFC0CB", font=("Arial", 12), fg="black")
            result_label.pack(pady=5)


class PlayWindow:
    def __init__(self, parent, difficulty, username):
        self.parent = parent
        self.difficulty = difficulty
        self.username = username
        self.play_window = Toplevel(self.parent)
        self.play_window.geometry("500x400")
        self.play_window.configure(bg="#FFC0CB")
        self.play_window.title("Maths Game")

        self.lives = 3
        self.current_question = 0
        self.total_questions = 10

        self.question_label = None

        # Lives label
        self.lives_label = Label(self.play_window, text=f"Lives: {self.lives}", font=("Arial", 20, "bold"), bg="#FFC0CB", fg="red")
        self.lives_label.pack(pady=10, anchor=E)

        # Progress bar
        self.progress_bar = Canvas(self.play_window, width=300, height=20, bg="white")
        self.progress_bar.pack(pady=10)

        self.update_progress_bar()

        # Define widgets for the play window
        self.solving = Entry(self.play_window, font=("Arial", 16))
        self.solving.pack(pady=10)

        self.submit = Button(self.play_window, text="Submit", command=self.submit_answer, bg="#FF69B4", font=("Arial", 12, "bold"), fg="white")
        self.submit.pack(pady=10)

        self.next_button = Button(self.play_window, text="Next", command=self.try_again, bg="#FF69B4", font=("Arial", 12, "bold"), fg="white")
        self.next_button.pack(pady=10)

        self.correct_label = None
        self.wrong_label = None
        

        # Start button
        self.try_again()

    def generate_question(self):
        if self.difficulty == "Easy":
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            operation = random.choice(['+', '-'])
            if operation == '+':
                return f"{num1} + {num2}", num1 + num2
            else:
                if num1 < num2:
                    num1, num2 = num2, num1
                return f"{num1} - {num2}", num1 - num2

        elif self.difficulty == "Medium":
            num1 = random.randint(10, 50)
            num2 = random.randint(1, 10)
            operation = random.choice(['*', '/'])
            if operation == '*':
                return f"{num1} * {num2}", num1 * num2
            else:
                num1 = num2 * random.randint(2, 5)
                return f"{num1} / {num2}", num1 / num2

        elif self.difficulty == "Hard":
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            num3 = random.randint(1, 10)
            operations = random.sample(['+', '-', '*', '/'], 2)

            if '-' in operations:
                if num1 < num2:
                    num1, num2 = num2, num1

            if '/' in operations:
                num2 = random.randint(1, 10)
                num1 = num2 * random.randint(1, 10)
                
            expression = f"{num1} {operations[0]} {num2} {operations[1]} {num3}"
            
            answer = eval(expression)

            if answer < 0:
                # Swap the operations if possible
                operations.reverse()
                expression = f"{num1} {operations[0]} {num2} {operations[1]} {num3}"
                answer = eval(expression)
            
            formatted_expression = expression.replace('/', ' / ').replace('*', ' * ').replace('+', ' + ').replace('-', ' - ')
            
            return f"{formatted_expression}", answer

    def update_progress_bar(self):
        # Update the progress bar
        self.progress_bar.delete("all")
        progress_width = (self.current_question / self.total_questions) * 300
        self.progress_bar.create_rectangle(0, 0, progress_width, 20, fill="green")

    def update_lives(self):
        # Update the lives label
        self.lives_label.config(text=f"Lives: {self.lives}")

    def submit_answer(self):
        user_answer = self.solving.get()

        if not user_answer.strip():
            messagebox.showwarning("Warning", "You haven't entered anything. Please enter an answer.")
            return
        
        try:
            correct_answer = self.correct_answer
            if user_answer.isdigit() and int(user_answer) == correct_answer:
                self.current_question += 1
                self.update_progress_bar()

                if self.current_question >= self.total_questions:
                    messagebox.showinfo("Congrats!", "You've completed all the questions!")
                    self.save_game_result(success=True)
                    self.play_window.destroy()
                    return
                
                if self.wrong_label:
                    self.wrong_label.destroy()
                if self.correct_label:
                    self.correct_label.destroy()
                self.correct_label = Label(self.play_window, text='Correct', fg='green', font=("Arial", 16, "bold"), bg="#FFC0CB")
                self.correct_label.pack(pady=10)
            else:
                self.lives -= 1
                self.update_lives()

                if self.lives == 0:
                    messagebox.showwarning("Game Over", "You've run out of lives!")
                    self.save_game_result(success=False)
                    self.play_window.destroy()
                    return

                if self.correct_label:
                    self.correct_label.destroy()
                if self.wrong_label:
                    self.wrong_label.destroy()
                self.wrong_label = Label(self.play_window, text='Wrong', fg='red', font=("Arial", 16, "bold"), bg="#FFC0CB")
                self.wrong_label.pack(pady=10)
        except ValueError:
            if self.correct_label:
                self.correct_label.destroy()
            if self.wrong_label:
                self.wrong_label.destroy()
            self.wrong_label = Label(self.play_window, text='Wrong', fg='red', font=("Arial", 16, "bold"), bg="#FFC0CB")
            self.wrong_label.pack(pady=10)

    def try_again(self):
        question_text, self.correct_answer = self.generate_question()

        if self.question_label:
            self.question_label.destroy()

        self.question_label = Label(self.play_window, text=question_text, font=("Arial", 32, "bold"), bg="#FFC0CB")
        self.question_label.pack(pady=20, anchor=N)

        self.solving.delete(0, END)

    def save_game_result(self, success):
        with open('leaderboard.txt', 'a') as f:
            status = "Success" if success else "Failed"
            f.write(f"{self.username}: {self.current_question}/{self.total_questions} - {status}\n")


# Main application
if __name__ == "__main__":
    root = Tk()
    FirstWindow(root)
    root.mainloop()
