from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('NORMAL', 'Normal User'),
        ('VENDOR', 'Vendor'),
    )
    
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='NORMAL')
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    # Vendor-specific fields
    store_name = models.CharField(max_length=100, blank=True, null=True)
    is_verified_vendor = models.BooleanField(default=False)
    vendor_description = models.TextField(blank=True, null=True)

    # Override the first_name and last_name fields to make them required
    first_name = models.CharField(_("first name"), max_length=150)
    last_name = models.CharField(_("last name"), max_length=150)

    # Email is already included in AbstractUser, but we'll override it to make it unique
    email = models.EmailField(_("email address"), unique=True)

    def __str__(self):
        return self.username

    def is_vendor(self):
        return self.user_type == 'VENDOR'

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")