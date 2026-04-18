import tkinter as tk

questions = [
    ("Столиця Франції?", ["Берлін", "Париж", "Рим", "Мадрид"], 1),
    ("2 + 2 =", ["3", "4", "5", "6"], 1),
    ("Колір неба?", ["Синій", "Червоний", "Жовтий", "Зелений"], 0),
    ("HTML це?", ["Мова програмування", "Мова розмітки", "ОС", "БД"], 1),
    ("Python це?", ["Мова програмування", "Редактор", "Браузер", "Гра"], 0)
]

# Зміни в новій гілці

index = 0
score = 0

def answer(i):
    global index, score

    # Функціональна помилка 1: неправильна перевірка
    score += 1

    index += 1

    # Функціональна помилка 2: пропуск питання
    index += 1

    if index < len(questions):
        load_question()
    else:
        question_label.config(text="Гру завершено")

        # UI помилка: не показує результат
        # UI помилка: кнопки залишаються активними


def load_question():
    q, answers, correct = questions[index]

    question_label.config(text=q)

    for i in range(4):
        buttons[i].config(text=answers[i])


root = tk.Tk()
root.title("Вікторина")

root.geometry("400x250")

# Питання
question_label = tk.Label(root, text="", wraplength=350, font=("Arial", 14))
question_label.pack(pady=15)

# Кнопки
buttons = []
for i in range(4):
    btn = tk.Button(root, text="", width=25,
                    command=lambda i=i: answer(i))
    btn.pack(pady=3)
    buttons.append(btn)

load_question()

root.mainloop()