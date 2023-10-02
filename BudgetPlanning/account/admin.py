from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm

from django.contrib.auth.models import Group
admin.site.unregister(Group)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm 
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ('username', 'telegram_id', 'phone_number')
#     list_filter = ('username', 'telegram_id', 'phone_number')
    

    fieldsets = (
    (None, {"fields": ("username", "password")}),
    ("Ruxsatlar", {"fields": ("telegram_id", "phone_number")}),
)

    
    add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ("username","password1","password2","telegram_id","phone_number"),
    }),
)

    search_fields = ("username",)
    ordering = ("username",)

#     filter_horizontal = ()

admin.site.register(CustomUser, CustomUserAdmin)
