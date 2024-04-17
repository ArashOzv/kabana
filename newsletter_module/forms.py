from django import forms


class SubscribeForm(forms.Form):
    email = forms.EmailField(
        label="ایمیل",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'ایمیل'
            },
        ),
        required=True,
        error_messages={
            'required': 'لطفا ایمیل خود را وارد کنید',
        }
    )