 # Date: 29/08/2024
 # Aurthor:Jerry Fan
 # Purpose: To create a math game so children can imporove their mach skills
 # Target Audience:Children or adults

import random # Import GUI
from tkinter import *
from tkinter import messagebox, filedialog # Imaport Messagebox
from PIL import Image, ImageTk # To put the image



class FirstWindow: # Create the first window
    def __init__(self, root):
        """
        Initializes the FirstWindow class.

        This method sets up the main window, configures its appearance, and 
        creates the necessary widgets for the user interface, such as buttons, 
        labels, and text entries.

        Args:
            root (Tk): The root window object for the Tkinter application.
        """
        self.root = root # To open it
        self.root.geometry("800x400") # To make the size
        self.root.configure(bg="#FFC0CB") # The colour for the window
        self.root.title("The Maths Game") # The name of the window

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
        username_label = Label(form_frame, text="Enter Username", bg="#FF69B4", font=("Arial", 12, "bold"), fg="white") # Hot pink
        username_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

        self.username_textbox = Entry(form_frame, font=("Arial", 12))
        self.username_textbox.grid(row=0, column=1, padx=5, pady=5)

         # Age label and textbox
        age_label = Label(form_frame, text="Enter Age", bg="#FF69B4", font=("Arial", 12, "bold"), fg="white") # Hot pink
        age_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

        self.age_textbox = Entry(form_frame, font=("Arial", 12))
        self.age_textbox.grid(row=1, column=1, padx=5, pady=5)

         # Photo upload label and button
        photo_label = Label(form_frame, text="Upload Photo", bg="#FF69B4", font=("Arial", 12, "bold"), fg="white") # Hot pink
        photo_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

        upload_button = Button(form_frame, text="Upload", command=self.upload_photo, height=1, width=15, bg="#FF69B4", font=("Arial", 12, "bold"), fg="white") # Hot pink
        upload_button.grid(row=2, column=1, padx=5, pady=5)

         # Placeholder for displaying the uploaded image
        self.photo_label = Label(form_frame, bg="#FFB6C1") # Pink
        self.photo_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

         # Middle frame for difficulty selection
        difficulty_frame = Frame(main_frame, bg="#FFB6C1") # Pink
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
                bg="#FFB6C1", # Pink
                font=("Arial", 12),
                fg="black",
                selectcolor="#FF69B4"
                ).pack(anchor=W, padx=10)

         # Right frame for action buttons
        action_frame = Frame(main_frame, bg="#FFB6C1")
        action_frame.pack(side=LEFT, padx=20, pady=10, fill=BOTH, expand=True)

         # Exit button at the top
        exit_button = Button(action_frame, text="Exit", command=self.root.destroy, height=2, width=15, bg="#FF69B4", font=("Arial", 12, "bold"), fg="white") # Hot pink
        exit_button.pack(pady=10)

         # Play button below exit
        play_button = Button(action_frame, text="Play", command=self.open_play_window, height=2, width=15, bg="#FF69B4", font=("Arial", 12, "bold"), fg="white") # Hot pink
        play_button.pack(pady=10)

         # Instructions button
        instructions_button = Button(action_frame, text="Instructions", command=self.show_instructions, height=2, width=15, bg="#FF69B4", font=("Arial", 12, "bold"), fg="white") # Hot pink
        instructions_button.pack(pady=10)

         # Leaderboard button
        leaderboard_button = Button(action_frame, text="Leaderboard", command=self.show_leaderboard, height=2, width=15, bg="#FF69B4", font=("Arial", 12, "bold"), fg="white") # Hot pink
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

    def show_instructions(self): # The instructions window
        instructions = Toplevel(self.root)
        instructions.title("Instructions") # The name of that
        instructions.geometry("400x300") # The size
        instructions.configure(bg="#FFC0CB")  # Light pink
        instructions_label = Label(instructions, text="Instructions: Solve the math problems correctly!", bg="#FFC0CB", font=("Arial", 14), fg="black")  
        instructions_label.pack(pady=20)

    def show_leaderboard(self): # The leaderboard window
        leaderboard = Toplevel(self.root)
        leaderboard.title("Leaderboard") # The name of that
        leaderboard.geometry("400x300") # The size
        leaderboard.configure(bg="#FFC0CB")  # Light pink 
        leaderboard_label = Label(leaderboard, text="Leaderboard!", bg="#FFC0CB", font=("Arial", 14,"bold"), fg="black")  
        leaderboard_label.pack(pady=10)

        try:
            with open('leaderboard.txt', 'r') as f:
                results = f.readlines()
                results.sort(key=lambda x: int(x.split(": ")[1].split("/")[0]), reverse=True)  

                for result in results:
                    result_label = Label(leaderboard, text=result.strip(), bg="#FFC0CB", font=("Arial", 12), fg="black") # Light pink
                    result_label.pack(pady=5)
        except FileNotFoundError:
            result_label = Label(leaderboard, text="No results yet!", bg="#FFC0CB", font=("Arial", 12), fg="black") # Light pink
            result_label.pack(pady=5)
    

    

    

        

