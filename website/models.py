from django.db import models

class Categorias(models.TextChoices):
    TECH = 'TC', 'Tecnologia'
    CR = 'CR', 'Curiosidades'
    GR = 'GR', 'Gerais'

class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    content = models.TextField()
    categories = models.CharField(max_length=2, 
                                  choices=Categorias.choices, 
                                  default=Categorias.GR)
    image = models.ImageField(upload_to="posts", null=True, blank=True)

    def __str__(self):
        return self.title
