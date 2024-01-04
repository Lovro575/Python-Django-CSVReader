from django.contrib import admin
from csv_reader.models import User, Vehicle

# Register your models here.

class VehicleInLine(admin.TabularInline):
    model = Vehicle

class UserAdmin(admin.ModelAdmin):
    list_display=('username', 'first_name', 'last_name')
    inlines=[VehicleInLine]


class VehicleAdmin(admin.ModelAdmin):
    list_display=['user', 'truck_number']
    list_filter = ('user',)

admin.site.register(User, UserAdmin)
admin.site.register(Vehicle, VehicleAdmin)