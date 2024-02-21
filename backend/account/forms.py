from django.contrib.auth.forms import BaseUserCreationForm
from django.contrib.auth import get_user_model
from django.forms import EmailField
from django.forms import ModelForm

class CustomUserCreationForm(BaseUserCreationForm):
    class Meta:
        model = get_user_model() 
        fields = ('email',)
        field_classes = {"email": EmailField}

class CustomUserForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = "__all__"
