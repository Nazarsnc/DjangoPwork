from django.db import models

class Poll(models.Model):
    ТЕМИ_ОПИТУВАНЬ = [
        ('суспільство', 'Суспільство'),
        ('технології', 'Технології'),
        ('освіта', 'Освіта'),
        ('політика', 'Політика'),
        ('інше', 'Інше'),
    ]

    назва = models.CharField("Назва опитування", max_length=200)
    опис = models.TextField("Опис опитування", blank=True)
    дата_створення = models.DateField("Дата створення", auto_now_add=True)
    активне = models.BooleanField("Активне?", default=True)
    категорія = models.CharField("Категорія", max_length=50, choices=ТЕМИ_ОПИТУВАНЬ, default='інше')
    дозволено_анонімно = models.BooleanField("Анонімне голосування?", default=True)
    мін_вік = models.PositiveIntegerField("Мінімальний вік", default=18)
    кількість_голосів = models.PositiveIntegerField("Кількість голосів", default=0)

    def __str__(self):
        return self.назва


class Vote(models.Model):
    опитування = models.ForeignKey(Poll, on_delete=models.CASCADE, verbose_name="Опитування")
    варіант = models.CharField("Вибраний варіант", max_length=100)
    дата_голосування = models.DateTimeField("Час голосування", auto_now_add=True)


    def __str__(self):
        return f"Голос за: {self.варіант}"
