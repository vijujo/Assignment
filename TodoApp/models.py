from django.db import models


class Board(models.Model):
    name = models.CharField(max_length=200)


class Todo(models.Model):
    title = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    created = models.DateTimeField('date created')
    updated = models.DateTimeField('date updated')
    board = models.ForeignKey(Board, related_name='todos',on_delete=models.CASCADE)

    def __str__(self):
        return '%s, %s, %s, %s' % (self.title, self.done, self.created, self.updated)