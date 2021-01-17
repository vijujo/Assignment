from celery import Celery

app = Celery('tasks', broker='amqp://localhost')


@app.task(name='ReminderApp.post_reminder')
def post_reminder(text, callback_url):
    return text + callback_url
