from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
import os
from django.core.validators import RegexValidator
# from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

GENDER_SELECTION = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('NS', 'Not Specified'),
]
ROLES = [(1, 'Admin'), (2, 'User')]


def validate_image(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    ext = ext.strip()
    valid_extensions = ['.jpg', '.jpeg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError("Unsupported file extension....")
    return value

class CustomUser(AbstractUser):
    # We don't need to define the email attribute because is inherited from AbstractUser
    gender = models.CharField(max_length=20, choices=GENDER_SELECTION)
    phone_number = models.CharField(max_length=15) 

    # phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    # phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)
    # phoneNumber = PhoneNumberField(unique = True, null = False, blank = False) # Here


    role = models.IntegerField(choices=ROLES, default=2)
    email_verified = models.BooleanField(default=False)
    forget_password_token = models.TextField(null=True, blank=True)
    token_expire_time = models.DateTimeField(null=True, blank=True)
    profile_title = models.CharField(max_length=200, null=True, blank=True)
    profile_description = models.TextField(null=True, blank=True)
    profile_img = models.ImageField(upload_to='user_profile_images/', null=True, blank=True,
                                    validators=[validate_image])
