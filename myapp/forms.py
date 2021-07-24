from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth.models import User
from django.db import models
from django.forms import widgets
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import *

def validate_mobile( value):
    if not (value.isnumeric and (value[0] in [9, 8, 6, 7])):
        raise ValidationError(
            _('%(value)s is not a valid number'),
            params={'value': value},
        )

class UserForm(UserCreationForm):
    address = forms.Textarea()
    mobile = forms.CharField(max_length=10, validators=[validate_mobile])
    profile_pic = forms.ImageField()

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['user']