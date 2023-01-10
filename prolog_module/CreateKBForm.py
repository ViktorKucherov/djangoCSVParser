from django import forms


class CreateKBForm(forms.Form):
    kb_name = forms.CharField(name="kb_name", max_length=100)
