from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.utils.log import get_task_logger
from accounts.email import send_confirmation_mail

logger = get_task_logger(__name__)

@shared_task(name="send_confirmation_mail_task")
def send_confirmation_mail_task(username, email):
    """
    This function used to peform celery task
    """
    print("task me ", username, email)
    logger.info("Sent Confirmation Email")
    return send_confirmation_mail(username, email)