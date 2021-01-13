from django.db import models


# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=200)


class Todo(models.Model):
    title = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    created = models.DateTimeField('date created')
    updated = models.DateTimeField('date updated')
    board = models.ForeignKey(Board, on_delete=models.CASCADE)