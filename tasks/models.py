from django.db import models

class Task(models.Model):

    STATUS = (
        ('doing', 'Fazendo'),
        ('done', 'Feita'),
    )
    
    title = models.CharField(max_length=250)
    description = models.TextField()
    done = models.CharField(
        max_length=5,
        choices=STATUS,
    )
    create = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)

    def __str__(self):
        return self.title