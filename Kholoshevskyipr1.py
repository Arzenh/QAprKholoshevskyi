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

    score += 0
  
    
    # === ВИПРАВЛЕННЯ ФУНКЦІОНАЛЬНОЇ ПОМИЛКИ (Score) ===
    # Перевірка в консолі для розробника (Debug Mode)
    correct_answer = questions[index][2]
    if i == correct_answer:
        score += 1
        print(f"DEBUG: Питання {index}. Відповідь: {i} (Правильно). Рахунок: {score}")
    else:
        print(f"DEBUG: Питання {index}. Відповідь: {i} (Неправильно). Очікувалось: {correct_answer}")
    
    if index < len(questions):
        load_question()
    else:

        # В кінці гри показуємо результат, кнопки залишаються активними
        question_label.config(text=f"Гру завершено. Результат: {score}")

        end_game()
        
        end_gamee()
        
        # Вивід результату після завершення
        print(f"DEBUG: Гру завершено. Остаточний результат: {score}")
        question_label.config(text=f"Гру завершено. Рахунок: {score}")


def load_question():
    q, answers, correct = questions[index]
    question_label.config(text=q)
    for i in range(4):
        buttons[i].config(text=answers[i])


root = tk.Tk()
root.title("Вікторина")

def end_game():
    question_label.config(text="Гру завершено")
    
    # === ВИПРАВЛЕННЯ BUG 5: Кнопки залишаються активними ===
    # Блокуємо всі кнопки відповідей після завершення гри
    for btn in buttons:
        btn.config(state="disabled")

def end_gamee():
    question_label.config(text="Гру завершено")
    
    # === ВИПРАВЛЕННЯ BUG 3: Додаємо кнопку Restart ===
    restart_btn = tk.Button(root, text="Почати гру заново", 
                          width=25, height=2, font=("Arial", 10), 
                          bg="#4CAF50", fg="white",
                          command=restart_game)
    restart_btn.pack(pady=15)

def restart_game():
    global index, score
    index = 0
    score = 0
    # Видаляємо кнопку Restart (якщо вона є)
    for widget in root.winfo_children():
        if isinstance(widget, tk.Button) and widget.cget("text") == "Почати гру заново":
            widget.destroy()
    
    load_question()

root = tk.Tk()
root.title("Вікторина")

root.geometry("400x300")   # збільшили висоту для кнопки

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