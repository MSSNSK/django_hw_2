from django.core.management import BaseCommand
from hw2_app.models import Client


class Command(BaseCommand):
    help = "Update customer name by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Customer ID')
        parser.add_argument('name', type=str, help='Customer name')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        customer = Client.objects.filter(pk=pk).first()
        customer.name = name
        customer.save()
        self.stdout.write(f'{customer}')