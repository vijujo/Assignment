from Assignment.celery import app
import requests


@app.task
def post_reminder(text, callback_url):
    x = requests.post(callback_url, data={'reminder': text})
    print(x.text)
