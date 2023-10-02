from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField

from .managers import CustomUserManager
# Create your models here.

class CustomUser(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(unique=True, max_length=30, null=True, blank=True, verbose_name=_('Username'))
    telegram_id = models.CharField(primary_key=True, default=0, verbose_name=_("Telegram id"))
    phone_number = PhoneNumberField(region='UZ', null=True, blank=True, verbose_name=_("Telefon raqami"))
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)  
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        try:
            if kwargs['password']:
                self.set_password(kwargs['password'])
        except Exception:
            pass
        finally:
            super(CustomUser, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.username}"
    
    class Meta:
        db_table = 'useraccount'
        verbose_name = _('Foydalanuvchi')
        verbose_name_plural = _('Foydalanuvchilar')
