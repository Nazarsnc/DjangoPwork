from django.db import models

class Poll(models.Model):
    POLL_TOPICS = [
        ('society', 'Суспільство'),
        ('technology', 'Технології'),
        ('education', 'Освіта'),
        ('politics', 'Політика'),
        ('other', 'Інше'),
    ]

    title = models.CharField("Назва опитування", max_length=200)
    description = models.TextField("Опис опитування", blank=True)
    created_date = models.DateField("Дата створення", auto_now_add=True)
    is_active = models.BooleanField("Активне?", default=True)
    category = models.CharField("Категорія", max_length=50, choices=POLL_TOPICS, default='other')
    allow_anonymous = models.BooleanField("Анонімне голосування?", default=True)
    min_age = models.PositiveIntegerField("Мінімальний вік", default=18)
    votes_count = models.PositiveIntegerField("Кількість голосів", default=0)

    def __str__(self):
        return self.title


class Vote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, verbose_name="Опитування")
    choice = models.CharField("Вибраний варіант", max_length=100)
    voted_at = models.DateTimeField("Час голосування", auto_now_add=True)

    def __str__(self):
        return f"Голос за: {self.choice}"
