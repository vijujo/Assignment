from django.db import models


class Board(models.Model):
    name = models.CharField(max_length=200)


class Todo(models.Model):
    title = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    board = models.ForeignKey(Board, related_name='todos',on_delete=models.CASCADE)

    def __str__(self):
        return 'id:%d  title:%s, done:%s, created on:%s, updated on: %s' % (self.id, self.title, self.done, self.created, self.updated)
