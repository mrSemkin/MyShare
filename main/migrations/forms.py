from django import forms
from .models import Donor, Beneficiary, Help, Supplier, Sponsor


class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['user']


class BeneficiaryForm(forms.ModelForm):
    class Meta:
        model = Beneficiary
        fields = ['user', 'bank_card_number']


class HelpForm(forms.ModelForm):
    class Meta:
        model = Help
        fields = ['date_of_help', 'kind_of_help', 'status_of_help', 'contain_of_help', 'donor', 'beneficiary']


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['company_name', 'contact_person', 'email', 'phone_num', 'address_optional', 'helps']


class SponsorForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = ['company_name', 'contact_person', 'email', 'phone_num', 'address_optional', 'type_of_help', 'helps']

