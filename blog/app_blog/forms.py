from django import forms

class EmailPostForm(forms.Form):
    nombre = forms.CharField(max_length=25)
    email= forms.EmailField()
    to = forms.EmailField()
    comentarios= forms.ChoiceField(required=False)
    widget=forms.Textarea()
    