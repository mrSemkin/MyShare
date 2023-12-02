import logging
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
LOGGER = logging.getLogger(__name__)
User = get_user_model()


class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Beneficiary(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bank_card_number = models.CharField(max_length=16, null=True)


class HelpRequestManager(models.Manager):
    def get_actual_help_requests(self):
        return self.filter(status=HelpRequest.ACTUAL)


class HelpRequestManager(models.Manager):
    def get_actual_help_requests(self):
        return self.filter(status=HelpRequest.ACTUAL)


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

    contain_of_help = models.TextField(max_length=255)
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.PROTECT)

    objects = HelpRequestManager()


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


class UserDonate(models.Model):
    help_request = models.ForeignKey(HelpRequest, on_delete=models.PROTECT)
    count_donate_summ = models.IntegerField(default=0)
    count_donate_times = models.IntegerField(default=0)
    last_donate_date = models.DateField(null=True, blank=True)

    def add_donation(self, amount):
        self.count_donate_summ += amount
        self.count_donate_times += 1
        self.last_donate_date = timezone.now()
        self.save()
        