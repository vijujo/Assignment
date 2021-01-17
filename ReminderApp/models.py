from django.db import models


class Reminder(models.Model):
    text = models.CharField(max_length=300)
    callback_url = models.URLField()
    delay = models.IntegerField()

    def __str__(self):
        return 'id:%d, text:%s, url:%s, delay:%s' % (self.id, self.text, self.callback_url, self.delay)