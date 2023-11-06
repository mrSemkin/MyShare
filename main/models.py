import logging
from django.db import models
from django.contrib.auth import get_user_model

LOGGER = logging.getLogger(__name__)
User = get_user_model()


class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Beneficiary(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bank_card_number = models.CharField(max_length=16, unique=True)
    objects = models.Manager()


class HelpRequest(models.Model):
    FINANCIAL = "Financial"
    MATERIAL = "Material"
    SUPPORT_TYPES = [
        (FINANCIAL, "Фінансова допомога"),
        (MATERIAL, "Матеріальна допомога"),
    ]
    ACTUAL = "ACTUAL"
    PROVIDED = "PROVIDED"
    STATUSES = [
        (ACTUAL, "Актуальна"),
        (PROVIDED, "Завершена"),
    ]

    support_type = models.CharField(
        max_length=64,
        choices=SUPPORT_TYPES,
        default=FINANCIAL
    )
    status = models.CharField(
        max_length=64,
        choices=STATUSES,
        default=ACTUAL
    )

    contain_of_help = models.TextField()
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.PROTECT)


class Help(models.Model):
    EXPECTED = "EXPECTED"
    CONFIRMED = "CONFIRMED"
    PROVIDED = "PROVIDED"
    STATUSES = [
        (EXPECTED, "Очікується допомога"),
        (PROVIDED, "Допомога надана"),
        (CONFIRMED, "Допомога підтверджена"),
    ]

    status = models.CharField(
        max_length=64,
        choices=STATUSES,
        default=EXPECTED
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    donor = models.ForeignKey(Donor, on_delete=models.PROTECT)
    help_request = models.ForeignKey(HelpRequest, on_delete=models.PROTECT)
