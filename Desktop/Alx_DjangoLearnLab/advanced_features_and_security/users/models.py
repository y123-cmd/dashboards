# users/models.py
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, date_of_birth, profile_photo, password=None):
        """
        Creates and returns a regular user with email, username, date_of_birth, and profile_photo.
        """
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, date_of_birth=date_of_birth, profile_photo=profile_photo)
        user.set_password(password)  # Hash the password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, date_of_birth, profile_photo, password=None):
        """
        Creates and returns a superuser with email, username, date_of_birth, profile_photo.
        """
        user = self.create_user(
            email=email,
            username=username,
            date_of_birth=date_of_birth,
            profile_photo=profile_photo,
            password=password,
        )
        user.is_staff = True  # Superuser can access the admin panel
        user.is_superuser = True  # Superuser is an admin
        user.save(using=self._db)
        return user

# Custom User Model
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    # Add the custom manager
    objects = CustomUserManager()

    def __str__(self):
        return self.username

