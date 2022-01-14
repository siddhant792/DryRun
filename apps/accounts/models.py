from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    """
    Custom User Manager class
    """

    def create_user(self, email, password, is_staff=False, is_admin=False):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.is_staff = is_staff
        user.is_admin = is_admin
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        return self.create_user(email, password, True, False)

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        return self.create_user(email, password, True, True)


class User(AbstractBaseUser):
    """
    Custom user class
    """

    GENDER_CHOICE = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    ]
    email = models.EmailField(unique=True, help_text='Email Address', max_length=50)
    username = models.CharField(unique=True, help_text='Username', max_length=50)
    name = models.CharField(max_length=50, help_text="Name of User")
    is_staff = models.BooleanField(default=False, help_text="This user can access admin panel")
    is_admin = models.BooleanField(
        default=False, help_text="This user has all permissions without explicitly assigning them"
    )
    gender = models.CharField(choices=GENDER_CHOICE, max_length=50, help_text="Gender of the user", null=True, blank=True)
    password = models.CharField(max_length=150)
    location = models.CharField(max_length=200, help_text="Location of the user", blank=True)
    summary = models.CharField(max_length=500, help_text="Summary of the user", blank=True)
    date_of_birth = models.DateField(help_text="Date of Birth of the user", null=True, blank=True)
    website = models.CharField(max_length=100, help_text="Website of the user", blank=True)
    education = models.CharField(max_length=150, help_text="Education of the user", blank=True)
    work = models.CharField(max_length=100, help_text="Work of the user", blank=True)
    profile_pic = models.CharField(max_length=300, help_text="Profile pic url of the user", blank=True)
    skills = models.CharField(max_length=1000, help_text="Skill set of the user", default="[]")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'

    def get_name(self):
        # The user is identified by their name
        return f"{self.name}"

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    # def save(self, *args, **kwargs):
    #     self.password = make_password(self.password)
    #     super(User, self).save(*args, **kwargs)
