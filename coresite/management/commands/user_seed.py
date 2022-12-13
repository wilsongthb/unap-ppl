from django.core.management.base import BaseCommand
import random
from django.contrib.auth.models import User

# python manage.py seed --mode=refresh

""" Clear all data and creates addresses  """""
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object  """""
MODE_CLEAR = 'clear'


class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        pass
        #  parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        #  run_seed(self, options['mode'])
        run_seed(self)
        self.stdout.write('done.')

def run_seed(self):
    user=User.objects.create_user('admin@email.com',password='secret')
    user.is_superuser=True
    user.is_staff=True
    user.save()
