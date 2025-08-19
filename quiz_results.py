import csv
import os

def save_results(user_name, score, questions, user_answers, correct_answers, filename="quiz_results.csv"):
    file_exists = os.path.isfile(filename)

    with open(filename, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Write header only if file doesn't exist
        if not file_exists:
            writer.writerow(["User", "Score", "Question", "User Answer", "Correct Answer"])

        # Write quiz results
        for i, question in enumerate(questions):
            writer.writerow([
                user_name,
                f"{score}/{len(questions)}",
                question["question"],
                user_answers[i],
                correct_answers[i]
            ])
