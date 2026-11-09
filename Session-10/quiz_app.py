
# ==========================================
# Task 1: Indian Geography Quiz App
# ==========================================

import tkinter as tk

# Create Main Window
root = tk.Tk()

# Set Window Title
root.title("Indian Geography Quiz")

# Set Window Size
root.geometry("450x400")


# Store Quiz Questions
questions = [
    {
        "question": "1. Which is the largest state of India by area?",
        "options": ["Gujarat", "Rajasthan", "Maharashtra", "Madhya Pradesh"],
        "answer": "Rajasthan"
    },
    {
        "question": "2. Which is the longest river in India?",
        "options": ["Yamuna", "Ganga", "Godavari", "Narmada"],
        "answer": "Ganga"
    },
    {
        "question": "3. Which is the highest mountain peak in India?",
        "options": ["Nanda Devi", "Kanchenjunga", "Anamudi", "Kamet"],
        "answer": "Kanchenjunga"
    },
    {
        "question": "4. Which ocean is located south of India?",
        "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"],
        "answer": "Indian Ocean"
    },
    {
        "question": "5. Which is the smallest state of India by area?",
        "options": ["Sikkim", "Tripura", "Goa", "Manipur"],
        "answer": "Goa"
    }
]


# ==========================================
# Task 2: Option Buttons and Result
# ==========================================

# Store Current Question Index and Score
state = {
    "index": 0,
    "score": 0
}


# Function to Check Answer
def check(option):

    if option == questions[state["index"]]["answer"]:
        state["score"] += 1
        result_label.config(text="Correct!")
    else:
        result_label.config(text="Wrong!")

    score_label.config(text="Score: " + str(state["score"]))


# ==========================================
# Task 3: Next Question and Score
# ==========================================

# Function to Load Next Question
def next_question():

    if state["index"] < len(questions) - 1:

        state["index"] += 1

        question_label.config(
            text=questions[state["index"]]["question"]
        )

        result_label.config(text="")

        for i, option in enumerate(questions[state["index"]]["options"]):
            option_buttons[i].config(
                text=option,
                command=lambda option=option: check(option),
                state="normal"
            )

    else:
        finish_quiz()


# ==========================================
# Task 4: Finish Quiz and Restart
# ==========================================

# Function to Finish Quiz
def finish_quiz():

    question_label.config(text="Quiz Completed!")

    result_label.config(text="")

    score_label.config(
        text="Your score: " + str(state["score"]) + "/5"
    )

    # Hide Option Buttons
    for button in option_buttons:
        button.grid_remove()

    # Disable Next Button
    next_button.config(state="disabled")

    # Show Restart Button
    restart_button.grid(row=7, column=0, columnspan=2, pady=10)


# Function to Restart Quiz
def restart_quiz():

    state["index"] = 0
    state["score"] = 0

    question_label.config(
        text=questions[0]["question"]
    )

    result_label.config(text="")

    score_label.config(text="Score: 0")

    # Show Option Buttons Again
    for i, option in enumerate(questions[0]["options"]):
        option_buttons[i].config(
            text=option,
            command=lambda option=option: check(option),
            state="normal"
        )

        option_buttons[i].grid()

    # Enable Next Button
    next_button.config(state="normal")

    # Hide Restart Button
    restart_button.grid_remove()


# Create Quiz Heading
heading = tk.Label(
    root,
    text="Indian Geography Quiz",
    font=("Arial", 18, "bold")
)

heading.grid(row=0, column=0, columnspan=2, pady=20)


# Display First Question
question_label = tk.Label(
    root,
    text=questions[0]["question"],
    font=("Arial", 12),
    wraplength=400
)

question_label.grid(row=1, column=0, columnspan=2, pady=20)


# Create Option Buttons
option_buttons = []

for i, option in enumerate(questions[0]["options"]):

    button = tk.Button(
        root,
        text=option,
        width=20,
        command=lambda option=option: check(option)
    )

    button.grid(
        row=2 + i // 2,
        column=i % 2,
        padx=10,
        pady=10
    )

    option_buttons.append(button)


# Create Result Label
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold")
)

result_label.grid(row=4, column=0, columnspan=2, pady=5)


# Create Score Label
score_label = tk.Label(
    root,
    text="Score: 0",
    font=("Arial", 12, "bold")
)

score_label.grid(row=5, column=0, columnspan=2, pady=5)


# Create Next Button
next_button = tk.Button(
    root,
    text="Next",
    width=15,
    command=next_question
)

next_button.grid(row=6, column=0, columnspan=2, pady=10)


# Create Restart Button
restart_button = tk.Button(
    root,
    text="Restart",
    width=15,
    command=restart_quiz
)

# Hide Restart Button Initially
restart_button.grid_remove()


# Run Main Window
root.mainloop()
