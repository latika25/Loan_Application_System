from django import forms
from .models import LoanApplication
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from django import forms
from .models import LoanApplication, BalanceSheetEntry,LoanApplication2

class LoanApplicationForm(forms.ModelForm):
    class Meta:
        model = LoanApplication
        fields = [
            'business_name',
            'year_established',
            'requested_loan_amount',
        ]

class BalanceSheetEntryForm(forms.ModelForm):
    class Meta:
        model = BalanceSheetEntry
        fields = [
            'year',
            'month',
            'profit_or_loss',
            'assets_value',
            # Add other fields as needed
        ]

class LoanApplicationForm2(forms.ModelForm):
    class Meta:
        model = LoanApplication2
        fields = [
            'user',
            'business_name',
            'requested_loan_amount',
            'has_profit_last_12_months',
            'average_asset_value',
        ]





# class ServiceRequestForm(ModelForm):
#     class Meta:
#         model = ServiceRequest
#         fields = ['request_type', 'details','attachment'
#                   ]
        

class SignUpForm(UserCreationForm):
    # My Own Custom Fields
    username = forms.CharField(widget= forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    first_name = forms.CharField(widget= forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), max_length=32, help_text='First name')
    last_name=forms.CharField(widget= forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), max_length=32, help_text='Last name')
    email=forms.EmailField(widget= forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), max_length=64, help_text='Enter a valid email address')
    password1=forms.CharField(widget= forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    # password2=forms.CharField(forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}))

    # The Default Fields Of The UserCreation Form
    class Meta(UserCreationForm.Meta):
        model = User
        # I've tried both of these 'fields' declaration, result is the same
        # fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)


