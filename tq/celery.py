from celery import Celery

app = Celery('tq')
app.config_from_object('tq.config')
# Auto-discover tasks in the 'tasks' folder
app.autodiscover_tasks(['tq.tasks'])

if __name__ == '__main__':
    app.start()