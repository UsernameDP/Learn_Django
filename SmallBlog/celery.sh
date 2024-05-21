#!/bin/sh

celery -A SmallBlog worker -l info &
celery -A SmallBlog beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler