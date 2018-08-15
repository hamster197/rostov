from django import forms
from django.core.exceptions import ValidationError


class UsdImputForm(forms.Form):
    usd_value = forms.DecimalField(help_text='Например 55.55', decimal_places=2, label='Введите сумму в USD:', min_value=0)
