from django.core.management.base import BaseCommand
from users.models import City

city_list = ['Addis Ababa', 'Dire Dawa', 'Bahir Dar']

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for city in city_list:
            City.objects.get_or_create(name=city)
        self.stdout.write(self.style.SUCCESS('Successfully populated cities'))