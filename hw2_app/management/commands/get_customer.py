from django.core.management import BaseCommand
from hw2_app.models import Client


class Command(BaseCommand):
    help = 'Get customer by ID'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Customer ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        customer = Client.objects.get(pk=pk)

        self.stdout.write(f'{customer}')
