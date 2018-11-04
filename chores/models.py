from django.db import models
from django.utils import timezone

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    due_date = models.DateTimeField(blank = True, null = True)
    completed = models.BooleanField(default = False)

    def complete(self):
        self.completed = True
        self.save()

    def __str__(self):
        return self.title

class Person(models.Model):
    username = models.CharField(max_length = 15)
    passworld = models.CharField(max_length = 25)
    name = models.CharField(max_length = 15)
    color = models.CharField(max_length = 7)
    tasks = []
    friends = []

    def addTask(self, task):
        tasks.append(task)
        self.save()

    def addFriend(self, friend):
        friends.append(friend)
        self.save()

    def __str__(self):
        return self.name
