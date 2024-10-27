import tkinter as tk
from tkinter import messagebox
import datetime


class DayPlannerApp:
    """Класс для создания приложения планирования дня."""

    def __init__(self, root):
        """Инициализация главного окна."""
        self.root = root
        self.root.title("ПЛАНИРОВЩИК ДНЯ")
        self.root.geometry("500x400")  # Устанавливаем размер окна побольше

        # Список задач
        self.tasks = []

        # Приветственное меню
        self.welcome_screen()

    def welcome_screen(self):
        """Создание приветственного экрана."""
        # Очистка окна
        self.clear_window()

        # Текст приветствия
        welcome_label = tk.Label(self.root, text="Добро пожаловать в Планировщик дня!", font=("Arial", 16))
        welcome_label.pack(pady=10)

        # Кнопки для перехода к функциональным возможностям
        add_task_button = tk.Button(self.root, text="Добавить задачу", command=self.add_task_screen, width=50,height=3)
        add_task_button.pack(pady=5)

        view_tasks_button = tk.Button(self.root, text="Просмотреть задачи", command=self.view_tasks_screen, width=50)
        view_tasks_button.pack(pady=5)

    def clear_window(self):
        """Очистка всех виджетов окна."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def add_task_screen(self):
        """Экран для добавления новой задачи."""
        self.clear_window()

        # Поле для ввода названия задачи
        tk.Label(self.root, text="Введите название задачи:").pack(pady=5)
        self.task_name_entry = tk.Entry(self.root, width=40)
        self.task_name_entry.pack(pady=5)

        # Поле для ввода описания задачи
        tk.Label(self.root, text="Введите описание задачи:").pack(pady=5)
        self.task_description_entry = tk.Entry(self.root, width=40)
        self.task_description_entry.pack(pady=5)

        # Поле для ввода даты задачи
        tk.Label(self.root, text="Введите дату выполнения (ГГГГ-ММ-ДД):").pack(pady=5)
        self.task_date_entry = tk.Entry(self.root, width=40)
        self.task_date_entry.pack(pady=5)

        # Кнопки для добавления задачи и возврата в главное меню
        save_task_button = tk.Button(self.root, text="Сохранить задачу", command=self.save_task, width=20)
        save_task_button.pack(pady=5)

        back_button = tk.Button(self.root, text="Назад в главное меню", command=self.welcome_screen, width=20)
        back_button.pack(pady=5)

    def save_task(self):
        """Сохранение задачи в список задач."""
        task_name = self.task_name_entry.get()
        task_description = self.task_description_entry.get()
        task_date_str = self.task_date_entry.get()

        # Валидация даты
        try:
            task_date = datetime.datetime.strptime(task_date_str, '%Y-%m-%d')
        except ValueError:
            messagebox.showerror("Ошибка", "Неверный формат даты. Используйте формат ГГГГ-ММ-ДД.")
            return

        # Добавление задачи в список
        self.tasks.append({
            "Название": task_name,
            "Описание": task_description,
            "Дата": task_date
        })
        messagebox.showinfo("Успешно", f"Задача '{task_name}' добавлена.")
        self.welcome_screen()

    def view_tasks_screen(self):
        """Экран для просмотра всех задач."""
        self.clear_window()

        # Заголовок экрана
        tk.Label(self.root, text="Ваши задачи:", font=("Arial", 14)).pack(pady=10)

        if not self.tasks:
            tk.Label(self.root, text="Нет запланированных задач.").pack()
        else:
            for task in self.tasks:
                task_info = (f"Задача: {task['Название']}\n"
                             f"Описание: {task['Описание']}\n"
                             f"Выполнить до: {task['Дата'].date()}\n")
                tk.Label(self.root, text=task_info, justify="left").pack(pady=2)

        # Кнопка для возврата в главное меню
        back_button = tk.Button(self.root, text="Назад в главное меню", command=self.welcome_screen, width=20)
        back_button.pack(pady=10)


# Запуск приложения
if __name__ == "__main__":
    root = tk.Tk()
    app = DayPlannerApp(root)
    root.mainloop()
