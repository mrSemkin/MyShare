import logging
from django.db import models
from django.contrib.auth import get_user_model

LOGGER = logging.getLogger(name)
User = get_user_model()

def str(self):
    return self.username

class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_DEFAULT, primary_key=True)

    def save(self, *args, **kwargs):
        if Donor.objects.filter(user__email=self.user.email).exclude(user_id=self.user_id).exists():
            raise ValidationError("Email вже існує в базі даних.")
        super().save(*args, **kwargs)

class Beneficiary(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_DEFAULT, primary_key=True)
    bank_card_number = models.CharField(max_length=16)

    def save(self, *args, **kwargs):
        if Beneficiary.objects.filter(user__email=self.user.email).exclude(user_id=self.user_id).exists():
            raise ValidationError("Email вже існує в базі даних.")
        if Beneficiary.objects.filter(bank_card_number=self.bank_card_number).exclude(user_id=self.user_id).exists():
            raise ValidationError("Номер банківської картки вже існує в базі даних.")
        super().save(*args, **kwargs)


class Help(models.Model):
    date_of_help = models.DateField()
    kind_of_help = models.CharField(max_length=255)
    status_of_help = models.CharField(max_length=255)
    contain_of_help = models.TextField()
    donor = models.ForeignKey(Donor, on_delete=models.PROTECT)
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