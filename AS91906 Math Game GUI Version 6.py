import random
from tkinter import *
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk

class FirstWindow:
    def __init__(self, root):
        """
        Initializes the FirstWindow class.

        This method sets up the main window, configures its appearance, and 
        creates the necessary widgets for the user interface, such as buttons, 
        labels, and text entries.

        Args:
            root (Tk): The root window object for the Tkinter application.
        """
        self.root = root
        self.root.geometry("800x400")
        self.root.configure(bg="#FFC0CB")
        self.root.title("The Maths Game")

        self.photo = None

        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = Label(self.root, text="The Maths Game", bg="#FFC0CB", font=("Arial", 24, "bold"), fg="#FF69B4")
        self.title_label.pack(pady=10)

        # Main Frame
        main_frame = Frame(self.root, bg="#FFC0CB")
        main_frame.pack(padx=20, pady=10, fill=BOTH, expand=True)

        # Left frame for form inputs
        form_frame = Frame(main_frame, bg="#FFB6C1")
        form_frame.pack(side=LEFT, padx=20, pady=10, fill=BOTH, expand=True)

        # Username label and textbox
        username_label = Label(form_frame, text="Enter Username", bg="#FF69B4", font=("Arial", 12, "bold"), fg="white")
        username_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

        self.username_textbox = Entry(form_frame, font=("Arial", 12))
        self.username_textbox.grid(row=0, column=1, padx=5, pady=5)

        # Age label and textbox
        age_label = Label(form_frame, text="Enter Age", bg="#FF69B4", font=("Arial", 12, "bold"), fg="white")
        age_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

        self.age_textbox = Entry(form_frame, font=("Arial", 12))
        self.age_textbox.grid(row=1, column=1, padx=5, pady=5)

        # Photo upload label and button
        photo_label = Label(form_frame, text="Upload Photo", bg="#FF69B4", font=("Arial", 12, "bold"), fg="white")
        photo_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

        upload_button = Button(form_frame, text="Upload", command=self.upload_photo, height=1, width=15, bg="#FF69B4", font=("Arial", 12, "bold"), fg="white")
        upload_button.grid(row=2, column=1, padx=5, pady=5)

        # Placeholder for displaying the uploaded image
        self.photo_label = Label(form_frame, bg="#FFB6C1")
        self.photo_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        # Middle frame for difficulty selection
        difficulty_frame = Frame(main_frame, bg="#FFB6C1")
        difficulty_frame.pack(side=LEFT, padx=20, pady=10, fill=BOTH, expand=True)

        difficulty_label = Label(difficulty_frame, text="Select Difficulty", bg="#FF69B4", font=("Arial", 14, "bold"), fg="white")
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

        # Right frame for action buttons
        action_frame = Frame(main_frame, bg="#FFB6C1")
        action_frame.pack(side=LEFT, padx=20, pady=10, fill=BOTH, expand=True)

        # Exit button at the top
        exit_button = Button(action_frame, text="Exit", command=self.root.destroy, height=2, width=15, bg="#FF69B4", font=("Arial", 12, "bold"), fg="white")
        exit_button.pack(pady=10)

        # Play button below exit
        play_button = Button(action_frame, text="Play", command=self.open_play_window, height=2, width=15, bg="#FF69B4", font=("Arial", 12, "bold"), fg="white")
        play_button.pack(pady=10)

        # Instructions button
        instructions_button = Button(action_frame, text="Instructions", command=self.show_instructions, height=2, width=15, bg="#FF69B4", font=("Arial", 12, "bold"), fg="white")
        instructions_button.pack(pady=10)

        # Leaderboard button
        leaderboard_button = Button(action_frame, text="Leaderboard", command=self.show_leaderboard, height=2, width=15, bg="#FF69B4", font=("Arial", 12, "bold"), fg="white")
        leaderboard_button.pack(pady=10)

    def upload_photo(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            image = Image.open(file_path)
            image = image.resize((100, 100), Image.Resampling.LANCZOS)
            self.photo = ImageTk.PhotoImage(image)
            self.photo_label.config(image=self.photo)

    def open_play_window(self):
        # Validate username and age before opening the play window
        if self.validate_user_input():
            username = self.username_textbox.get()
            PlayWindow(self.root, self.difficulty.get(), username)
        else:
            messagebox.showwarning("Warning", "Please enter a valid username and age. Username should not contain spaces.")

    def validate_user_input(self):
        # Validate the username and age entries
        username = self.username_textbox.get()
        age = self.age_textbox.get()

        if not username or not username.isalnum() or ' ' in username:
            return False
        if not age.isdigit():
            return False

        return True

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
        self.play_window.geometry("700x600")
        self.play_window.configure(bg="#FFC0CB")
        self.play_window.title("Maths Game")

        self.lives = 3
        self.current_question = 0
        self.total_questions = 10

        # Lives label
        self.lives_label = Label(self.play_window, text=f"Lives: {self.lives}", font=("Arial", 12, "bold"), bg="#FFC0CB", fg="red")
        self.lives_label.pack(pady=10, anchor=W)

        # Progress bar
        self.progress_bar = Canvas(self.play_window, width=300, height=20, bg="white")
        self.progress_bar.pack(pady=10, anchor=W)
        self.progress_rectangle = self.progress_bar.create_rectangle(0, 0, 0, 20, fill="green")

        # Define widgets for the play window
        self.solving = Entry(self.play_window, font=("Arial", 12))
        self.solving.pack(pady=10, padx=10)

        self.submit = Button(self.play_window, text="Submit", command=self.submit_answer, bg="#FF69B4", font=("Arial", 12, "bold"), fg="white")
        self.submit.pack(pady=5, padx=10)

        self.next_button = Button(self.play_window, text="Next", command=self.try_again, bg="#FF69B4", font=("Arial", 12, "bold"), fg="white")
        self.next_button.pack(pady=5, padx=10)
        
        self.show_question()

    def show_question(self):
        self.current_question += 1
        self.question = self.generate_question(self.difficulty)
        self.solving.delete(0, END)
        self.solving.insert(0, self.question)

    def submit_answer(self):
        answer = self.solving.get()
        correct_answer = self.evaluate_question(self.question)

        if answer == str(correct_answer):
            self.update_progress()
        else:
            self.lives -= 1
            self.lives_label.config(text=f"Lives: {self.lives}")

        if self.lives == 0:
            self.end_game(f"Sorry {self.username}, you've lost all your lives.")
        elif self.current_question == self.total_questions:
            self.end_game(f"Congratulations {self.username}, you've completed all the questions!")

    def update_progress(self):
        self.progress_bar.delete(self.progress_rectangle)
        self.progress_rectangle = self.progress_bar.create_rectangle(0, 0, 30 * self.current_question, 20, fill="green")

    def end_game(self, message):
        messagebox.showinfo("Game Over", message)
        self.play_window.destroy()

        with open("leaderboard.txt", "a") as f:
            result = f"{self.username}: {self.current_question}/{self.total_questions} - {'Success' if self.current_question == self.total_questions else 'Fail'}\n"
            f.write(result)

    def try_again(self):
        self.show_question()

    def generate_question(self, difficulty):
        if difficulty == "Easy":
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
        elif difficulty == "Medium":
            num1 = random.randint(10, 100)
            num2 = random.randint(10, 100)
        else:
            num1 = random.randint(100, 1000)
            num2 = random.randint(100, 1000)

        return f"{num1} + {num2}"

    def evaluate_question(self, question):
        return eval(question)


if __name__ == "__main__":
    root = Tk()
    app = FirstWindow(root)
    root.mainloop()
