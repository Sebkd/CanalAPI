"""
Модуль предназначен для команды периодического опроса
"""

from django.core.management.base import BaseCommand, CommandError
from django_celery_beat.models import PeriodicTask, IntervalSchedule