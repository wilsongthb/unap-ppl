from django.core.management.base import BaseCommand
import marketplace.models as models
import csv
from django.conf import settings
import os

class Command(BaseCommand):
    def handle(self, *args, **options):
        seed_map_markers()


def seed_map_markers():
    with open(os.path.join(settings.BASE_DIR, 'marketplace/data/map-markers.csv'), newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',',quotechar='"')
        i = 1
        for row in spamreader:
            print(row)
            if i > 1:
                models.MapMark.objects.create(
                    label=row[0],
                    title=row[1],
                    lat=row[2],
                    lng=row[3],
                    type=row[4]
                )
            i += 1
