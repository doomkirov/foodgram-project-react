from csv import DictReader

from django.core.management import BaseCommand
from django.db.utils import IntegrityError

from foodgram_api import settings
from recipes.models import Ingridient


def print_error(error, row):
    print('Error:', error.args, '\nRow ID:', row.get('id'))


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Удаляем старые данные...')
        Ingridient.objects.all().delete()
        self.stdout.write(self.style.NOTICE('Заполняем базу данных...'))

        with open(
                f'{settings.BASE_DIR}/../data/ingredients.csv',
                mode='r',
                encoding='utf-8',
        ) as table:
            reader = DictReader(table)
            for row in reader:
                try:
                    Ingridient.objects.get_or_create(**row)
                except IntegrityError as error:
                    print_error(error, row)
                except ValueError as error:
                    print_error(error, row)
        self.stdout.write(self.style.SUCCESS('Успешно!'))
