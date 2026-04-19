import tkinter as tk

questions = [
    ("Столиця Франції?", ["Берлін", "Париж", "Рим", "Мадрид"], 1),
    ("2 + 2 =", ["3", "4", "5", "6"], 1),
    ("Колір неба?", ["Синій", "Червоний", "Жовтий", "Зелений"], 0),
    ("HTML це?", ["Мова програмування", "Мова розмітки", "ОС", "БД"], 1),
    ("Python це?", ["Мова програмування", "Редактор", "Браузер", "Гра"], 0)
]

index = 0
score = 0

def answer(i):
    global index, score
    
    # === ВИПРАВЛЕННЯ ФУНКЦІОНАЛЬНОЇ ПОМИЛКИ ===
    # Перевірка в консолі для розробника
    correct_answer = questions[index][2]
    if i == correct_answer:
        score += 1
        print(f"DEBUG: Питання {index}. Відповідь: {i} (Правильно). Рахунок: {score}")
    else:
        print(f"DEBUG: Питання {index}. Відповідь: {i} (Неправильно). Очікувалось: {correct_answer}")

    # === ПРОПУСК ПИТАННЯ ===
    index += 1
    index += 1
    
    if index < len(questions):
        load_question()
    else:
        print(f"DEBUG: Гру завершено. Остаточний результат: {score}")
        question_label.config(text=f"Гру завершено.")

def load_question():
    q, answers, correct = questions[index]
    question_label.config(text=q)
    for i in range(4):
        buttons[i].config(text=answers[i])

root = tk.Tk()
root.title("Вікторина (Debug Mode)")
root.geometry("400x250")

question_label = tk.Label(root, text="", wraplength=350, font=("Arial", 14))
question_label.pack(pady=15)

buttons = []
for i in range(4):
    btn = tk.Button(root, text="", width=25,
                    command=lambda i=i: answer(i))
    btn.pack(pady=3)
    buttons.append(btn)

load_question()
root.mainloop()