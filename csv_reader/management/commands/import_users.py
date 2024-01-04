from django.core.management import BaseCommand
from django.contrib.auth import get_user_model
import csv

User = get_user_model()

class Command(BaseCommand):

    help = "Imports users from users.csv"


    def handle(self, *args, **options):

        with open('./users.csv', 'r') as file:
            reader = csv.DictReader(file, delimiter='\t')
            for row in reader:
                username = row['username']
                first_name = row['firstname']
                last_name = row['lastname']

                try:
                    #check if the user exists
                    user = User.objects.get(username=username)

                    #update the first and last names of existing users
                    user.first_name = first_name
                    user.last_name = last_name
                    user.save()
                except User.DoesNotExist:
                    #create a new user
                    User.objects.create(username=username, first_name=first_name, last_name=last_name)