from django.core.management.base import BaseCommand

from core.services import update_vacancy


class Command(BaseCommand):
    help = 'Обновить статусы вакансии hh.ru'

    def handle(self, *args, **options):
        update_vacancy()
