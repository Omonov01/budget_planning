from django.db import models
from account.models import CustomUser

from django.utils.translation import  gettext_lazy as _
# Create your models here.

class Income(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, 
                             related_name="users_income", verbose_name=_("Foydalanuvchi"))
    income_name = models.CharField(max_length=250, null=True, blank=True, verbose_name=_("Kirim manbaalari"))


class Expence(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, 
                             related_name="users_expence", verbose_name=_("Foydalanuvchi"))
    expence_name = models.CharField(max_length=250, null=True, blank=True, verbose_name=_("chiqim manbaalari"))

class Savings(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, 
                             related_name="users_savings", verbose_name=_("Foydalanuvchi"))
    savings_name = models.CharField(max_length=250, null=True, blank=True, verbose_name=_("Saqlash manbaalari"))    