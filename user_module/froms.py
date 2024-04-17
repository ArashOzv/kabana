
from django import forms


class SignupForm(forms.Form):
    username = forms.CharField(
        max_length=11,
        min_length=11,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'شماره تلفن',

        }),
        label='',
        required=True,
        error_messages={
            'required': 'لطفا شماره تلفن خود را وارد کنید',
        }


    )
    password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'رمز عبور',
        }),
        label='',
        required=True,
        error_messages={
            'required': 'لطفا رمز عبور خود را وارد کنید',
        }
    )
    repeat_password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'رمز عبور',
        }),
        label='',
        required=True,
        error_messages={
            'required': 'لطفا رمز عبور خود را وارد کنید',
        }
    )

    def clean_password2(self):
        pass1 = self.cleaned_data['password']
        pass2 = self.cleaned_data['repeat_password']
        if pass1 and pass2 and pass1 != pass2:
            raise forms.ValidationError('رمز عبور و تکرار آم مطابقت ندارند')
        return pass2
    


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'شماره تلفن',
        }),
        label='',
        required=True,
        error_messages={
            'required': 'لطفا شماره تلفن خود را وارد کنید',
        }
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'رمز عبور',
        }),
        label='',
        required=True,
        error_messages={
            'required': 'لطفا رمز عبور خود را وارد کنید',
        }
    )