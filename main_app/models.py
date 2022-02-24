from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    #changes to instance methods do not require re-generation / running migrations
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'game_id': self.id})