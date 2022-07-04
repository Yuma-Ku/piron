from django.core.exceptions import ValidationError
from django import forms
from pironapp.models import User


def is_account_exist(v_email, v_password):
    user_info = User.objects.filter(login_id=v_email, password=v_password)
    return user_info.count() > 0


class LoginForm(forms.Form):
    login_id = forms.CharField(
        widget=forms.TextInput(attrs={
            "id": "login_id",
            "class": "form-control input-field",
            "placeholder": "メールアドレス"
        }), required=True
        # }), required=True, validators=[validators.EmailValidator()]
    )

    login_pass = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "id": "login_pass",
            "class": "form-control input-field",
            "placeholder": "パスワード"
        }), required=True
    )

    def clean(self):
        cleaned_data = super().clean()
        login_id = cleaned_data.get('login_id')
        login_pass = cleaned_data.get('login_pass')

        if not (login_id and login_pass):
            raise ValidationError('ログインIDとパスワードを入力してください。')

        if not is_account_exist(login_id, login_pass):
            raise ValidationError('ログインIDまたはパスワードが正しくありません。')
