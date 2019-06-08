from django import forms
#from django import ValidationError
from .models import *
from django.contrib.auth.models import User



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        labels = {
            'first_name':'Имя',
            'last_name':'Фамилия',
        }
        required={
            'first_name':'True',
            'last_name':'True',
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = PersonProfile
        fields = ('birth_date', 'adress', 'phone', 'description','image', 'nickname','genres', 'instruments', 'soundcloud', 'company')
        labels = {
            'birth_date': 'Дата рождения',
            'adress': 'Укажите свой город',
            'phone': 'Телефон',
            'description': 'Расскажите пару слов о себе',

            'nickname': 'Ваш творческий ник:',
            'genres': 'Жанры Вашего творчества',
            'instruments':'Инструменты которыми вы владете',
            'soundcloud':'Ссылка на soundcloud (опционально)',
            'image': 'Ваша пикча',
            'company':'Название вашей компании',
        }
        widgets = {
            'birth_date': forms.TextInput(attrs={'class':'datepicker'}),
            'image': forms.FileInput(attrs={'class': 'avatar'}),
            'description': forms.Textarea(attrs={'class':'materialize-textarea'})
            
        }
        initial = {
            
            'birth_date': ''
        }

class GroupForm(forms.ModelForm):
    class Meta:
        model = GroupProfile
        fields = ['users', 'name']
        widgets = {
            'users':  forms.Select(attrs={'style':'display: flex'})
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = EventProfile
        fields = ('name', 'address', 'description', 'group', 'date')
        labels = {
            'name': 'Наименование события',
            'date': 'Время проведения',
            'address': 'Место проведения',
            'group': 'Выступает',
            #'company': 'Проводит',
            'description': 'Описание'
        }
        widgets = {
            'date': forms.TextInput(attrs={'class':'datepicker'}),
            'description': forms.Textarea(attrs={'class':'materialize-textarea', 'id':'desc'}),
            'company': forms.Select(attrs={'style':'display: flex'}),
            'address': forms.TextInput(attrs={}),
            
        }
        initial = {
            'date': ''
        }



    # def __init__(self, *args, **kwargs):
    #     super(EventForm, self).__init__(*args, **kwargs)
    #     self.fields['company'].queryset = PersonProfile.objects.all()

# class MusicianForm(forms.ModelForm):
#     class Meta:
#         model = MusicianProfile
#         fields = ('nickname', 'genres', 'instruments', 'soundcloud', 'birth_date', 'adress', 'phone', 'description','image')
#         labels = {
#             'nickname': 'Ваш творческий ник:',
#             'genres': 'Жанры Вашего творчества',
#             'instruments':'Инструменты которыми вы владете',
#             'soundcloud':'Ссылка на soundcloud (опционально)',
#             'birth_date': 'Дата рождения',
#             'adress': 'Укажите свой город',
#             'phone': 'Телефон',
#             'description': 'Расскажите пару слов о себе',
#         }
#         widgets = {
#             'birth_date': forms.TextInput(attrs={'class':'datepicker'}),
#         }
#         initial = {
#             'birth_date': ''
#         }
        
# class CompanyForm(forms.ModelForm):
#     class Meta:
#         model = CompanyProfile
#         fields = ('company', 'adress', 'phone', 'description','image')
#         labels = {
#             'company':'Название вашей компании',
#             'birth_date': 'Дата рождения',
#             'adress': 'Укажите свой город',
#             'phone': 'Телефон',
#             'description': 'Расскажите пару слов о себе',
#         }
#         widgets = {
#             'birth_date': forms.TextInput(attrs={'class':'datepicker'}),
#         }
#         initial = {
#             'birth_date': ''
#         }     


'''
class PersonForm(forms.Form):
    

    #name=forms.CharField(required=True, max_length=200, label='Введите имя:', error_messages={'required': 'Please enter your name'})

    #password=forms.CharField(widget = forms.PasswordInput, required=True)
    #confirm_password = forms.CharField(widget = forms.PasswordInput, required=True)
    date=forms.CharField(widget=forms.TextInput(attrs={'class':'datepicker'}), required=True)
    
    #spec=forms.IntegerField()
    #phone=forms.CharField(max_length=20)
    
    description=forms.CharField(widget = forms.Textarea, initial ='', required=False)
    image = forms.ImageField(initial ='/pic_folder/None/no_img.jpg')



  
    def clean_password(self):
        cleaned_data = super(PersonForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
'''

