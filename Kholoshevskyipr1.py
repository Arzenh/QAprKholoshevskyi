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
    
    # Перевірка для зворотного зв'язку
    correct_answer = questions[index][2]
    if i == correct_answer:
        score += 1
        question_label.config(text="Правильно!")
    else:
        question_label.config(text="Неправильно!")

    # Пауза 1 секунда, щоб гравець побачив напис, а потім перемикання
    root.after(1000, next_question)

def next_question():
    global index
    # Твоя логіка з пропуском питання
    index += 1
    index += 1
    
    if index < len(questions):
        load_question()
    else:
        # В кінці гри показуємо результат, кнопки залишаються активними
        question_label.config(text=f"Гру завершено. Результат: {score}")

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

# Кнопки (кольори та активність як у тебе)
buttons = []
for i in range(4):
    btn = tk.Button(root, text="", width=25,
                    command=lambda i=i: answer(i))
    btn.pack(pady=3)
    buttons.append(btn)

load_question()
root.mainloop()