class PlayWindow: # The maths play window
    def __init__(self, parent, difficulty, username):
        self.parent = parent
        self.difficulty = difficulty
        self.username = username
        self.play_window = Toplevel(self.parent)
        self.play_window.geometry("500x400")
        self.play_window.configure(bg="#FFC0CB") # Light pink
        self.play_window.title("Maths Game") # The name of that 

        self.lives = 3
        self.current_question = 0
        self.total_questions = 10

        self.question_label = None

         # Lives label
        self.lives_label = Label(self.play_window, text=f"Lives: {self.lives}", font=("Arial", 20, "bold"), bg="#FFC0CB", fg="red") # Light pink
        self.lives_label.pack(pady=10, anchor=E)

         # Progress bar
        self.progress_bar = Canvas(self.play_window, width=300, height=20, bg="white")
        self.progress_bar.pack(pady=10)

        self.update_progress_bar()

         # Define widgets for the play window
        self.solving = Entry(self.play_window, font=("Arial", 16))
        self.solving.pack(pady=10)

        self.submit = Button(self.play_window, text="Submit", command=self.submit_answer, bg="#FF69B4", font=("Arial", 12, "bold"), fg="white") # Hot pink
        self.submit.pack(pady=10)

        self.next_button = Button(self.play_window, text="Next", command=self.try_again, bg="#FF69B4", font=("Arial", 12, "bold"), fg="white") # Hot pink
        self.next_button.pack(pady=10)

        self.correct_label = None
        self.wrong_label = None
        

         # Start button
        self.try_again()

    def generate_question(self):
        if self.difficulty == "Easy":
            num1 = random.randint(1, 10) # First number from 1 to 10
            num2 = random.randint(1, 10) # The second from 1 to 10
            operation = random.choice(['+', '-']) # Just use the + and -
            if operation == '+':
                return f"{num1} + {num2}", num1 + num2
            else:
                if num1 < num2:
                    num1, num2 = num2, num1 # Make sure there are no negative answers
                return f"{num1} - {num2}", num1 - num2

        elif self.difficulty == "Medium":
            num1 = random.randint(10, 50) # 10 to 50 number to choose
            num2 = random.randint(1, 10) # 1 to 10 number to choose
            operation = random.choice(['*', '/'] )# To use time and dived
            if operation == '*':
                return f"{num1} * {num2}", num1 * num2
            else:
                num1 = num2 * random.randint(2, 5)
                return f"{num1} / {num2}", num1 / num2

        elif self.difficulty == "Hard":
            num1 = random.randint(1, 10) # 1 to 10 number to choose
            num2 = random.randint(1, 10) # 1 to 10 number to choose
            num3 = random.randint(1, 10) # 1 to 10 number to choose
            operations = random.sample(['+', '-', '*', '/'], 2) # To use 4

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

    def submit_answer(self): # To check the answer and print out
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

    def try_again(self): # To be the next
        question_text, self.correct_answer = self.generate_question()

        if self.question_label:
            self.question_label.destroy()

        self.question_label = Label(self.play_window, text=question_text, font=("Arial", 32, "bold"), bg="#FFC0CB")
        self.question_label.pack(pady=20, anchor=N)

        self.solving.delete(0, END)

    def save_game_result(self, success): # To save the window to the doc
        with open('leaderboard.txt', 'a') as f:
            status = "Success" if success else "Failed"
            f.write(f"{self.username}: {self.current_question}/{self.total_questions} - {status}\n")


 # Main application
if __name__ == "__main__":
    root = Tk()
    FirstWindow(root)
    root.mainloop()
