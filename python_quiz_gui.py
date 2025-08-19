import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from quiz_results import save_results



# Quiz questions data
questions = [
    {
        "question": "Who developed Python?",
        "options": ["Guido van Rossum", "Linus Torvalds", "Dennis Ritchie", "James Gosling"],
        "answer": "Guido van Rossum"
    },
    {
        "question": "What is the output of print(2 ** 3)?",
        "options": ["6", "8", "9", "5"],
        "answer": "8"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "define", "def", "function"],
        "answer": "def"
    },
    {
        "question": "Which of the following is a mutable data type in Python?",
        "options": ["tuple", "list", "string", "int"],
        "answer": "list"
    },
    {
        "question": "What is the output of print(type([]))?",
        "options": ["<class 'tuple'>", "<class 'list'>", "<class 'dict'>", "<class 'set'>"],
        "answer": "<class 'list'>"
    },
    {
        "question": "Which operator is used for floor division in Python?",
        "options": ["/", "//", "%", "**"],
        "answer": "//"
    },
    {
        "question": "What is the correct way to create a dictionary in Python?",
        "options": ["dict = {}", "dict = []", "dict = ()", "dict = <>"],
        "answer": "dict = {}"
    },
    {
        "question": "What is the output of print(bool(0))?",
        "options": ["True", "False", "0", "None"],
        "answer": "False"
    },
    {
        "question": "What is the difference between 'is' and '==' in Python?",
        "options": [
            "'is' checks value, '==' checks memory location",
            "'==' checks value, 'is' checks memory location",
            "Both are same",
            "None of the above"
        ],
        "answer": "'==' checks value, 'is' checks memory location"
    },
    {
        "question": "What will be the output of print([i for i in range(5) if i % 2 == 0])?",
        "options": ["[1, 3, 5]", "[0, 2, 4]", "[2, 4, 6]", "[0, 1, 2, 3, 4]"],
        "answer": "[0, 2, 4]"
    }
]


#Global Vars 
score = 0
current_q = 0
user_name = ""

#GUI Setup 
root = tk.Tk()
root.title("Python Quiz App")
root.geometry("1600x1000")   # Start page size

# Start Page
start_frame = tk.Frame(root)
start_frame.pack(fill="both", expand=True)

# Background for Start Page
start_bg = Image.open(r"C:\\Users\\saies\\OneDrive\\Pictures\\Desktop\\Quiz_app\\background_img.png")
start_bg = start_bg.resize((600, 400))
start_bg_photo = ImageTk.PhotoImage(start_bg)

start_bg_label = tk.Label(start_frame, image=start_bg_photo)
start_bg_label.place(x=0, y=100, relwidth=1, relheight=1)

# Title on Start Page
title_label = tk.Label(
    start_frame,
    text="Welcome to the Python Quiz!",
    font=("Arial", 28, "bold"),
    bg="#dfe6e9",
    fg="#255096"
)
title_label.pack(pady=20)

# Name input
name_label = tk.Label(start_frame, text="Enter your name:", font=("Times New Roman", 18, "bold"), bg="#dfe6e9")
name_label.pack(pady=40)

name_entry = tk.Entry(start_frame, font=("Times New Roman", 16))
name_entry.pack(pady=20)

# ------------------ Quiz Page ------------------
quiz_frame = tk.Frame(root)

# Background for Quiz Page
quiz_bg = Image.open(r"C:\\Users\\saies\\OneDrive\\Pictures\\Desktop\\Quiz_app\\background_img.png")
quiz_bg = quiz_bg.resize((1600, 1000))
quiz_bg_photo = ImageTk.PhotoImage(quiz_bg)

quiz_bg_label = tk.Label(quiz_frame, image=quiz_bg_photo)
quiz_bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Question Label
question_label = tk.Label(quiz_frame, text="", font=("Comic Sans MS", 20, "bold"), fg="#0f0c68", bg="#f1f2f6")
question_label.pack(pady=40)

