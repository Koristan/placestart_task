from django.db import models

COLOR_CHOICES = {
    'red': 'Высокий',
    'yellow': 'Средний',
    'green': 'Низкий',
}

STATUS = {
    "Ожидает выполнения":"Ожидает выполнения",
    "Выполнена":"Выполнена",
    "В процессе выполнения":"В процессе выполнения",
}

class Tasks(models.Model):
    datetime_start = models.DateTimeField("Дата и время создания")
    datetime_deadline = models.DateTimeField("Дата и время к которому должна быть выполнена")
    priority = models.CharField("Приоритет", max_length=7, choices=COLOR_CHOICES, default="Низкий")
    status = models.CharField("Статус", max_length=21, choices=STATUS, default="Ожидает выполнения")
    task_name = models.CharField("Название задачи", max_length=50)
    task_description = models.TextField("Описание задачи")

    def __str__(self):
        return self.task_name

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
