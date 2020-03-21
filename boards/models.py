from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Card(models.Model):
    card_name = models.CharField(max_length=16, default="card")
    content = models.CharField(max_length=64, default="card")
    image = models.ImageField(null=True)
    file = models.FileField(null=True)
    link = models.URLField(null=True)


class List(models.Model):
    list_name = models.CharField(max_length=16, default="list")
    cards = models.ManyToManyField(Card, related_name="card")


class PersonalBoard(models.Model):
    lists = models.ManyToManyField(List, related_name="list")
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class TeamBoard(models.Model):
    members = models.ManyToManyField(User, related_name="member")
    admins = models.ManyToManyField(User, related_name="admin")
    name = models.CharField(max_length=16, default="Board")
    lists = models.ManyToManyField(List)
