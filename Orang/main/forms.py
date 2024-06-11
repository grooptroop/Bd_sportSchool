from django import forms
from django.forms import TextInput

from .models import *


class AddGroupaForm(forms.ModelForm):
    class Meta:
        model = Groupa
        fields = "__all__"


class UpdateGroupaForm(forms.ModelForm):
    class Meta:
        model = Groupa
        fields = '__all__'


class AddTreneraForm(forms.ModelForm):
    class Meta:
        model = Trenera
        fields = "__all__"


class UpdateTreneraForm(forms.ModelForm):
    class Meta:
        model = Trenera
        fields = '__all__'

class AddSorevnovaniaForm(forms.ModelForm):
    class Meta:
        model = Sorevnovania
        fields = "__all__"


class UpdateSorevnovaniaForm(forms.ModelForm):
    class Meta:
        model = Sorevnovania
        fields = '__all__'

class AddRoditelForm(forms.ModelForm):
    class Meta:
        model = Roditel
        fields = "__all__"


class UpdateRoditelForm(forms.ModelForm):
    class Meta:
        model = Roditel
        fields = '__all__'


class AddChildrenForm(forms.ModelForm):
    class Meta:
        model = Children
        fields = "__all__"


class UpdateChildrenForm(forms.ModelForm):
    class Meta:
        model = Children
        fields = '__all__'