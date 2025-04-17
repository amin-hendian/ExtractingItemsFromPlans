from time import sleep

from celery import shared_task


@shared_task
def first_celery_task(no: int) -> int:
    sleep(10)
    return no * 10
