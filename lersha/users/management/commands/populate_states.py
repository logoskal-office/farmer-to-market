from django.core.management.base import BaseCommand
from users.models import State

state_list = [
    'Addis Ababa',
    'Dire Dawa',
    'Afar',
    'Amhara',
    'Benishangul-Gumuz',
    'Central Ethiopia',
    'Gambela',
    'Harari',
    'Oromia',
    'Sidama',
    'Somali',
    'South Ethiopia',
    'South West Ethiopia',
    'Tigray',
]

class Command(BaseCommand):
    help = 'Populates the database with predefined Ethiopia\'s States.'

    def handle(self, *args, **kwargs):
        self.stdout.write('Populating States...')
        for name in state_list:
            State.objects.get_or_create(name=name)
        self.stdout.write('Completed Populating States')