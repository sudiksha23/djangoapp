from django import forms 
from .models import EntrySignup
  
class EntrySignupForm(forms.ModelForm): 
    
    class Meta: 
        model = EntrySignup
        fields = ['uname','psw','fname','lname','country','city','state','zipp','gender','interested_in','marital_status','religion','occupation','education_status','subject','dob','dp'] 
