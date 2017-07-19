from __future__ import unicode_literals

from django import forms


class AccountForm(forms.ModelForm):
    class Meta:
        password = forms.CharField(widget=forms.PasswordInput)
        model = Account
        widgets = {
            'password' : forms.PasswordInput(),
        }