from django.contrib.auth.forms import AuthenticationForm as AuthAuthenticationForm
from django import forms
from django.utils.translation import ugettext_lazy as _
from account.forms import SignupForm as BaseSignupForm
from phonenumber_field.formfields import PhoneNumberField
from bootstrap_datepicker_plus import DatePickerInput


class AuthenticationForm(AuthAuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {
            'class': 'form-control',
        }
        self.fields['password'].widget.attrs = {
            'class': 'form-control',
        }

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                _("This account is inactive."),
                code='inactive',
            )


class SignupForm(BaseSignupForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    middle_name = forms.CharField()
    address = forms.CharField()
    phone_number = PhoneNumberField()
    birth_date = forms.DateField(
        label='Дата рождения',
        widget=DatePickerInput(
            options={
                "format": "DD.MM.YYYY",
                "showClose": True,
                "showClear": True,
                "showTodayButton": True,
                "locale": 'ru',
                "ignoreReadonly": True,
            }
        ),
        required=True,
        error_messages={
            'required': 'Введите дату вашего рождения'
        },
    )

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {
            'id': 'username',
            'class': 'form-control',
            'placeholder': 'Логин',
        }
        self.fields['first_name'].widget.attrs = {
            'id': 'first_name',
            'class': 'form-control',
            'placeholder': 'Имя',
        }
        self.fields['last_name'].widget.attrs = {
            'id': 'last_name',
            'class': 'form-control',
            'placeholder': 'Фамилия',
        }
        self.fields['middle_name'].widget.attrs = {
            'id': 'middle_name',
            'class': 'form-control',
            'placeholder': 'Отчетство',
        }
        self.fields['email'].widget.attrs = {
            'id': 'email',
            'class': 'form-control',
            'placeholder': 'E-mail',
        }
        self.fields['password'].widget.attrs = {
            'id': 'email',
            'class': 'form-control',
            'placeholder': 'Пароль',
        }
        self.fields['password_confirm'].widget.attrs = {
            'id': 'password_confirm',
            'class': 'form-control',
            'placeholder': 'Пароль еще раз',
        }
        self.fields['birth_date'].widget.attrs = {
            'id': 'birth_date',
            'class': 'form-control',
            'readonly': 'readonly',
        }
        self.fields['birth_date'].label = "Дата рождения"
        self.fields['address'].widget.attrs = {
            'id': 'address',
            'class': 'form-control',
        }
        self.fields['address'].label = "Адрес проживания"
        self.fields['phone_number'].widget.attrs = {
            'id': 'phone_number',
            'class': 'form-control',
        }
        self.fields['phone_number'].label = "Номер телефона"


class SpecifyParentForm(forms.Form):
    email = forms.EmailField(
        label=_("Email"),
        widget=forms.TextInput(),
        required=True,
    )

    def __init__(self, *args, **kwargs):
        super(SpecifyParentForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs = {
            'id': 'email',
            'class': 'form-control',
        }
