from django.forms import ModelForm
from auth_app.models import SecretUser
from django import forms

class Secretuser_Form(ModelForm):
    class Meta:
        model = SecretUser
        fields = ['hobby', 'fav_food', 'hap_moment', 'fun_moment', 'child_dream', 'job_desc', 'teen_photo']

        textinput = forms.TextInput()

        widgets = {
            "hobby": textinput,
            "fav_food": textinput,
            "hap_moment": textinput,
            "fun_moment": textinput,
            "child_dream": textinput,
            'job_desc': textinput,
        }
