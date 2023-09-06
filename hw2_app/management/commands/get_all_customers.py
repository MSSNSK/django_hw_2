from django.core.management import BaseCommand
from hw2_app.models import Client


class Command(BaseCommand):
    help = "Get all customers."

    def handle(self, *args, **kwargs):
        customers = Client.objects.all()

        self.stdout.write(f'{customers}')