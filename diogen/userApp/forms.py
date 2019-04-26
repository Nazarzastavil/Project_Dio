from django import forms
#from django import ValidationError
from .models import *
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = PersonProfile
        fields = ('birth_date', 'adress', 'phone', 'description','image')
        labels = {
            'birth_date': 'Дата рождения',
            'adress': 'Укажите свой город',
            'phone': 'Телефон',
            'description': 'Расскажите пару слов о себе'
        }
        widgets = {
            'birth_date': forms.TextInput(attrs={'class':'datepicker'}),
        }

class PersonForm(forms.Form):
    

    #name=forms.CharField(required=True, max_length=200, label='Введите имя:', error_messages={'required': 'Please enter your name'})

    #password=forms.CharField(widget = forms.PasswordInput, required=True)
    #confirm_password = forms.CharField(widget = forms.PasswordInput, required=True)
    date=forms.CharField(widget=forms.TextInput(attrs={'class':'datepicker'}), required=True)
    
    #spec=forms.IntegerField()
    #phone=forms.CharField(max_length=20)
    
    description=forms.CharField(widget = forms.Textarea, initial ='', required=False)
    image = forms.ImageField(initial ='/pic_folder/None/no_img.jpg')



    '''
    def clean_password(self):
        cleaned_data = super(PersonForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
    '''
