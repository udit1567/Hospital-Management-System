from celery_worker import celery


@celery.task
def send_reminder():

    print("Sending appointment reminders")