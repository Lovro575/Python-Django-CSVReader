from django.core.management import BaseCommand
from django.contrib.auth import get_user_model
from ...models import Vehicle
import csv

User = get_user_model()

class Command(BaseCommand):

    help = "Imports vehicles from vehicles.csv"

    def handle(self, *args, **kwargs):

        #clear all existing vehicles
        Vehicle.objects.all().delete()

        with open('./vehicles.csv', 'r', newline='') as file:
            reader = csv.DictReader(file)
            # Dictionary to store the latest vehicle for each truck_number
            vehicles_to_save = {} 
            for row in reader:
                try:
                    user = User.objects.get(username=row['username'])
                    truck_number = row['truck_number']
                    
                    if truck_number == 'NaN':
                        self.stderr.write(self.style.ERROR('Truck number not found'))
                    else:
                        # Create or update the vehicle for each truck_number
                        vehicles_to_save[truck_number] = {'user': user, 'truck_number': truck_number}
                except Exception as error:
                    print("Error", error)
            # Save the latest vehicle for each truck_number
            for truck_number, values in vehicles_to_save.items():
                user = values['user']
                truck_number = values['truck_number']
                vehicle = Vehicle.objects.update_or_create(
                    user=user,
                    truck_number=truck_number,
                )