from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from .utils import unique_random_code


class Card(models.Model):
    name = models.CharField(max_length=16, default="card")
    content = models.CharField(max_length=64, default="card")
    image = models.ImageField(null=True)
    file = models.FileField(null=True)
    link = models.URLField(null=True)
    obj_id = models.CharField(max_length=64)

    def __str__(self):
        return self.obj_id


def pre_save_card(sender, instance, **kwargs):
    if instance._state.adding is True:
        instance.obj_id = unique_random_code(instance)


pre_save.connect(pre_save_card, sender=Card)


class List(models.Model):
    name = models.CharField(max_length=16, default="list")
    cards = models.ManyToManyField(Card, related_name="card")
    obj_id = models.CharField(max_length=32)

    def __str__(self):
        return self.obj_id


def pre_save_list(sender, instance, **kwargs):
    if instance._state.adding is True:
        instance.obj_id = unique_random_code(instance)


pre_save.connect(pre_save_list, sender=List)


def post_save_list(sender, instance, created, **kwargs):
    if created:
        card = Card.objects.create(name="Task")
        instance.cards.add(card)


post_save.connect(post_save_list, sender=List)


class Board(models.Model):
    personal_board = models.BooleanField(default=False)
    description = models.CharField(max_length=128, blank=True)
    members = models.ManyToManyField(User, related_name="member", blank=True)
    admins = models.ManyToManyField(User, related_name="admin", blank=True)
    name = models.CharField(max_length=16, default="Board")
    lists = models.ManyToManyField(List, blank=True, related_name="list")
    obj_id = models.CharField(max_length=16, default="NULL")

    def __str__(self):
        return self.obj_id


def pre_save_board(sender, instance, **kwargs):
    if instance._state.adding is True:
        instance.obj_id = unique_random_code(instance)


pre_save.connect(pre_save_board, sender=Board)


def post_save_board(sender, instance, created, **kwargs):
    if created:
        list1 = List.objects.create(name="To Do")
        instance.lists.add(list1)
        list2 = List.objects.create(name="In Progress")
        list3 = List.objects.create(name="Completed")
        instance.lists.add(list2)
        instance.lists.add(list3)


post_save.connect(post_save_board, sender=Board)
