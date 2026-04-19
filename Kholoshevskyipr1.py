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
    # Функціональна помилка 1: неправильна перевірка (залишаємо)
    score += 1
    # Функціональна помилка 2: пропуск питання (залишаємо)
    index += 1
    index += 1
    
    if index < len(questions):
        load_question()
    else:
        end_game()

def load_question():
    q, answers, correct = questions[index]
    question_label.config(text=q)
    for i in range(4):
        buttons[i].config(text=answers[i])

def end_game():
    question_label.config(text="Гру завершено")
    
    # === ВИПРАВЛЕННЯ BUG 5: Кнопки залишаються активними ===
    # Блокуємо всі кнопки відповідей після завершення гри
    for btn in buttons:
        btn.config(state="disabled")

root = tk.Tk()
root.title("Вікторина")
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