# Options
selected_option = tk.StringVar()
options = []
for i in range(4):
    rb = tk.Radiobutton(
        quiz_frame, text="", variable=selected_option, value="",
        font=("Comic Sans MS", 16), bg="#efe812", anchor="w", padx=20
    )
    rb.pack(fill="x", padx=400, pady=10)
    options.append(rb)

# Buttons
submit_btn = tk.Button(quiz_frame, text="Submit", font=("Arial", 16, "bold"), command=lambda: check_answer())
submit_btn.pack(pady=30)


# ------------------ Functions ------------------
def start_quiz():
    global user_name
    user_name = name_entry.get().strip()

    if user_name == "":
        messagebox.showwarning("Input Error", "Please enter your name to start the quiz!")
        return

    # Switch page
    start_frame.pack_forget()
    quiz_frame.pack(fill="both", expand=True)

    # Resize window for quiz
    root.geometry("1600x1000")

    load_question()


def load_question():
    global current_q
    if current_q < len(questions):
        q = questions[current_q]
        question_label.config(text=q["question"])
        selected_option.set(None)

        for i, opt in enumerate(q["options"]):
            options[i].config(text=opt, value=opt)
    else:
        show_score()

user_answers = []

def check_answer():
    global score, current_q, user_answers
    chosen = selected_option.get()
    user_answers.append(chosen)  # store the answer
    if chosen == questions[current_q]["answer"]:
        score += 1
    current_q += 1
    load_question()



def show_score():
    global result_frame
    # Hide quiz frame
    quiz_frame.pack_forget()

    # Create a new results frame
    result_frame = tk.Frame(root, width=1600, height=1000)
    result_frame.pack(fill="both", expand=True)

    # Background same as quiz
    score_bg_label = tk.Label(result_frame, image=quiz_bg_photo)
    score_bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Show Score
    score_label = tk.Label(
        result_frame,
        text=f"🎉 {user_name}, Your Score: {score}/{len(questions)} 🎉",
        font=("Comic Sans MS", 28, "bold"),
        fg="dark blue",
        bg="#f7f715"
    )
    score_label.pack(pady=20)

    # Create canvas + scrollbar for scrolling answers
    canvas = tk.Canvas(result_frame, bg="#ffffff", highlightthickness=0)
    canvas.pack(side="left", fill="both", expand=True, padx=20, pady=20)

    scrollbar = tk.Scrollbar(result_frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)

    # Frame inside canvas
    review_frame = tk.Frame(canvas, bg="#ffffff")
    canvas.create_window((0, 0), window=review_frame, anchor="nw")

    # Update scroll region when size changes
    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    review_frame.bind("<Configure>", on_frame_configure)

    # Populate review_frame with questions & answers
    for i, q in enumerate(questions):
        q_label = tk.Label(
            review_frame,
            text=f"Q{i+1}. {q['question']}",
            font=("Arial", 14, "bold"),
            bg="#ffffff",
            anchor="w",
            justify="left"
        )
        q_label.pack(anchor="w", pady=5)

        for opt in q["options"]:
            if opt == q["answer"]:
                color = "green"  # Correct answer highlighted
            else:
                color = "black"

            opt_label = tk.Label(
                review_frame,
                text=f"   • {opt}",
                font=("Arial", 12),
                fg=color,
                bg="#ffffff",
                anchor="w",
                justify="left"
            )
            opt_label.pack(anchor="w")

    restart_btn = tk.Button(
        result_frame,
        text="Restart Quiz",
        font=("Arial", 14, "bold"),
        bg="#0984e3",
        fg="white",
        command=lambda: restart_quiz(result_frame)
    )
    restart_btn.pack(pady=20)

    correct_answers = [q["answer"] for q in questions]
    save_results(user_name, score, questions, user_answers, correct_answers)

def restart_quiz(result_frame):
    global score, current_q
    score = 0
    current_q = 0

    result_frame.destroy()
    start_frame.pack(fill="both", expand=True)
    root.geometry("800x500")


# Start button
start_btn = tk.Button(start_frame, text="Start Quiz", font=("Arial", 16, "bold"), command=start_quiz)
start_btn.pack(pady=20)

# Run GUI
root.mainloop()