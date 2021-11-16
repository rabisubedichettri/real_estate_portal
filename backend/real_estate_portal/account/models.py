from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils import timezone
from .validators import AlphanumericValidator

class MyUserManager(BaseUserManager):
    def create_user(self, email,username,gender,first_name,last_name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username.strip(),
            gender=gender,
            first_name=first_name.strip(),
            last_name=last_name.strip(),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,username,gender,first_name,last_name, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        username=username.strip()
        user = self.create_user(
            email,
            username,
            gender,
            first_name.strip(),
            last_name.strip(),
            password,
        )
        user.is_admin = True
        user.is_active=True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    GENDER = (
            ('', 'Select a Gender'),
            ('M', 'Male'),
            ('F', 'Female'),
            ('O', 'Other'),
        )
    username_validator = UnicodeUsernameValidator()

    gender = models.CharField(max_length=3, choices=GENDER)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(
        'username',
        max_length=150,
        unique=True,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[username_validator],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    first_name = models.CharField('first name', max_length=150,validators=[AlphanumericValidator])
    last_name = models.CharField('last name', max_length=150,validators=[AlphanumericValidator])
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField('date joined', default=timezone.now)

    objects = MyUserManager()

    USERNAME_FIELD = 'email' # email and password are by default 'required'
    REQUIRED_FIELDS = ['username','first_name','last_name','gender',]

    def __str__(self):
        return self.email

    def check_Unique_Username(self):
        if self.objects.filter(username=self.username.strip()).exits():
            return False
        return True

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin



