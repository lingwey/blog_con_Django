from django import forms
from .models import Comentario

class EmailPostForm(forms.Form):
    nombre = forms.CharField(max_length=25)
    email= forms.EmailField()
    to = forms.EmailField()
    comentarios= forms.CharField(required=False, widget=forms.Textarea)
  
class ComentariosForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nombre', 'email', 'cuerpo']  
    
class SearchForm(forms.Form):
    query = forms.CharField()