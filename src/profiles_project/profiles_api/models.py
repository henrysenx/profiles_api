from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# Create your models here.

class UserProfileManager(BaseUserManager):
    """Helps Django work with our custom user model"""

    def create_user(self, name, email, password):
        """creates a new user profile"""

        if not email:
            raise ValueError('User must have an email')
        
        email = self.normalize_email(email)

        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, name, email, password):
        """creates a new superuser with given details"""

        user = self.create_user(email, name, password)
        
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represent a user profile inside our system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Used to get the user full name"""

        return self.name
    
    def get_short_name(self):
        """Used to get the user short name"""

        return self.name
    
    def __str__(self):
        """Django uses this when it needs to convert the object to a string"""

        return self.email

