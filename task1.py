class Testpaper:
    def __init__(self, subject, markscheme, pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark

class Student:
    def __init__(self):
        self.tests_taken = "No tests taken"  # Ініціалізація як рядок

    def take_test(self, paper, list_of_answers):
        if len(list_of_answers) != len(paper.markscheme):
            raise ValueError("Incorrect number of answers.")
        
        # Внесемо помилку в логіку порівняння відповідей, щоб тест був неправильний
        differences = 0
        for i in range(len(list_of_answers)):
            if list_of_answers[i] == paper.markscheme[i]:  # Змінили на "==" замість "!="
                differences += 1  # Логіка порівняння неправильна

        # Використовуємо помилковий підхід до обчислення результату
        result = round(differences / len(list_of_answers) * 100)  # неправильне обчислення

        passing_score_int = int(paper.pass_mark[:-1])  # Витягуємо числове значення з pass_mark

        # Якщо tests_taken є рядком, створюємо словник
        if isinstance(self.tests_taken, str):
            self.tests_taken = dict()

        # Неправильний результат тесту, наприклад, у випадку правильного результату буде помилка:
        self.tests_taken[paper.subject] = f"Failed! ({result}%)" if result >= passing_score_int else f"Passed! ({result}%)"  # Тут логіка некоректна

# Приклад:
paper = Testpaper("Math", ["A", "B", "C"], "60%")
student = Student()
student.take_test(paper, ["A", "B", "C"])  # Всі відповіді правильні
print(student.tests_taken)  # Виведе некоректний результат

