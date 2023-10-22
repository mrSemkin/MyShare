import logging
from django.db import models
from django.contrib.auth import get_user_model

LOGGER = logging.getLogger(__name__)
User = get_user_model()


class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_DEFAULT, primary_key=True)


class Beneficiary(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_DEFAULT, primary_key=True)
    bank_card_number = models.CharField(max_length=16)


class Help(models.Model):
    date_of_help = models.DateField()
    kind_of_help = models.CharField(max_length=255)
    status_of_help = models.CharField(max_length=255)
    contain_of_help = models.TextField()
    donor = models.ForeignKey(Donor, on_delete=models.PROTECT)
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.PROTECT)


class Supplier(models.Model):
    company_name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField()
    phone_num = models.CharField(max_length=15)
    address_optional = models.CharField(max_length=255)
    helps = models.ManyToManyField(Help, related_name='suppliers')


class Sponsor(models.Model):
    company_name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField()
    phone_num = models.CharField(max_length=15)
    address_optional = models.CharField(max_length=255)
    type_of_help = models.CharField(max_length=255)
    helps = models.ManyToManyField(Help, related_name='sponsors')
