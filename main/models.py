from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Поле Email повинно бути заповненим')
        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Add your custom fields here
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone_num = models.CharField(max_length=15)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def str(self):
        return self.username

    # Add related_name to groups and user_permissions
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='custom_users',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_users_permissions',
    )


class Benefactor(CustomUser):
    pass


class Beneficiary(CustomUser):
    pass


class Help(models.Model):
    date_of_help = models.DateField()
    kind_of_help = models.CharField(max_length=255)
    status_of_help = models.CharField(max_length=255)
    contain_of_help = models.TextField()
    benefactor = models.ForeignKey(Benefactor, on_delete=models.PROTECT)
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.PROTECT)


class Suppliers(models.Model):
    company_name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField()
    phone_num = models.CharField(max_length=15)
    address_optional = models.CharField(max_length=255)
    helps = models.ManyToManyField(Help, related_name='suppliers')


class Sponsors(models.Model):
    company_name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField()
    phone_num = models.CharField(max_length=15)
    address_optional = models.CharField(max_length=255)
    type_of_help = models.CharField(max_length=255)
    helps = models.ManyToManyField(Help, related_name='sponsors')