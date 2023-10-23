from django import forms
from .models import Donor, Beneficiary, Help, Supplier, Sponsor
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class NewDonorForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Donor
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewDonorForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Donor.objects.create(user=user)
        return user


class NewBeneficiaryForm(UserCreationForm):
    email = forms.EmailField(required=True)
    bank_card_number = forms.CharField(max_length=16)

    class Meta:
        model = Beneficiary
        fields = ("username", "email", "password1", "password2", "bank_card_number")

    def save(self, commit=True):
        user = super(NewBeneficiaryForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Beneficiary.objects.create(user=user, bank_card_number=self.cleaned_data['bank_card_number'])
        return user


class HelpForm(forms.ModelForm):
    class Meta:
        model = Help
        fields = ['date_of_help', 'kind_of_help', 'status_of_help', 'contain_of_help', 'donor', 'beneficiary']


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['company_name', 'contact_person', 'email', 'phone_num', 'address_optional', 'helps']


class SponsorProfileForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = ['description']


class DonorAuthenticationForm(AuthenticationForm):
    class Meta:
        model = Donor
        fields = ["username", "password"]


class BeneficiaryAuthenticationForm(AuthenticationForm):
    class Meta:
        model = Beneficiary
        fields = ["username", "password"]