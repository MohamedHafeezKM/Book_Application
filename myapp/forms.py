from django.forms import ModelForm,Form,CharField,DateField,IntegerField,ImageField,TextInput,Textarea,DateInput,NumberInput,PasswordInput,EmailInput
from myapp.models import Books
from django.contrib.auth.models import User
# class BookAdd(Form):
#     name=CharField()
#     author=CharField()
#     catogary=CharField()
#     published_date=DateField()
#     pages=IntegerField()
#     # cover=ImageField()
#     rating=CharField()
    
class BookAddModelForm(ModelForm):
    class Meta:
        model=Books
        fields='__all__'

        widgets={
            'name':Textarea(attrs={'class':'form-control','rows':2}),
            'author':TextInput(attrs={'class':'form-control'}),
            'catogary':TextInput(attrs={'class':'form-control'}),
            'published_date':DateInput(attrs={'class':'form-control','type':'date'}),
            'pages':NumberInput(attrs={'class':'form-control'}),
            # 'rating':TextInput(attrs={'class':'form-control'})

        }


class RegisterationForm(ModelForm):
    class Meta:
     model=User
     fields=['username','password','email']
     widgets={
        'username':TextInput(attrs={'class':'form-control'}),
        'password':PasswordInput(attrs={'class':'form-control'}),
        'email':EmailInput(attrs={'class':'form-control'})
        }
     
class SignInForm(Form):
   username=CharField(widget=TextInput(attrs={'class':'form-control'}))
   password=CharField(widget=PasswordInput(attrs={'class':'form-control'}))