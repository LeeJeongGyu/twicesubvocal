from django.db import models

# Create your models here.
class Twice(models.Model):
    name = models.CharField(max_length = 20)
    age = models.IntegerField(default = 0)
    birth = models.DateTimeField()
    nation_choice = (
        ('대한민국', 'Korea'),
        ('일본', 'Japan'),
        ('대만', 'Taiwan')
    )
    nationality = models.CharField(choices = nation_choice, max_length=20)

    position = models.TextField()
    def __str__(self):
        return self.name