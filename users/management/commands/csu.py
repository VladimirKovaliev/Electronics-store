from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admintest@mail.ru',
            first_name='Admin',
            phone='8800553535',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )

        user.set_password('qwerty7586')
        user.save()
        print('created successfully')