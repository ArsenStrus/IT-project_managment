import unittest
from task1 import Testpaper, Student  # Імпортуємо класи з task1.py

class TestStudent(unittest.TestCase):

    def test_passed_test(self):
        paper = Testpaper("Math", ["A", "B", "C"], "60%")
        student = Student()
        student.take_test(paper, ["A", "B", "C"])
        # Перевіряємо, чи правильно зберігається результат тесту
        self.assertEqual(student.tests_taken["Math"], "Passed! (100%)")

    def test_failed_test(self):
        paper = Testpaper("Math", ["A", "B", "C"], "60%")
        student = Student()
        student.take_test(paper, ["A", "C", "A"])
        # Перевіряємо, чи правильно зберігається результат тесту
        self.assertEqual(student.tests_taken["Math"], "Failed! (33%)")

    def test_incorrect_number_of_answers(self):
        paper = Testpaper("Math", ["A", "B", "C"], "60%")
        student = Student()
        # Перевіряємо, чи правильно піднімається помилка
        with self.assertRaises(ValueError):  # Перевіряємо, чи піднявся ValueError
            student.take_test(paper, ["A", "B"])

    def test_edge_case_pass_score(self):
        paper = Testpaper("Math", ["A", "B", "C"], "33%")
        student = Student()
        student.take_test(paper, ["A", "B", "C"])
        # Перевіряємо, чи правильно зберігається результат на межовому балу
        self.assertEqual(student.tests_taken["Math"], "Passed! (100%)")

# Запуск тестів
if __name__ == '__main__':
    unittest.main()
