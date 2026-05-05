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
    
    if index >= len(questions):
        return

    # 1. Перевірка відповіді
    correct_answer = questions[index][2]
    
    # Блокуємо кнопки на секунду, щоб гравець не міг "наклікати" зайвого
    for btn in buttons:
        btn.config(state="disabled")

    if i == correct_answer:
        score += 1
        feedback = "✅ ПРАВИЛЬНО!"
        print(f"DEBUG: Питання {index}. Правильно! Рахунок: {score}")
    else:
        feedback = f"❌ НЕПРАВИЛЬНО!\n(Правильна відповідь: {questions[index][1][correct_answer]})"
        print(f"DEBUG: Питання {index}. Неправильно!")

    # Відображаємо результат прямо на екрані
    question_label.config(text=feedback)

    # 2. Збільшуємо індекс
    index += 1
    
    # 3. Пауза 1.5 секунди, щоб гравець встиг прочитати текст, а потім наступне питання
    if index < len(questions):
        root.after(1500, load_question)
    else:
        root.after(1500, end_game)

def load_question():
    # Повертаємо кнопкам робочий стан при завантаженні нового питання
    q, answers, correct = questions[index]
    question_label.config(text=q)
    for i in range(4):
        buttons[i].config(text=answers[i], state="normal")

def end_game():
    question_label.config(text=f"Гру завершено.\nВаш рахунок: {score}")
    
    # Блокуємо кнопки відповідей
    for btn in buttons:
        btn.config(state="disabled")
    
    # Додаємо кнопку Restart (якщо її ще немає)
    show_restart_button()

def show_restart_button():
    # Перевірка, щоб не створювати декілька кнопок
    for widget in root.winfo_children():
        if isinstance(widget, tk.Button) and widget.cget("text") == "Почати гру заново":
            return
            
    restart_btn = tk.Button(root, text="Почати гру заново", 
                          width=25, height=2, font=("Arial", 10), 
                          bg="#4CAF50", fg="white",
                          command=restart_game)
    restart_btn.pack(pady=15)

def restart_game():
    global index, score
    index = 0
    score = 0
    # Видаляємо кнопку Restart
    for widget in root.winfo_children():
        if isinstance(widget, tk.Button) and widget.cget("text") == "Почати гру заново":
            widget.destroy()
    
    load_question()

# Налаштування вікна (ТІЛЬКИ ОДИН РАЗ)
root = tk.Tk()
root.title("Вікторина (Debug Mode)")
root.geometry("640x480")

question_label = tk.Label(root, text="", wraplength=350, font=("Arial", 18))
question_label.pack(pady=15)

buttons = []
for i in range(4):
    # Додаємо параметр font=("Назва шрифту", розмір, "стиль")
    btn = tk.Button(root, text="", width=40, height=2,
                    font=("Arial", 14, "bold"), 
                    command=lambda i=i: answer(i))
    btn.pack(pady=10)
    buttons.append(btn)

load_question()
root.mainloop()

import pytest

score = 0
index = 0


# ======================
# FIXTURE
# ======================
@pytest.fixture
def reset_game():
    global score, index
    score = 0
    index = 0


# ======================
# ASSERT ТЕСТИ
# ======================
def test_assert_1(reset_game):
    global score
    score = 1
    assert score == 1


def test_assert_2(reset_game):
    score = 0
    assert score == 0


# ======================
# PARAMETRIZE
# ======================
@pytest.mark.parametrize("input_value", [0, 1, 2])
def test_parametrize(input_value):
    assert isinstance(input_value, int)


# ======================
# RAISES
# ======================
def test_raises():
    with pytest.raises(ZeroDivisionError):
        1 / 0


# ======================
# SKIP
# ======================
@pytest.mark.skip(reason="Демонстраційний тест")
def test_skip():
    assert False


# ======================
# XFAIL
# ======================
@pytest.mark.xfail(reason="Відомий баг")
def test_xfail():
    assert 2 + 2 == 5


# ======================
# ПОМИЛКОВІ ТЕСТИ
# ======================
def test_error_1():
    assert 2 + 2 == 5

def test_error_2():
    assert "A" == "a"