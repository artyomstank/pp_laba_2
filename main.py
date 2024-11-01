import tkinter as tk
from tkinter import messagebox
import datetime

class DayPlannerApp:
    """Класс для создания приложения планирования дня."""

    def __init__(self, root):
        """Инициализация главного окна."""
        self.root = root
        self.root.title("ПЛАНИРОВЩИК ДНЯ")
        self.root.geometry("500x400")
        self.root.configure(bg="beige")
        # Список задач
        self.tasks = []

        # Приветственное меню
        self.welcome_screen()

    def welcome_screen(self):
        """Создание приветственного экрана."""
        # Очистка окна
        self.clear_window()

        # Текст приветствия
        welcome_label = tk.Label(self.root, text="Добро пожаловать в Планировщик дня!", font=("Times", 20))
        welcome_label.pack(pady=10)

        # Кнопки для перехода к функциональным возможностям
        add_task_button = tk.Button(
            self.root,
            text="Добавить задачу",
            command=self.add_task_screen,
            width=30, height=2, font=("Times", 14),
            bg="green",
            fg="white"
        )
        add_task_button.pack(pady=20)

        view_tasks_button = tk.Button(
            self.root,
            text="Просмотреть задачи",
            command=self.view_tasks_screen,
            width=34, height=2,
            font=("Roman", 14),
            bg="grey"
        )
        view_tasks_button.pack(pady=5)

        go_git_button = tk.Button(
            self.root,
            text="GitHub автора",
            command=self.go_git,
            width=38, height=1,
            font=("Roman", 12),
            bg="grey"
        )
        go_git_button.pack(pady=5)

    def clear_window(self):
        """Очистка всех виджетов окна."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def add_task_screen(self):
        """Экран для добавления новой задачи."""
        self.clear_window()

        # Поле для ввода названия задачи
        tk.Label(self.root, text="Введите название задачи:", font=("Times", 16)).pack(pady=5)
        self.task_name_entry = tk.Entry(self.root, width=40)
        self.task_name_entry.pack(pady=5)

        # Поле для ввода описания задачи
        tk.Label(self.root, text="Введите описание задачи:", font=("Times", 16)).pack(pady=5)
        self.task_description_entry = tk.Entry(self.root, width=40)
        self.task_description_entry.pack(pady=5)

        # Поле для ввода даты задачи
        tk.Label(self.root, text="Введите дату выполнения", font=("Times", 16)).pack(pady=5)
        tk.Label(self.root, text="(ГГГГ - ММ - ДД):", font=("Times", 10)).pack()

        self.task_date_entry = tk.Entry(self.root, width=40)
        self.task_date_entry.pack(pady=5)

        # Кнопки для добавления задачи и возврата в главное меню
        save_task_button = tk.Button(
            self.root, text="Сохранить задачу", command=self.save_task,
            width=20, bg="green", fg="white", font=("Times", 12)
        )
        save_task_button.pack(pady=20)

        back_button = tk.Button(
            self.root, text="Назад в главное меню", command=self.welcome_screen,
            width=20, height=2, font=("Arial", 12)
        )
        back_button.place(x=0, y=355)

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
            "Дата": task_date,
            "Выполнено": False
        })
        messagebox.showinfo("Успешно", f"Задача '{task_name}' добавлена.")
        self.welcome_screen()

    def view_tasks_screen(self):
        """Экран для просмотра всех задач с возможностью отметить выполненной или удалить."""
        self.clear_window()

        # Заголовок экрана
        tk.Label(self.root, text="Ваши задачи:", font=("Arial", 20)).pack(pady=10)

        if not self.tasks:
            tk.Label(self.root, text="Нет запланированных задач.", font=("Arial", 14)).pack(pady=22)
        else:
            for index, task in enumerate(self.tasks):
                task_info = (f"Задача: {task['Название']}\n"
                             f"Описание: {task['Описание']}\n"
                             f"Выполнить до: {task['Дата'].date()}\n"
                             f"Статус: {'Выполнено' if task['Выполнено'] else 'Не выполнено'}")
                task_label = tk.Label(self.root, text=task_info, justify="left")
                task_label.pack(pady=2)

                # Кнопка "Отметить выполненной"
                mark_done_button = tk.Button(
                    self.root, text="Отметить выполненной",
                    command=lambda idx=index: self.mark_task_done(idx), width=20
                )
                mark_done_button.pack(pady=2)

                # Кнопка "Удалить задачу"
                delete_button = tk.Button(
                    self.root, text="Удалить задачу",
                    command=lambda idx=index: self.delete_task(idx), width=20
                )
                delete_button.pack(pady=2)

        # Кнопка для возврата в главное меню
        back_button = tk.Button(
            self.root, text="Назад в главное меню", command=self.welcome_screen,
            width=20, height=2, font=("Arial", 12)
        )
        back_button.place(x=0, y=355)

    def go_git(self):
        """Экран с информацией о GitHub автора."""
        self.clear_window()
        tk.Label(self.root, text="GitHub: https://github.com/artyomstank", font=("Arial", 14)).pack(pady=10)
        back_button = tk.Button(
            self.root, text="Назад в главное меню", command=self.welcome_screen,
            width=20, height=2, font=("Arial", 12)
        )
        back_button.place(x=0, y=355)

    def mark_task_done(self, index):
        """Отмечает задачу как выполненную."""
        self.tasks[index]["Выполнено"] = True
        messagebox.showinfo("Успешно", f"Задача '{self.tasks[index]['Название']}' отмечена как выполненная.")
        self.view_tasks_screen()

    def delete_task(self, index):
        """Удаляет задачу из списка."""
        task_name = self.tasks[index]["Название"]
        del self.tasks[index]
        messagebox.showinfo("Удалено", f"Задача '{task_name}' удалена.")
        self.view_tasks_screen()

# Запуск приложения
if __name__ == "__main__":
    root = tk.Tk()
    app = DayPlannerApp(root)
    root.mainloop()
