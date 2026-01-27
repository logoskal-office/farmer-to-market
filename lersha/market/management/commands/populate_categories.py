from django.core.management.base import BaseCommand
from market.models import Category

category_list = [
    ['Dairy', 'categories/dairy.jpg'],
    ['Vegetables', 'categories/vegetables.jpg'],
    ['Fruits', 'categories/fruits.jpg'],
    ['Livestock', 'categories/livestock.jpg'],
    ['Meats', 'categories/meats.jpg'],
    ['Herbs', 'categories/herbs.jpg'],
    ['Grains', 'categories/grains.jpg'],
    ['Oilseeds', 'categories/oilseeds.jpg'],
    ['Other', 'categories/others.jpg'],
]

class Command(BaseCommand):
    help = 'Populates the database with predefined product categories.'

    def handle(self, *args, **kwargs):
        self.stdout.write('Populating Categories...')
        for category in category_list:
            name, image_path = category
            Category.objects.get_or_create(name=name, image=image_path)
        self.stdout.write('Completed Populating Categories')