from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

import logging
logger = logging.getLogger(__name__)

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where username is the unique identifiers
    for authentication instead of email.
    """
    def create_user(self, username, password=None, **extra_fields):
        """
        Create and save a user with the given username and password.
        """
        try:
            if not username:
                raise ValueError(_("The username must be set"))
            # username = self.normalize_username(username)
            user = self.model(username=username, **extra_fields)
            user.set_password(password)
            user.save()
            # logger.info("User created successfully.")
            return user
        except Exception as e:
            logger.error(f"Error creating user: {e}")


    def create_superuser(self, username, password=None, **extra_fields):
        """
        Create and save a SuperUser with the given username and password.
        """
        # extra_fields.setdefault("role", 0)
        try:
            extra_fields.setdefault("is_staff", True)
            extra_fields.setdefault("is_superuser", True)
            extra_fields.setdefault("is_active", True)

            if extra_fields.get("is_staff") is not True:
                raise ValueError(_("Superuser must have is_staff=True."))
            if extra_fields.get("is_superuser") is not True:
                raise ValueError(_("Superuser must have is_superuser=True."))
            logger.info("User created successfully.")
            return self.create_user(username, password, **extra_fields)
        except Exception as e:
                logger.error(f"Error creating user: {e}")