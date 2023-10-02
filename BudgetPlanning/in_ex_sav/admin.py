from django.contrib import admin

from .models import Income, Expence, Savings
# Register your models here.
admin.site.register(Income)
admin.site.register(Expence)
admin.site.register(Savings)
