from django.core.managemente.base import BaseCommand
from marketplace.models import BaseProduct

class Command(BaseCommand):
    def handle(self, *args, **options):
        pass