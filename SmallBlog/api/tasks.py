from celery import Celery
from celery.schedules import crontab
from celery import shared_task
from .models import BlogPost
from django.utils import timezone
from datetime import timedelta
import pytz


@shared_task
def update_blog_dates():

    ny_timezone = pytz.timezone("America/New_York")

    for blog in BlogPost.objects.all():
        new_date = timezone.now().astimezone(ny_timezone)
        blog.date = new_date.date()
        blog.save()
