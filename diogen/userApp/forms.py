from django import forms
#from django import ValidationError
class PersonForm(forms.Form):
    name=forms.CharField(max_length=200, required=True, label='Введите имя:', error_messages={'required': 'Please enter your name'})
    email=forms.EmailField(required=True)
    password=forms.CharField(widget = forms.PasswordInput, required=True)
    password_confirm = forms.CharField(widget = forms.PasswordInput, required=True)
    #if(password!=password_confirm):
    #    ValidationError(_('Пароли не совпадают'), code='invalid')
        
    date=forms.CharField(widget=forms.TextInput(attrs={'class':'datepicker'}), required=True)
    
    #spec=forms.IntegerField()
    #phone=forms.CharField(max_length=20)
    
    description=forms.CharField(widget = forms.Textarea, initial ='')
    image = forms.ImageField(initial ='/pic_folder/None/no_img.jpg')



