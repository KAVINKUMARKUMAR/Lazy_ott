from django import forms
from .models import Movie_card,generes_card,Nav_banner,Actor

class AddmovieForm(forms.ModelForm):
    class Meta:
        model = Movie_card
        fields = '__all__'
        widget = {
            "Movie name": forms.TextInput(attrs={'class':'form w-50 ', 'placeholder' :'Product name'}),
            "Movie rating": forms.NumberInput(attrs={'class' : 'form w-50', 'value': 0.00}),
            "img" : forms.TextInput(attrs={'class' : 'form'}),
        }
class AddgenereForm(forms.ModelForm):
    class Meta:
        model = generes_card
        fields = '__all__'
        widget = {
            "name": forms.TextInput(attrs={'class':'form-control w-50 ', 'placeholder' :'Product name'}),
            "price": forms.NumberInput(attrs={'class' : 'form-control w-50', 'value': 0.00}),
            "desc" : forms.TextInput(attrs={'class' : 'form-control'}),
        }
class AddnavForm(forms.ModelForm):
    class Meta:
        model = Nav_banner
        fields = '__all__'
        widget = {
            "name": forms.TextInput(attrs={'class':'form-control w-50 ', 'placeholder' :'Product name'}),
            "price": forms.NumberInput(attrs={'class' : 'form-control w-50', 'value': 0.00}),
            "desc" : forms.TextInput(attrs={'class' : 'form-control'}),
        }
class AddactorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = '__all__'
        widget = {
            "name": forms.TextInput(attrs={'class':'form-control w-50 ', 'placeholder' :'Product name'}),
            "price": forms.NumberInput(attrs={'class' : 'form-control w-50', 'value': 0.00}),
            "desc" : forms.TextInput(attrs={'class' : 'form-control'}),
        }
class EditmovieForm(forms.ModelForm):
    class Meta:
        model = Movie_card
        fields = '__all__'
        widget = {
            "name": forms.TextInput(attrs={'class':'form-control w-50 ', 'placeholder' :'Product name'}),
            "price": forms.NumberInput(attrs={'class' : 'form-control w-50', 'value': 0.00}),
            "desc" : forms.TextInput(attrs={'class' : 'form-control'}),
        }