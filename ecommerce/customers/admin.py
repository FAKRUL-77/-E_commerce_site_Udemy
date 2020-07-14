from django.contrib import admin
from .models import Customer

# Register your models here.

#
# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ['__str__']
#
#     class Meta:
#         model = Customer


admin.site.register(Customer)