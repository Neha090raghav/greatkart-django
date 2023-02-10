from django import forms
from .models import Account
class RegistrationForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter Password',
        
    }))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm Password'
    }))
    class Meta:
        model=Account
        fields=['first_name','last_name','phone_number','email','password']
    def _init_(self,*args,**kwargs):
        super(RegistrationForm,self)._init_(*args,**kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] ='Enter First Name'
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'
    def clean(self):
        cleaned_data=super(RegistrationForm,self).clean()
        password=cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')
        if password!=confirm_password:
            raise forms.ValidationError(
                "Password does not match!"
            )

