import tkinter as tk

# 1–2. Создание главного окна
window = tk.Tk()
window.title("Қарапайым калькулятор")
window.geometry("400x300")

# 3–7. GUI элементы

# Поле для первого числа
tk.Label(window, text="Сан 1:").pack()
num1_entry = tk.Entry(window)
num1_entry.pack()

# Поле для второго числа
tk.Label(window, text="Сан 2:").pack()
num2_entry = tk.Entry(window)
num2_entry.pack()

# Label для результата
result_label = tk.Label(window, text="Нәтиже: ", font=("Arial", 14))
result_label.pack(pady=15)


# 8–15. Функция выполнения математической операции
def calculate(operation):
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())

        if operation == "+":
            result = num1 + num2

        elif operation == "-":
            result = num1 - num2

        elif operation == "*":
            result = num1 * num2

        elif operation == "/":
            if num2 == 0:
                result_label.config(text="Нөлге бөлу мүмкін емес!")
                return
            result = num1 / num2

        # 16–17. Вывод результата
        result_label.config(text="Нәтиже: " + str(result))

    except ValueError:
        result_label.config(text="Қате: Сан енгізіңіз!")


# Кнопки операций
add_button = tk.Button(
    window,
    text="Қосу",
    command=lambda: calculate("+")
)
add_button.pack(pady=3)

subtract_button = tk.Button(
    window,
    text="Алу",
    command=lambda: calculate("-")
)
subtract_button.pack(pady=3)

multiply_button = tk.Button(
    window,
    text="Көбейту",
    command=lambda: calculate("*")
)
multiply_button.pack(pady=3)

divide_button = tk.Button(
    window,
    text="Бөлу",
    command=lambda: calculate("/")
)
divide_button.pack(pady=3)


# Запуск программы
window.mainloop()