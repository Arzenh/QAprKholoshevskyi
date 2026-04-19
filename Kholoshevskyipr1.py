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

def answer(selected_index):
    global index, score
    
    correct_index = questions[index][2]
    correct_answer_text = questions[index][1][correct_index]
    
    # === ВИПРАВЛЕНО BUG 1: неправильна перевірка відповіді ===
    if selected_index == correct_index:
        score += 1
        feedback = "✅ Правильно!"
        color = "green"
    else:
        feedback = f"❌ Неправильно.\nПравильна відповідь: {correct_answer_text}"
        color = "red"
    
    # Показуємо фідбек у грі
    question_label.config(text=feedback, fg=color, font=("Arial", 13))
    
    # Блокуємо кнопки на час фідбеку
    for btn in buttons:
        btn.config(state="disabled")
    
    # Затримка перед наступним питанням
    root.after(1500, next_question)

def next_question():
    global index
    # === BUG 2: Пропуск питань (навмисно залишено для демонстрації) ===
    # Через цей рядок питання пропускаються
    index += 1      # перший раз
    index += 1      # другий раз → питання пропускається
    
    if index < len(questions):
        load_question()
    else:
        end_game()

def load_question():
    q, answers, _ = questions[index]
    question_label.config(text=q, fg="black", font=("Arial", 14))
    
    for i in range(4):
        buttons[i].config(text=answers[i], state="normal")

def end_game():
    question_label.config(
        text=f"Гру завершено!\n\nВаш результат: {score} з {len(questions)}",
        fg="blue",
        font=("Arial", 14)
    )
    for btn in buttons:
        btn.config(state="disabled")

# ====================== GUI ======================
root = tk.Tk()
root.title("Вікторина")
root.geometry("520x380")

question_label = tk.Label(root, text="", wraplength=480, font=("Arial", 14), justify="center")
question_label.pack(pady=30)

buttons = []
for i in range(4):
    btn = tk.Button(root, text="", width=40, height=2, font=("Arial", 10),
                    command=lambda i=i: answer(i))
    btn.pack(pady=6)
    buttons.append(btn)

load_question()
root.mainloop()