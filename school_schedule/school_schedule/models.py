"""
Моделі для системи керування шкільним розкладом.

Цей модуль описує основні сутності: предмети, вчителів, класи та учнів.
Кожна модель представлена як клас Django ORM, що дозволяє взаємодіяти з базою даних
та використовувати всі переваги фреймворку.

Ви можете адаптувати ці класи під інший ORM або SQL, якщо не використовуєте Django.
"""

from django.db import models


class Subject(models.Model):
    """Навчальний предмет.

    Зберігає назву та необов’язковий опис предмета.
    """

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предмети"

    def __str__(self) -> str:
        return self.name


class Teacher(models.Model):
    """Вчитель.

    Кожен вчитель має ім’я та належить до певного предмета. Зв’язок задається через
    ForeignKey, тому один предмет може викладатися кількома вчителями.
    """

    full_name = models.CharField(max_length=150)
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="teachers",
        help_text="Предмет, який викладає вчитель",
    )

    class Meta:
        verbose_name = "Вчитель"
        verbose_name_plural = "Вчителі"

    def __str__(self) -> str:
        return f"{self.full_name} ({self.subject.name})"


class SchoolClass(models.Model):
    """Шкільний клас.

    Представляє групу учнів (наприклад, "5‑А" чи "10‑B").
    """

    name = models.CharField(max_length=20, unique=True, help_text="Наприклад, 5‑А або 10‑B")

    class Meta:
        verbose_name = "Клас"
        verbose_name_plural = "Класи"

    def __str__(self) -> str:
        return self.name


class Student(models.Model):
    """Учень.

    Кожен учень має ім’я та відноситься до певного класу. Зв’язок встановлено через
    ForeignKey, що дозволяє одному класу мати багато учнів.
    """

    full_name = models.CharField(max_length=150)
    school_class = models.ForeignKey(
        SchoolClass,
        on_delete=models.CASCADE,
        related_name="students",
        help_text="Клас, у якому навчається учень",
    )

    class Meta:
        verbose_name = "Учень"
        verbose_name_plural = "Учні"

    def __str__(self) -> str:
        return f"{self.full_name} – {self.school_class.name}"